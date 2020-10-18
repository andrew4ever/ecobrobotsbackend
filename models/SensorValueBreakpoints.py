from app import db
from datetime import datetime


class SensorValueBreakpointsModel(db.Model):
    __tablename__ = 'sensor_value_breakpoints'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    sensor_value_type_id = db.Column(
        db.Integer
    )
    value_min = db.Column(
        db.Float,
        index=False,
        unique=False,
        nullable=False
    )
    value_max = db.Column(
        db.Float,
        index=False,
        unique=False,
        nullable=False
    )
    aqi_min = db.Column(
        db.Integer
    )
    aqi_max = db.Column(
        db.Integer
    )

    def __repr__(self):
        return '<SensorValueBreakpointsModel {}>'.format(self.sensor_value_type_id)

    def as_dict(self):
        r = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return r
