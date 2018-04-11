angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'pass',
        url: '/',
        templateUrl: '/static/pass.template',
        controller: 'PassController'
    });

    $urlRouterProvider.otherwise('/');
}]);