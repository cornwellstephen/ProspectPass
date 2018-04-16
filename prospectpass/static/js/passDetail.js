function PassDetailController($scope, $attrs, $element) {
    
    this.$onInit = function() {
        console.log(this.passObj);
        console.log(this.passNum);
    };

    this.swapModalDetailToTransfer = function() {
        $("#passDetailModal"+this.passNum).modal('hide');
    };

    this.swapModalTransferToDetail = function() {
        $("#passTransferModal"+this.passNum).modal('hide');
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
