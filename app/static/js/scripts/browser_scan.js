// Listen for click on toggle checkbox
$('#select-all').click(function(event) {   
    var isChecked = this.checked;
    $(':checkbox').prop('checked', isChecked);
    updateScanButtonStyle();
});

$(':checkbox').change(function() {
    updateScanButtonStyle();
});

function updateScanButtonStyle() {
    var anyChecked = false;
    $(':checkbox').each(function() {
        if (this.checked) {
            anyChecked = true;
            return false;
        }
    });
    if (anyChecked) {
        $("#scan_button").addClass("bg-red-500 hover:bg-red-700").removeClass("bg-gray-500").removeAttr("disabled");                    
    } else {
        $("#scan_button").addClass("bg-gray-500").removeClass("bg-red-500 hover:bg-red-700").attr("disabled", true);
    }
}

// Color Scan button if folder/file is clicked
$("#checkbox-folder, #checkbox-file").click(function(event) {
    var isChecked = this.checked;
    $("#scan_button").toggleClass("bg-red-500 hover:bg-red-700", isChecked)
                     .toggleClass("bg-gray-500", !isChecked)
                     .prop("disabled", !isChecked);
});

