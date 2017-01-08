from pyramid.view import view_config
from twohundredvideos.services import scraper


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    return {'project': 'twohundredvideos', 'error': None, 'csv': None}


@view_config(route_name='home', renderer='templates/home.pt', request_method="POST")
def search(request):
    query = request.POST.get('search_query')
    error = None  # DO VALIDATION HERE FOR ERRORS
    csv = scraper.scrape(query)
    return {'project': 'twohundredvideos', 'error': error, 'csv': csv}
