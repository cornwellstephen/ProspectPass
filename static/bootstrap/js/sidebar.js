$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');
    });
});

// Disable function
jQuery.fn.extend({
    disable: function(state) {
        return this.each(function() {
            this.disabled = state;
        });
    }
});
$('#hint_button1').disable(false);

function toggleButton(number, max) {
	if (number == max) {
		$('#answer_button').disable(false);
	}
	else
		$('#hint_button' + (number + 1)).disable(false);
}
//
