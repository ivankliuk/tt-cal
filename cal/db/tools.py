import itertools

from cal.db import Session
from cal.db.models import Date, Month


def load_defaults():
    """Default values for in-memory database."""
    c = itertools.cycle([4, 5, 6, 7, 1, 2, 3])
    dates = zip(
        [2015] * 90,
        [1] * 31 + [2] * 28 + [3] * 31,
        range(1, 32) + range(1, 29) + range(1, 32),
        [c.next() for _ in range(90)]
    )

    months = list(enumerate(
        ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"], start=1))

    session = Session()
    for date in dates:
        date = Date(
            year=date[0],
            month=date[1],
            day=date[2],
            dow=date[3])
        session.add(date)

    for month in months:
        date = Month(
            id=month[0],
            name=month[1])
        session.add(date)

    session.commit()
    session.close()
