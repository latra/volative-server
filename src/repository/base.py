from sqlalchemy.orm import Session
from sqlalchemy import ColumnExpressionArgument

class BaseRepository:

    def add(self, session: Session, entity: object):
        session.add(entity)
        session.commit()
        return entity

    def get(self, session: Session, entity_class: type, entity_id: object = None, query: ColumnExpressionArgument = None):
        if entity_id and not query:
            return session.query(entity_class).filter_by(uuid=entity_id).first()
        return session.query(entity_class).filter(query).first()

    def get_all(self, session: Session, entity_class: type):
        return session.query(entity_class).all()

    def update(self, session: Session):
        session.commit()

    def delete(self, session: Session, entity: object):
        session.delete(entity)
        session.commit()