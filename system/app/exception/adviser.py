import dataclasses
import json
from dataclasses import dataclass
from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from .custom_exc import ItemNotFoundError


exception_map = []


@dataclass
class ErrorVm:
    message: str


# region Client Error
def not_found_exception_handler(_: Request, exc):
    content = ErrorVm(message='Item not found.')
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content=dataclasses.asdict(content))
exception_map.append((ItemNotFoundError, not_found_exception_handler))


def bad_request_exception_handler(_: Request, exc):
    content = ErrorVm(message='Duplicate unique key.')
    return JSONResponse(status_code=HTTPStatus.BAD_REQUEST, content=dataclasses.asdict(content))
exception_map.append((IntegrityError, bad_request_exception_handler))
# endregion


# region Server Error
def internal_server_error_exception_handler(_: Request, exc):
    if isinstance(exc, SQLAlchemyError):
        content = ErrorVm(message='Database error')
    elif isinstance(exc, ValueError):
        content = ErrorVm(message='Error.')
    return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, content=dataclasses.asdict(content))
exception_map.append((SQLAlchemyError, internal_server_error_exception_handler))
exception_map.append((ValueError, internal_server_error_exception_handler))
# endregion
