from app import db
from datetime import datetime


class SensorValueTypeModel(db.Model):
    __tablename__ = 'sensor_value_type'

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
    type = db.Column(
        db.String(16),
        index=False,
        unique=False,
        nullable=False
    )
    round_digits = db.Column(
        db.Integer
    )
    max_possible_value = db.Column(
        db.String(16)
    )
    is_in_aqi = db.Column(
        db.Integer
    )
    calculate_period = db.Column(
        db.Integer
    )

    def __repr__(self):
        return '<SensorValueTypeModel {}>'.format(self.name)

    def as_dict(self):
        r = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return r
