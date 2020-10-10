from app import db
from datetime import datetime


class SensorDataModel(db.Model):
    __tablename__ = 'sensor_records'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    internal_id = db.Column(
        db.String(16),
        index=False,
        unique=False,
        nullable=False
    )
    latitude = db.Column(
        db.String(16),
        index=False,
        unique=False,
        nullable=False
    )
    longitude = db.Column(
        db.String(16),
        index=False,
        unique=False,
        nullable=False
    )
    altitude = db.Column(
        db.String(16),
        index=False,
        unique=False,
        nullable=False
    )
    recorded = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    pm25 = db.Column(
        db.Integer
    )
    pm100 = db.Column(
        db.Integer
    )
    o31 = db.Column(
        db.Integer
    )
    o38 = db.Column(
        db.Integer
    )
    co = db.Column(
        db.Integer
    )
    so2 = db.Column(
        db.Integer
    )
    no2 = db.Column(
        db.Integer
    )
    temp = db.Column(
        db.Integer
    )
    humi = db.Column(
        db.Integer
    )
    press = db.Column(
        db.Integer
    )
    pm1 = db.Column(
        db.Integer
    )
    nh3 = db.Column(
        db.Integer
    )
    co2 = db.Column(
        db.Integer
    )
    rad = db.Column(
        db.Integer
    )
    sound = db.Column(
        db.Integer
    )

    def __repr__(self):
        return '<SensorData {}>'.format(self.string_coords())

    def string_coords(self):
        return str(self.latitude) + '-' + str(self.longitude)

    def as_dict(self):
        r = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        r['recorded'] = str(r['recorded'])
        return r
