angular.module('ProspectPassApp')
    .controller('ProspectUserCtrl', 
        function ProspectUserCtrl($window, 
            $location, 
            $anchorScroll) {
    
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

        this.officerfail = false;
        this.createfail = false;
        this.distributefail = false;
        this.uploadfail = false;
        this.officersuccess = false;
        this.createsuccess = false;
        this.distributesuccess = false;
        this.uploadsuccess = false;

        this.$onInit = function() {

            var url = $window.location.href;
            if (url.includes("admin-homepage")) {
                if (url.includes("officerfail")) {
                    this.officerfail = true;
                    $location.hash("NewClubOfficer");
                    $anchorScroll();
                }
                else if (url.includes("officersuccess")) {
                    this.officersuccess = true;
                    $location.hash("NewClubOfficer");
                    $anchorScroll();
                }
                else if (url.includes("createfail")) {
                    this.createfail = true;
                    $location.hash("CreatePassForm");
                    $anchorScroll();
                }
                else if (url.includes("createsuccess")) {
                    this.createsuccess = true;
                    $location.hash("CreatePassForm");
                    $anchorScroll();
                }
                else if (url.includes("distributefail")) {
                    this.distributefail = true;
                    $location.hash("DistributePassForm");
                    $anchorScroll();
                }
                else if (url.includes("distributesuccess")) {
                    this.distributesuccess = true;
                    $location.hash("DistributePassForm");
                    $anchorScroll();
                }
                else if (url.includes("uploadfail")) {
                    this.uploadfail = true;
                    $location.hash("UpdateMembersForm");
                    $anchorScroll();
                }
                else if (url.includes("uploadsuccess")) {
                    this.uploadsuccess = true;
                    $location.hash("UpdateMembersForm");
                    $anchorScroll();
                }
            }

            for (var i = 0; i < 11; i++) {
                if ($("#id_color").find("[for='id_color_"+i+"']")[0] != undefined) {
                    var label = $("#id_color").find("[for='id_color_"+i+"']")[0].innerText;
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
