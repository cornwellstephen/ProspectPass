pass.controller('PassController', function($scope, Student) {
        Student.query().$promise.then(function(data) {
        	$scope.students = data;
        });
        $scope.message = "hello world";
});