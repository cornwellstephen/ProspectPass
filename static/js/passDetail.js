function PassDetailController($scope, $attrs, $element, $http) {
    
    this.swapModalDetailToTransfer = function() {
        $("#passDetailModal"+this.passNum).modal('hide');
    };

    this.swapModalTransferToDetail = function() {
        $("#passTransferModal"+this.passNum).modal('hide');
    };

    this.colors = [
        "#e24e42", // red
        "#e9b000", // mustard
        "#eb6e80", // pink
        "#008f95", // greenish blue
        "#94618e", // purple
        "#8fd8f2", // light blue
        "#273f5f", // dark blue
        "#ee3377", // bright pink
        "#e5e358", // bright green
        "#a7d2cb", // super light blue
        "#11895a"  // green
    ];

    this.colorsDarkened = [
        "#d13d31", 
        "#d8a000", 
        "#da5d70", 
        "#007e84", 
        "#83507d", 
        "#7ec7e1", 
        "#062f4f", 
        "#dd2266", 
        "#d4d247", 
        "#96c1ba",
        "#007849"
    ]   

    this.buttonColor;

    this.sendUrl;

    this.changeBackgroundColorDark = function() {
        this.buttonColor = this.colorsDarkened[this.passObj[0].fields.color];
    }

    this.changeBackgroundColorLight = function() {
        this.buttonColor = this.colors[this.passObj[0].fields.color];
    }

    this.getFormattedDate = function(dateString) {
        var datebreak = dateString.split('-');
        var date = new Date(datebreak[0], datebreak[1]-1, datebreak[2]);
        return date.toDateString();
    }

    this.isDateToday = function(dateString) {
        var datebreak = dateString.split('-');
        var date = new Date(datebreak[0], datebreak[1]-1, datebreak[2]);
        var today = new Date();
        return date.toDateString() == today.toDateString();
    }

    this.$onInit = function() {
        this.sendUrl = "/sendpass/" + this.passId + "/";
        this.buttonColor = this.colors[this.passObj[0].fields.color];
    };

    this.activate = function(passId) {
      return $http.post('/activatepass/', {
        'pass_id': this.passId,
      });
    }

    this.transfer = function(netid, transferrable) {
       return $http.post(this.sendUrl, {
        'target': $scope.netid,
        'source': this.passUserNetid,
        'transferrable': $scope.transferrable
      });       
    }
    
}

angular.module('ProspectPassApp').component('passDetail', {
    templateUrl: 'passDetail.html',
    controller: PassDetailController,
    bindings: {
        passObj: '=',
        passNum: '<',
        passUser: '@',
        passId: '@',
        passUserNetid: '@',
    }
});
