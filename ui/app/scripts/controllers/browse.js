'use strict';

angular.module('SmithsonianApp')
  .controller('BrowseCtrl', function ($scope, $q, Collection) {
    var itemPage = 0;
    $scope.columns = [];
    $scope.param = {};

    generateColumns();

    $scope.updateFilter = function (filter) {
      return _.debounce(function (filter) {
        var promises = [];
        itemPage = 0;

        _.each(_.range(0, 6), function (idx) {
          promises.push(requestFilteredItems(filter, itemPage * 60 + idx * 10));
          if (idx === 5) {
            itemPage++;
          }
        });

        $q.all(promises).then(function (data) {
          $scope.columns = [];
          generateColumns();
          fillColumns(data);
        });
      }, 200);
    };

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
        fillData(data);
      });
    };

    function requestItems (startIdx) {
      return Collection.get({
        q: $scope.param.filter ? $scope.param.filter : '',
        rows: 10,
        start: startIdx
      });
    }

    function requestFilteredItems (filter, startIdx) {
      return Collection.get({
        q: filter,
        rows: 10,
        start: startIdx
      });
    }

    function generateColumns () {
      _.each(_.range(0, 6), function (idx) {
        $scope.columns.push({ images: [] });
      });
    }

    function fillData (data) {
      _.each(data, function (actualData, idx) {
        Array.prototype.push.apply($scope.columns[idx].images, actualData.response.docs);
      });
    }
  });
