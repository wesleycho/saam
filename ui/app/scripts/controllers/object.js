'use strict';

angular.module('SmithsonianApp')
  .controller('ObjectCtrl', function ($scope, $state) {
    console.log($state);
    $scope.image = $state.current.data.image;
    console.log($scope.image);
  });
