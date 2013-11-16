
# Cherrypy backend for LuceHack
# 2013 November 16

# Team Back Left

def luce_match(self, **kwargs):

    from luce_credentials import username, password

    import random
    import requests
    from requests.auth import HTTPBasicAuth

    max_random = 31114 # Luce has this many images

    right_side = left_side = random.randint(1, max_random)

    while right_side == left_side:
        right_side = random.randint(1, max_random)

    left_request_url = 'http://edan-api.si.edu/metadataService?applicationID=HACK&rows=1&start={0}&wt=json&fq=online_media_type:Images'.format(left_side)
    right_request_url = 'http://edan-api.si.edu/metadataService?applicationID=HACK&rows=1&start={0}&wt=json&fq=online_media_type:Images'.format(right_side)

    left_response = requests.get(left_request_url, auth=HTTPBasicAuth(username, password)).json()
    right_response = requests.get(right_request_url, auth=HTTPBasicAuth(username, password)).json()

    left_image_url = left_response['response']['docs'][0]['descriptiveNonRepeating']['online_media']['media'][0]['content']
    right_image_url = right_response['response']['docs'][0]['descriptiveNonRepeating']['online_media']['media'][0]['content']

    left_title = left_response['response']['docs'][0]['descriptiveNonRepeating']['title']['content']
    right_title = right_response['response']['docs'][0]['descriptiveNonRepeating']['title']['content']

    ## ABOVE: COLLECT AND PROCESS
    ## BELOW: DISPLAY

    page_source = []

    page_source.append('<link rel="stylesheet" type="text/css" href="/static/main.css"> <link rel="stylesheet" type="text/css" href="/static/gumby.css">')

    page_source.append('<div class="row"> <h2>Click the artwork you like better.</h2>')

    page_source.append('<div class="six columns quickMargin">')
    page_source.append('<a href="luce_match?vote={0}"><img src="{1}" alt="{2}"></a>'.format(left_side, left_image_url, left_title))
    page_source.append('</div>')

    page_source.append('<div class="five columns">')
    page_source.append('<a href="luce_match?vote={0}"><img src="{1}" alt="{2}"></a>'.format(right_side, right_image_url, right_title))
    page_source.append('</div>')

    page_source.append('</div>')

    page_source.append('<div class="row">')
    page_source.append('<h6><a href="luce_match_score">View the all-time favorites</a></h6>')
    page_source.append('</div>')

    return page_source

def vote(art_id):

    import psycopg2

    try:
        art_id = int(art_id)
        assert 0 < art_id <= 31114 # Luce has this many images
    except Exception:
        return False

    from luce_database_credentials import database_connection_details as database_connection_details

    database_connection = psycopg2.connect(database_connection_details)
    database_cursor = database_connection.cursor()

    insert_query = 'insert into sidebyside (image_id) values ({0})'.format(art_id)

    database_cursor.execute(insert_query)
    database_connection.commit()

    return True
