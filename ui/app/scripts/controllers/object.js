'use strict';

angular.module('SmithsonianApp')
  .controller('ObjectCtrl', function ($scope, $state) {
    $scope.image = $state.current.data;
    console.log($scope.image);
  });
