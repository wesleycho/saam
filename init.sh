#!/bin/sh
# Initialize the server for production
echo "Update UI changes in ui/app and they will be added to cherrypy/static"
watch cp -rf ui/dist/* cherrypy/static
