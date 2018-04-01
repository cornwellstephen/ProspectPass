function PassDetailController($scope, $attrs, $element) {
    
    this.$onInit = function() {
        // confuzzed(this.passObj);
    };

}

// function confuzzed(str) {
//     console.log(str);
// }

angular.module('ProspectPassApp').component('passDetail', {
    templateUrl: 'passDetail.html',
    controller: PassDetailController,
    bindings: {
        passObj: '='
    }
});
