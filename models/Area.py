from app import db
from datetime import datetime


class AreaModel(db.Model):
    __tablename__ = 'aqi_records'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    aqi = db.Column(
        db.Integer,
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
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False,
        default=datetime.now()
    )
    pm25 = db.Column(
        db.String(16),
        nullable=True
    )
    pm100 = db.Column(
        db.String(16),
        nullable=True
    )
    o31 = db.Column(
        db.String(16),
        nullable=True
    )
    o38 = db.Column(
        db.String(16),
        nullable=True
    )
    co = db.Column(
        db.String(16),
        nullable=True
    )
    so2 = db.Column(
        db.String(16),
        nullable=True
    )
    no2 = db.Column(
        db.String(16),
        nullable=True
    )
    temp = db.Column(
        db.String(16),
        nullable=True
    )
    humi = db.Column(
        db.String(16),
        nullable=True
    )
    press = db.Column(
        db.String(16),
        nullable=True
    )
    pm1 = db.Column(
        db.String(16),
        nullable=True
    )
    nh3 = db.Column(
        db.String(16),
        nullable=True
    )
    co2 = db.Column(
        db.String(16),
        nullable=True
    )
    rad = db.Column(
        db.String(16),
        nullable=True
    )
    sound = db.Column(
        db.String(16),
        nullable=True
    )

    def __repr__(self):
        return '<Area {}>'.format(self.string_coords())

    def string_coords(self):
        return str(self.latitude) + '-' + str(self.longitude)

    def as_dict(self):
        r = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        r['created'] = str(r['created'])
        return r
