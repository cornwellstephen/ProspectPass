function PassDetailController($scope, $attrs, $element) {
    
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
        "#a7d2cb"  // super light blue
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
        "#96c1ba"
    ]

    this.randomColorIndex = 
        Math.floor(Math.random() * this.colors.length);

    this.buttonColor = this.colors[this.randomColorIndex];

    this.changeBackgroundColorDark = function() {
        this.buttonColor = this.colorsDarkened[this.randomColorIndex];
    }

    this.changeBackgroundColorLight = function() {
        this.buttonColor = this.colors[this.randomColorIndex];
    }

    this.getFormattedDate = function(dateString) {
        var date = new Date(dateString);
        return date.toDateString();
    }

    this.$onInit = function() {

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
