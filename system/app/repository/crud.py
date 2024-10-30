from typing import TypeVar, Generic, List, Optional, Type
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from app.exception.custom_exc import ItemNotFoundError
from app.model import ElsaBaseModel
from app.viewmodel.request import PaginationParams, OrderByParams

ModelType = TypeVar('ModelType', bound=ElsaBaseModel)


class CRUDRepository(Generic[ModelType]):
    _model_type: Type[ModelType] = NotImplemented

    def __init__(self, db_session: sessionmaker):
        self._db_session = db_session

    def get_all(self) -> List[ModelType]:
        with self._db_session.begin() as session:
            items = session.query(self._model_type).all()
            session.expunge_all()
        return items

    def get_all_paginated(self, pagination: PaginationParams, order_by: OrderByParams) -> List[ModelType]:
        offset, size = pagination.model_dump()
        direction, order_by_property = order_by.model_dump()
        with self._db_session.begin() as session:
            items = session.query(self._model_type) \
                .order_by(direction(getattr(self._model_type, order_by_property))) \
                .offset(offset * size) \
                .limit(size) \
                .all()
            session.expunge_all()  # change objs state from persistent to detached
        return items

    def get_multiple_by_ids(self, ids: List[int | UUID | str], order_by: OrderByParams) -> List[ModelType]:
        direction, order_by_property = order_by.model_dump()
        with self._db_session.begin() as session:
            items = session.query(self._model_type) \
                .filter(self._model_type.id.in_(ids)) \
                .order_by(direction(getattr(self._model_type, order_by_property))) \
                .all()
            session.expunge_all()
        return items

    def get_one_by_id(self, id: int | UUID | str) -> Optional[ModelType]:
        with self._db_session.begin() as session:
            item = session.get(self._model_type, id)
            if not item:
                raise ItemNotFoundError('Item Not Found')
            session.expunge_all()
        return item

    def create(self, item: ModelType) -> ModelType:
        with self._db_session.begin() as session:
            try:
                session.add(item)
                session.flush()
                session.expunge(item)
            except IntegrityError as ex:
                session.rollback()
                raise ex
        return item

    def create_multiple(self, items: List[ModelType]):
        with self._db_session.begin() as session:
            try:
                session.add_all(items)
                session.flush()
                session.expunge_all()
            except IntegrityError as ex:
                session.rollback()
                raise ex

    def patch_update(self, item: ModelType):
        with self._db_session.begin() as session:
            existed_item = session.get(self._model_type, item.id)
            if not existed_item:
                raise ItemNotFoundError('Item Not Found')
            for key, new_val in item.as_updatable_dict().items():
                if hasattr(existed_item, key):
                    setattr(existed_item, key, new_val)
            try:
                session.flush()
            except IntegrityError as ex:
                session.rollback()
                raise ex

    def patch_update_multiple(self, items: List[ModelType]):
        with self._db_session.begin() as session:
            existed_items = session.query(self._model_type) \
                .filter(self._model_type.id.in_([item.id for item in items])) \
                .all()
            for item in existed_items:
                if not (update_data := next((i for i in items if str(item.id) == str(i.id)), None)):
                    continue
                for key, new_val in update_data.as_updatable_dict().items():
                    if hasattr(item, key):
                        setattr(item, key, new_val)
            try:
                session.flush()
            except IntegrityError as ex:
                session.rollback()
                raise ex

    def upsert_multiple(self, items: List[ModelType]):
        existing_items = self.get_multiple_by_slugs([x.slug for x in items])
        existing_item_slugs = {x.slug for x in existing_items}
        updating_items = []
        for existing_item in existing_items:
            updating_item = next((x for x in items if x.slug == existing_item.slug))
            updating_item.id = existing_item.id
            updating_items.append(updating_item)
        creating_items = [x for x in items if x.slug not in existing_item_slugs]
        self.create_multiple(creating_items)
        self.patch_update_multiple(updating_items)

    def upsert(self, item: ModelType):
        existing_item = self.get_one_by_slug(item.slug)
        if not existing_item:
            self.create(item)
            return
        item.id = existing_item.id
        self.patch_update(item)

    def delete(self):
        raise NotImplementedError('Unimplemented Method')

    def count(self) -> int:
        with self._db_session.begin() as session:
            return session.query(func.count(self._model_type.id)).scalar()
