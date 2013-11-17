'use strict';

angular.module('SmithsonianApp')
  .controller('BrowseCtrl', function ($scope, $q, Collection) {
    var itemPage = 0;
    $scope.columns = [];
    _.each(_.range(0, 6), function (idx) {
      $scope.columns.push({ images: [] });
    });

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
        _.each(data, function (actualData, idx) {
          Array.prototype.push.apply($scope.columns[idx].images, actualData.response.docs);
        });
        console.log($scope.columns);
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
