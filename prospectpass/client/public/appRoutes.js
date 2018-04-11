angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'pass',
        url: '/',
        templateUrl: 'public/components/pass/templates/pass.template',
        controller: 'PassController'
    });

    $urlRouterProvider.otherwise('/');
}]);