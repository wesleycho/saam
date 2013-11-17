'use strict';

var dev = true;

angular.module('SmithsonianApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngAnimate',
  'ui.router'
])
  .value('route', {
    api: dev ? 'http://localhost:9000/api' : 'http://localhost:8080/api'
  })
  .config(function () {
  });
