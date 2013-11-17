'use strict';

angular.module('SmithsonianApp')
  .controller('MainCtrl', function ($scope, $rootScope, $location, $anchorScroll) {
    $rootScope.goTo = function (str) {
      $location.hash(str);
      $anchorScroll();
    };
  });
