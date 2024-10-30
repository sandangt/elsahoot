from contextlib import asynccontextmanager
import random

from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError

from app.model import Riddle
from app.resource.db import db_session
from app.resource.lorem import faker

async def init_db():
    riddle_list = []
    for _ in range(5000):
        number_of_answer = random.randint(4, 10)
        content_sentence_number = random.randint(7, 20)
        title_word_number = random.randint(5,15)
        answer_number = random.randint(0, number_of_answer - 1)
        riddle_list.append(
            Riddle(**{
                'title': faker.sentence(nb_words=title_word_number),
                'content': faker.paragraph(nb_sentences=content_sentence_number),
                'answer_list': faker.sentences(nb=number_of_answer),
                'answer': answer_number,
            })
        )
    with db_session.begin() as session:
        try:
            session.add_all(riddle_list)
            session.commit()
        except SQLAlchemyError:
            session.rollback()

@asynccontextmanager
async def init_app(app: FastAPI):
    await init_db()
    yield
