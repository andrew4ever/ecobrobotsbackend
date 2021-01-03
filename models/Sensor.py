from app import db
from datetime import datetime


class SensorModel(db.Model):
    __tablename__ = 'sensor'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(16),
        index=False,
        unique=False,
        nullable=False
    )
    is_active = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=False
    )
    created_at = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False,
        default=datetime.now()
    )
    modified_at = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False,
        default=datetime.now()
    )
    external_id = db.Column(
        db.String(16),
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<Sensor {}>'.format(self.external_id)

    def as_dict(self):
        r = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return r
