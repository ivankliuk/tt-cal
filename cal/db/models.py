from sqlalchemy import Column, ForeignKey, Integer, String

from cal.db import Base, engine
from cal.utils import split_sequence


class Month(Base):
    __tablename__ = 'months'
    id = Column(Integer, primary_key=True)
    name = Column(String(10))

    def __repr__(self):
        return "<Month {}>".format(self.name)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name}


class Date(Base):
    __tablename__ = 'dates'
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    month = Column(Integer, ForeignKey('months.id'))
    day = Column(Integer)
    dow = Column(Integer)
    week = Column(Integer)

    def __repr__(self):
        return "<Date {}-{}-{}>".format(self.day, self.month, self.year)

    def serialize(self):
        return {
            "dow": self.dow,
            "day": self.day,
            "month": self.month,
            "year": self.year}

    @classmethod
    def get_months_of_year(cls, db_session, year):
        """Returns available months for given year."""
        dates = db_session.query(cls).distinct(cls.month).group_by(
            cls.month).all()
        months_ids = [date.month for date in dates]
        months = db_session.query(Month).filter(Month.id.in_(months_ids)).all()
        return {month.id: month.name for month in months}

    @classmethod
    def get_month_by_week(cls, db_session, **kwargs):
        """Returns nested list which is consumed by DataTable UI component."""
        dates = db_session.query(cls).filter_by(**kwargs).all()
        sorted_dates = sorted(dates)
        empty_days_prepend = sorted_dates[0].dow - 1
        empty_days_append = 7 - sorted_dates[-1].dow
        result = [""] * empty_days_prepend + \
                 [str(d.day) for d in sorted_dates] + [""] * empty_days_append
        return split_sequence(result, 7)

    def __cmp__(self, other):
        """Comparable interface implementation.
        Required for the objects sorting.
        """
        if self.year < other.year:
            return -1
        if self.year > other.year:
            return 1

        if self.month < other.month:
            return -1
        if self.month > other.month:
            return 1

        if self.day < other.day:
            return -1
        if self.day > other.day:
            return 1

        return 0


Base.metadata.create_all(engine)
