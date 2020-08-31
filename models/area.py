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
        db.Float,
        index=False,
        unique=False,
        nullable=False
    )
    longitude = db.Column(
        db.Float,
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

    def __repr__(self):
        return '<Area {}>'.format(self._string_coords())

    def _string_coords(self):
        return str(self.latitude) + '-' + str(self.longitude)
