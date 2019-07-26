import urllib.request,json
from .models import Article,Category,Source,Headlines

# Api key
api_key = None
# Source url
source_url = None
# Source url
cat_url = None

def configure_request(app):
    global api_key, source_url, cat_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_API_SOURCE_URL']
    cat_url = app.config['CAT_API_URL']


def get_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url=source_url.format(api_key)
    # print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response =
        json.loads(get_source_data)

        source_results = None
