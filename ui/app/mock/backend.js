'use strict';

angular.module('mockBackend', ['ngMockE2E'])
  .run(function ($http, $httpBackend, route) {
    var mockData = {};

    $httpBackend.whenGET(/.*\.html$/).passThrough();
    $httpBackend.whenGET(/.*\.css$/).passThrough();
    $httpBackend.whenGET(/.*\.js$/).passThrough();
    $httpBackend.whenGET(/.*\.json$/).passThrough();

    $http.get('mock/data/all.json')
      .success(setData('all'));
    $http.get('mock/data/new_york.json')
      .success(setData('new york'));
    $http.get('mock/data/dc.json')
      .success(setData('dc'));
    $http.get('mock/data/san_francisco.json')
      .success(setData('san francisco'));
    $http.get('mock/data/los_angeles.json')
      .success(setData('los angeles'));
    $http.get('mock/data/chicago.json')
      .success(setData('chicago'));
    $http.get('mock/data/las_vegas.json')
      .success(setData('las vegas'));

    function setData (key) {
      return function (data) {
        return mockData[key] = data;
      };
    }

    $httpBackend.whenGET(/http:\/\/localhost:9000\/api\/collections(\?.*)?/).respond(function (method, url) {
      var q, dataToReturn;
      q = url.match(/q=[\w\+]*&/)[0];
      q = q.slice(0, -1);
      q = q.substr(2);
      q = q.replace(/\+/, ' ');

      if (q.toLowerCase() === '') {
        dataToReturn = _.cloneDeep(mockData.all);
      }
      else {
        dataToReturn = _.cloneDeep(mockData.all);
        dataToReturn.response.docs = _.filter(dataToReturn.response.docs, function (item) {
          return contains(dataToReturn.response.docs, q);
        });
      }

      dataToReturn.response.docs = _.sample(dataToReturn.response.docs, 10);

      return [200, dataToReturn];
    });

    function contains (collection, str) {
      for (var item in collection) {
        if (_.contains(collection[item], str)) {
          return true;
        }
        if (_(collection[item]).isArray() || _(collection[item]).isObject()) {
          if (contains(collection[item], str)) {
            return true;
          }
        }
      }

      return false;
    }
  });
