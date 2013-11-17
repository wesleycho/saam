#!/usr/local/bin/python2.7

# Cherrypy backend for LuceHack
# 2013 November 16

# Team Back Left

import cherrypy

class api(object):

    from luce_api import collections as collections
    collections.exposed = True
    
    @cherrypy.expose
    def search(self, **kwargs):
        return "search"


class Root(object):

    api = api()

    from luce_index import luce_index as index
    index.exposed = True

    from luce_match import luce_match
    luce_match.exposed = True

    lucemash = luce_mash = luce_match
    lucemash.exposed = luce_mash.exposed = True

    from luce_match_score import luce_match_score
    luce_match_score.exposed = True

    from luce_zoom import luce_zoom
    luce_zoom.exposed = True

    from luce_zoom_score import luce_zoom_score
    luce_zoom_score.exposed = True

    from luce_learn_more import luce_learn_more as learn_more
    learn_more.exposed = True

if __name__ == '__main__':

    import os.path
    current_dir = os.path.dirname(os.path.abspath(__file__))

    cherrypy.config.update({'server.socket_port': 8080,
                            'server.socket_host': '127.0.0.1',
                            'log.screen': True,
                            'log.error_file': 'site.log'
                            })

    conf = {'/static': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': os.path.join(current_dir, 'static'),
                        }
            }
    
    cherrypy.quickstart(Root(), '/', config=conf)
