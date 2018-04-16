function PassDetailController($scope, $attrs, $element) {
    
    this.swapModalDetailToTransfer = function() {
        $("#passDetailModal"+this.passNum).modal('hide');
    };

    this.swapModalTransferToDetail = function() {
        $("#passTransferModal"+this.passNum).modal('hide');
    };

    // $scope.c = Constants.all();
    // $scope.pass = $scope.m.in[Constants.get("pass")];
    // $scope.pass_date = django_variables.pass_date;
    // $scope.club_name = django_variables.club_name;
    // $scope.pass_user = django_variables.pass_user;
    // $scope.pass_source = django_variables.pass_source;
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
        passNum: '<'
    }
});

// 'static/passDetail.html'
