var temp_name_object = ""

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
	if(url.slice(url.lastIndexOf('/')) != '/browser/server/path/'){
		var to = url.lastIndexOf('/');
		to = to == -1 ? url.length : to + 1;
		url = url.substring(0, to -1 );
		window.location=url;
	}
});

$(function(){
	if(window.location.pathname != "/browser/server/path/"){
		$("#returnButton").removeAttr('hidden');
	}
});

// Detect Element
if($("#bodyBrowser").find('tr').is(':visible')){
	document.getElementById("noElementFound").style  = "display: none;";
}else{
	document.getElementById("noElementFound").style  = "display: True;";
}


// Remove element 
$(".delete_object_name").click(function(){
	temp_name_object=$(this).closest("tr").find(".object_name").text().trim()
});

// Yes button
$(".yesButtonDeleteObject").click(function(e){
	var get_url=window.location.pathname.split("/").slice(4).join("/")
	e.preventDefault()
	console.log(temp_name_object)
	$.ajax({
		type: "GET",
		url: "/browser/server/delete/"+get_url+"/"+temp_name_object,
		success: function(data){
			if(data == "ok"){
				window.location.reload();
			}
		}
	});
});
