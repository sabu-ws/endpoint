$(".onclick_object").click(function(){
	var href = $(this).closest("tr").find(".location").closest("a").attr("href")
	if(href) {
		window.location = href;
	}
});

// Return Button
$("#returnButton").click(function(){
	var url = window.parent.location.href;
	if(url.substr(url.length - 2) == "/"){
		url=url.slice(0,-1)
	}
	if(url.slice(url.lastIndexOf('/')) != '/scan/path/'){
		var to = url.lastIndexOf('/');
		to = to == -1 ? url.length : to + 1;
		url = url.substring(0, to -1 );
		window.location=url;
	}
});

$(function(){
	if(window.location.pathname != "/scan/path/"){
		$("#returnButton").removeAttr('hidden');
	}
});

// Detect Element
if($("#bodyBrowser").find('tr').is(':visible')){
	document.getElementById("noElementFound").style  = "display: none;";
}else{
	document.getElementById("noElementFound").style  = "display: True;";
}

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

