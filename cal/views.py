""" Cornice services.
"""

from cornice import Service
from pyramid.renderers import render_to_response
from cornice.resource import resource, view

from cal.db import Session
from cal.db.models import Date, Month

db_session = Session()

index = Service(name='index', path='/', description="Calendar index page")


@index.get()
def get_info(request):
    """Returns index page."""
    return render_to_response('templates/index.mako', {}, request=request)


class BaseView(object):
    model = None

    def __init__(self, request):
        self.request = request

    def collection_get(self):
        """Returns all the model data as a list."""
        data = db_session.query(self.model).all()
        return [d.serialize() for d in data]


@resource(collection_path='/cal', path='/cal/{year}/{month}')
class CalendarView(BaseView):

    model = Date

    @view(renderer='json')
    def get(self):
        year = self.request.matchdict['year']
        month = self.request.matchdict['month']
        return Date.get_month_by_week(Session(), year=year, month=month)


@resource(collection_path='/month', path='/month/{year}')
class MonthView(BaseView):

    model = Month

    @view(renderer='json')
    def get(self):
        year = self.request.matchdict['year']
        return Date.get_months_of_year(Session(), year=year)
