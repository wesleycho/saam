
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



if __name__ == '__main__':
    
    cherrypy.config.update({'server.socket_port': 8080,
                            'server.socket_host': '127.0.0.1',
                            'log.screen': True,
                            })
    
    cherrypy.quickstart(Root(), '/')
