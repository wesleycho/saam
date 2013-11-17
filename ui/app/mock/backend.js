'use strict';

angular.module('mockBackend', ['ngMockE2E'])
  .run(function ($httpBackend) {
    $httpBackend.whenGET(/.*\.html$/).passThrough();
    $httpBackend.whenGET(/.*\.css$/).passThrough();
    $httpBackend.whenGET(/.*\.js$/).passThrough();
  });
