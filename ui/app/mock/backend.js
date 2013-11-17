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
    $http.get('mock/data/dc.json')
      .success(setData('dc'));
    $http.get('mock/data/san_francisco.json')
      .success(setData('san francisco'));
    $http.get('mock/data/los_angeles.json')
      .success(setData('los angeles'));

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
