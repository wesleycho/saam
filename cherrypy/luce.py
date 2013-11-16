
# Cherrypy backend for LuceHack
# 2013 November 16

# Team Back Left

import cherrypy

class Root(object):

    from luce_index import luce_index as index
    index.exposed = True

if __name__ == '__main__':
    
    cherrypy.config.update({'server.socket_port': 8080,
                            'server.socket_host': '127.0.0.1',
                            'log.screen': True,
                            })
    
    cherrypy.quickstart(Root(), '/')
