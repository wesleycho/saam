#!/bin/sh
# Initialize the server for production
echo "Update UI changes in ui/app and they will be added to cherrypy/static"
pushd ui
grunt build
popd
rm -rf cherrypy/static/*
cp -rf ui/dist/* cherrypy/static
