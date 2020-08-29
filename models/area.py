from app import db


class Area(db.Model):
    __tablename__ = 'aqi-records'

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
        nullable=False
    )

    def __repr__(self):
        return '<Area {}>'.format(self._string_coords())

    def _string_coords(self):
        return str(self.latitude) + '-' + str(self.longitude)
