'use strict';

angular.module('mockBackend', ['ngMockE2E'])
  .run(function ($httpBackend) {
    $httpBackend.passThrough(/.*\.html$/);
    $httpBackend.passThrough(/.*\.css$/);
    $httpBackend.passThrough(/.*\.js$/);
  });
