angular.module('ProspectPassApp')
    .controller('ProspectUserCtrl', function ProspectUserCtrl($window) {
    
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

        this.$onInit = function() {
            // console.log($window.location.href);

            for (var i = 0; i < 11; i++) {
                if ($("#id_color").find("[for='id_color_"+i+"']")[0] != undefined) {
                    var label = $("#id_color").find("[for='id_color_"+i+"']")[0].innerText;
                    // $("#id_color").find("[for='id_color_"+i+"']")[0].empty();
                    $("#id_color").find("[for='id_color_"+i+"']")[0].innerHtml =
                        '<input type="radio"' +
                            'name="color"' +
                            'value="'+i+'" ' +
                            'class="admin-hmpg-form-radios"' +
                            'placeholder="What color should this pass be?"' +
                            'id="id_color_'+i+'"' +
                            '>';
                    $("#id_color").find("[for='id_color_"+i+"']").css({
                        'background-color': label,
                        'color': label
                    });
                    $("#id_color").find('li').find(':contains('+label+')').each(function(){
                        $(this).html($(this).html().split(label).join(""));
                    });
                }
            }
        };
    }
);
