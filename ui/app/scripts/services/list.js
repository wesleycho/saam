'use strict';

angular.module('SmithsonianApp')
  .service('List', function ($resource, route) {
    var List = $resource(route.api + '/lists/:id', {}, {
      update: {method: 'PUT'},
      merge: {method: 'POST'},
      approve: {method: 'POST'},
      getItems: {method: 'GET', url: '/items'},
      addItem: {method: 'POST', url: '/items/:itemId'},
      modifyItem: {method: 'PUT', url: '/items/:itemId'},
      deleteItem: {method: 'DELETE', url: '/items/:itemId'}
    });
  });
