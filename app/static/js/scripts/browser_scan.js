// Listen for click on toggle checkbox
$('#select-all').click(function(event) {   
    if(this.checked) {
        // Iterate each checkbox
        $(':checkbox').each(function() {
            this.checked = true; 
            $("#scan_button").addClass("bg-red-500 hover:bg-red-700");
            $("#scan_button").removeClass("bg-gray-500");
            $("#scan_button").removeAttr("disabled");                    
        });
    } else {
        $(':checkbox').each(function() {
            this.checked = false;
            $("#scan_button").addClass("bg-gray-500");
            $("#scan_button").removeClass("bg-red-500 hover:bg-red-700"); 
            $("#scan_button").attr("disabled",true);
        });
    }
}); 

// Color Scan button if folder/file is click
$("#checkbox-folder").click(function(event) {
    if(this.checked) {
        $("#scan_button").addClass("bg-red-500 hover:bg-red-700");
        $("#scan_button").removeClass("bg-gray-500");
        $("#scan_button").removeAttr("disabled"); 
    }
    else {
        $("#scan_button").addClass("bg-gray-500");
        $("#scan_button").removeClass("bg-red-500 hover:bg-red-700");
        $("#scan_button").attr("disabled",true);
    }
})
$("#checkbox-file").click(function(event) {
    if(this.checked) {
        $("#scan_button").addClass("bg-red-500 hover:bg-red-700");
        $("#scan_button").removeClass("bg-gray-500");
        $("#scan_button").removeAttr("disabled");   
    }
    else {
        $("#scan_button").addClass("bg-gray-500");
        $("#scan_button").removeClass("bg-red-500 hover:bg-red-700");
        $("#scan_button").attr("disabled",true); 
    }
})
