
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

    return "Left side is: {0} <br> Right side is: {1}".format(left_side, right_side)
