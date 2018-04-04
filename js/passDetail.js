function PassDetailController($scope, $attrs, $element) {
    
    this.$onInit = function() {
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
