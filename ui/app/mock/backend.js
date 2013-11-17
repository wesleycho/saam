'use strict';

angular.module('mockBackend', ['ngMockE2E'])
  .run(function ($http, $httpBackend, route) {
    var mockData = {};

    $httpBackend.whenGET(/.*\.html$/).passThrough();
    $httpBackend.whenGET(/.*\.css$/).passThrough();
    $httpBackend.whenGET(/.*\.js$/).passThrough();
    $httpBackend.whenGET(/.*\.json$/).passThrough();

    $http.get('mock/data/new_york.json')
      .success(setData('new york'));

    function setData (key) {
      return function (data) {
        return mockData[key] = data;
      };
    }

    $httpBackend.whenGET(route.api + '/collections').respond(function (method, url, data) {
      var data = angular.fromJson(data);

      return [200, mockData[data.q.toLowerCase()]];
    });
  });
