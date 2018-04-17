function PassDetailController($scope, $attrs, $element) {
    
    this.swapModalDetailToTransfer = function() {
        $("#passDetailModal"+this.passNum).modal('hide');
    };

    this.swapModalTransferToDetail = function() {
        $("#passTransferModal"+this.passNum).modal('hide');
    };

    // $scope.pass_user = django_variables.pass_user;
    // // $scope.pass_source = django_variables.pass_source;
    this.$onInit = function() {
        console.log(this.passObj);
        console.log(this.passNum);
        // console.log($scope.pass_date);
    };
}

angular.module('ProspectPassApp').component('passDetail', {
    templateUrl: 'passDetail.html',
    controller: PassDetailController,
    bindings: {
        passObj: '=',
        passNum: '<',
        passUser: '@'
    }
});

// 'static/passDetail.html'
