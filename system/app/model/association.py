from sqlalchemy import ForeignKey, Table, Column

from app.model.base import ElsaBaseModel

quiz_riddle_association = Table(
    'quiz_riddle_association',
    ElsaBaseModel.metadata,
    Column('quiz_id', ForeignKey('quiz.id'), primary_key=True),
    Column('riddle_id', ForeignKey('riddle.id'), primary_key=True),
)
