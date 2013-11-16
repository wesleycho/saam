'use strict';

angular.module('SmithsonianApp')
  .service('Collection', function ($resource) {
    var Collection = $resource('/api/collections/:id'),
      Tags = $resource('/api/collections/:id/tags', {}, {
        update: {method: 'PUT'}
      });

    return {
      get: function (id, params) {
        var defaultParams;
        
        defaultParams = {
          start: 0            
        };

        params = _.extend(defaultParams, params);

        if (_.isUndefined(id)) {
          params = _.extend(params, {id: id});
        }

        return Collection.get(params);
      },
      getTags: function (id, params) {
        params = _.extend(params, {id: id});
        return Tags.get(params);
      },
      createTag: function (id, data) {
        return Tags.save({id: id}, data);
      },
      modifyTag: function (id, data) {
        return Tags.update({id: id}, data);
      },
      deleteTag: function (id, data) {
        return Tags.delete({id: id}, data);
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
