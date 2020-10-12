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
        db.String(16)
    )
    pm100 = db.Column(
        db.String(16)
    )
    o31 = db.Column(
        db.String(16)
    )
    o38 = db.Column(
        db.String(16)
    )
    co = db.Column(
        db.String(16)
    )
    so2 = db.Column(
        db.String(16)
    )
    no2 = db.Column(
        db.String(16)
    )
    temp = db.Column(
        db.String(16)
    )
    humi = db.Column(
        db.String(16)
    )
    press = db.Column(
        db.String(16)
    )
    pm1 = db.Column(
        db.String(16)
    )
    nh3 = db.Column(
        db.String(16)
    )
    co2 = db.Column(
        db.String(16)
    )
    rad = db.Column(
        db.String(16)
    )
    sound = db.Column(
        db.String(16)
    )

    def __repr__(self):
        return '<SensorData {}>'.format(self.string_coords())

    def string_coords(self):
        return str(self.latitude) + '-' + str(self.longitude)

    def as_dict(self):
        r = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        r['recorded'] = str(r['recorded'])
        return r
