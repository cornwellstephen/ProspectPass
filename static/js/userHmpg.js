angular.module('ProspectPassApp')
    .controller('ProspectUserCtrl', function ProspectUserCtrl() {
    
        this.hasDatePassed = function(dateString) {
            // console.log(dateString);
            var today = new Date();
            var yesterday = new Date(today);
            yesterday.setDate(today.getDate() - 1);
            // console.log(yesterday);

            var passDate = new Date(dateString);
            // console.log(passDate > yesterday);
            return passDate > yesterday;
        }

        this.hasCurrentPass = function(passList) {
            return true;
        }

    }
);
