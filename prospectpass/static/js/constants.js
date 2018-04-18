angular.module('ProspectPassApp').factory('Constants', ['DjangoConstants', function(DjangoConstants) {
  // pull in the django constants
  angular.extend(constants, DjangoConstants);
 
  return {
    get: function(key) {
      return constants[key];
    },
    // this is a handy way to make all constants available in your HTML 
    // e.g. $scope.c = Constants.all() 
    all: function() {
      return constants;
    }
  };
}]);