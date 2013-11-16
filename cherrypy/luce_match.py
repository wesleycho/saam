
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

##    return "Left side is: {0} -- {1} <br> Right side is: {2} -- {3}".format(left_side, left_request_url, right_side, right_request_url)
##    return "Left is: {0} -- {1} <br> Right is: {2} -- {3}".format(left_image_url, left_title, right_image_url, right_title)

    ## ABOVE: COLLECT AND PROCESS
    ## BELOW: DISPLAY

    page_source = []

    page_source.append('<link rel="stylesheet" type="text/css" href="/static/main.css"> <link rel="stylesheet" type="text/css" href="/static/gumby.css">')

    page_source.append('<h1>Which one do you like?</h1>')

    page_source.append('<img src="{0}" alt="{1}"> <img src="{2}" alt="{3}">'.format(left_image_url, left_title, right_image_url, right_title))

    return page_source
