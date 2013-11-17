# Smithsonian Hackathon 2013
## Team Back Left

### About

This is some placeholder text that someone should update

### Technical Details

#### Components

*    Node.js: [MIT License](https://raw.github.com/joyent/node/v0.10.22/LICENSE)
*    CherryPy: [BSD License](https://bitbucket.org/cherrypy/cherrypy/src/697c7af588b8/cherrypy/LICENSE.txt)
*    Compass: [Slightly Modified MIT License](https://github.com/chriseppstein/compass/blob/stable/compass/blob/stable/LICENSE.markdown)
*    Grunt: [MIT License](https://github.com/gruntjs/grunt/blob/master/LICENSE-MIT) 

#### UI

*    Install [Node.js](http://nodejs.org)
*    Run `npm install -g grunt-cli bower` (will likely have to prefix with `sudo`)
*    In the `ui` directory, run `npm install` and then `bower install`
*    Install [Ruby](http://ruby-lang.org) (Wes: I recommend via [RVM](http://rvm.io))
*    In the command line, run `gem install compass modular-scale`
*    In another terminal window, navigate to `ui/app/styles` and run `compass watch ./`
*    If you want to see the page, just run `grunt server` and observe any changes automatically reflected by this browser!

##### Building Deployed Version of UI

*    Run `grunt build` (from `ui` directory)
*    Run `sh deploy.sh` (from the project root directory)
