'use strict';

angular.module('SmithsonianApp')
  .controller('ObjectCtrl', function ($scope, $state) {
    if ($state.current.data) {
      $scope.image = $state.current.data.image;
    }

    $scope.goTo = function (string) {
      if (string === 'similar') {
        var browseState = $state.get('browse');
        browseState.data = {};
        browseState.data.topic = $scope.image.indexedStructured.topic[0];
        $state.go('browse');
      }
    };
  });
