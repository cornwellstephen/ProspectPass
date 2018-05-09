function PassDetailController($scope, $attrs, $element, $http, $window, $location, $document) {
    
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

    $scope.sendUrl;
    $scope.passUserNetid
    $scope.passId
    $scope.passNum
    this.getUser;
    this.transferError = false;

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
        $scope.sendUrl = "/sendpass/" + this.passId + "/";
        $scope.passUserNetid = this.passUserNetid
        $scope.passId = this.passId
        $scope.passNum = this.passNum
        this.buttonColor = this.colors[this.passObj[0].fields.color];
        var url = $window.location.href;
        if (url.includes("homepage")) {
            if (url.includes("transferfail") && url.includes($scope.passId)) {
                this.transferError = true;
                // how to get modal to show up?
                    // $("#passTransferModal"+this.passNum).modal('show');
                    // console.log("openModalButton" + this.passNum);
                    // console.log(document.getElementById("openModalButton" + this.passNum));
                    $(window).load(function() {
                        document.getElementById("openModal" + $scope.passNum).click()
                    });
                

            }
        }
    };

    this.activate = function(passId) {
      return $http.post('/activatepass/', {
        'pass_id': this.passId,
      });
    }

    this.transfer = function(netid, transferrable) {
        if ($scope.transferrable != true) {
            $scope.transferrable = false
        }
        this.getUser = "/restapi/students/" + $scope.netid + "/"; 
        $http({
        method: 'GET',
        url: this.getUser,
        }).then(function successCallback(response) {
                $window.location.href = '/homepage';
                return $http.post($scope.sendUrl, {
                'target': $scope.netid,
                'source': $scope.passUserNetid,
                'transferrable': $scope.transferrable
                });
            }, function errorCallback(response) {
                $window.location.href = '/homepage/#transferfail/' + $scope.passId;
                location.reload();
                return;
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
