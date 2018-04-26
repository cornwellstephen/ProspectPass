angular.module('ProspectPassApp', []);

angular.module('ProspectPassApp', []).
  config(function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  });