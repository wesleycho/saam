'use strict';

angular.module('SmithsonianApp')
  .service('Collection', function ($resource, route) {
    var Collection = $resource(route.api + '/collections/:id'),
      Tags = $resource(route.api + '/collections/:id/tags', {}, {
        update: {method: 'PUT', url: '/:tagId'}
      });

    return {
      get: function (params, id) {
        var defaultParams;
        
        defaultParams = {
          start: 0 
        };

        params = _.extend(defaultParams, params);

        if (_.isUndefined(id)) {
          params = _.extend(params, {id: id});
        }

        return Collection.get(params).$promise;
      },
      getTags: function (id, params) {
        params = _.extend(params, {id: id});
        return Tags.get(params).$promise;
      },
      createTag: function (id, data) {
        return Tags.save({id: id}, data).$promise;
      },
      modifyTag: function (id, data) {
        return Tags.update({id: id}, data).$promise;
      },
      deleteTag: function (id, data) {
        return Tags.delete({id: id}, data).$promise;
      }
    };

    function resolve (deferred) {
      return function (data) {
        deferred.resolve(data);
      };
    }

    function reject (deferred) {
      return function (error) {
        deferred.reject(error);
      };
    }
  });
