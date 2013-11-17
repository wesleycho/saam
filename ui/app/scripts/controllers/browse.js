'use strict';

angular.module('SmithsonianApp')
  .controller('BrowseCtrl', function ($scope, $q, Collection) {
    var itemPage = 0;
    $scope.columns = [];

    $scope.requestMoreItems = function () {
      var promises;
      promises = [];

      _.each(_.range(0, 6), function (idx) {
        promises.push(requestItems(itemPage * 60 + idx * 10));
        if (idx === 5) {
          itemPage++;
        }
      });

      $q.all(promises).then(function (data) {
        _.each(data, function (actualData) {
          $scope.columns.push(actualData.response.docs);
        });
      });
    };

    function requestItems (startIdx) {
      return Collection.get({
        q: '',
        rows: 10,
        start: startIdx
      });
    }
  });
