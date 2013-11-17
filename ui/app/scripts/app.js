'use strict';

var modules = [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngAnimate',
  'ui.router',
  'infinite-scroll'
];

if (dev) {
  modules.push('mockBackend');
}

angular.module('SmithsonianApp', modules)
  .value('route', {
    api: dev ? 'http://localhost:9000/api' : 'http://localhost:8080/api'
  })
  .config(function () {
  });
