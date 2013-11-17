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
  .config(function ($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.when('', '/');
    $stateProvider.state('main', {
      url: '/',
      views: {
        'main': {
          controller: 'MainCtrl',
          templateUrl: 'views/main.html'
        }
      }
    })
    .state('tour', {
      url: '/tour',
      views: {
        'main': {
          controller: 'TourCtrl',
          templateUrl: 'views/tour.html'
        }
      }
    })
    .state('browse', {
      url: '/browse',
      views: {
        'main': {
          controller: 'BrowseCtrl',
          templateUrl: 'views/browse.html'
        }
      }
    })
    .state('favorite', {
      url: '/favorite',
      views: {
        'main': {
          controller: 'FavoriteCtrl',
          templateUrl: 'views/favorite.html'
        }
      }
    })
    .state('item', {
      url: '/item/:itemId',
      views: {
        'main': {
          controller: 'ObjectCtrl',
          templateUrl: 'views/object.html'
        }
      }
    })
    ;
  });
