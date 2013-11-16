
# Cherrypy backend for LuceHack
# 2013 November 16

# Team Back Left

def luce_match(self, **kwargs):

    import random
    import requests

    max_random = 31114 # Luce has this many images

    right_side = left_side = random.randint(1, max_random)

    while right_side == left_side:
        right_side = random.randint(1, max_random)

    left_request_url = 'http://edan-api.si.edu/metadataService?rows=1&start={0}&wt=json&fq=online_media_type:Images'.format(left_side)
    right_request_url = 'http://edan-api.si.edu/metadataService?rows=1&start={0}&wt=json&fq=online_media_type:Images'.format(right_side)

        

    return "Left side is: {0} -- {1} <br> Right side is: {2} -- {3}".format(left_side, left_request_url, right_side, right_request_url)
