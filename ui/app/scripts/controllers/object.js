'use strict';

angular.module('SmithsonianApp')
  .controller('ObjectCtrl', function ($scope, $state) {
    if ($state.current.data) {
      $scope.image = $state.current.data.image;
    }
  });
