// CSRF TOKEN 
$.ajaxSetup({
	beforeSend: function(xhr, settings) {
		if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrf_token);
		}
	}
});

// Dark mode
$("#ToggleDarkMode").click(function(){
	if(localStorage.theme === 'dark' ){
		localStorage.theme = 'light';
		document.documentElement.classList.remove('dark');
		$("#ToggleDarkModeIcon").removeClass("fa-moon");
		$("#ToggleDarkModeIcon").addClass("fa-sun");
	}else{
		document.documentElement.classList.add('dark');
		$("#ToggleDarkModeIcon").removeClass("fa-sun");
		$("#ToggleDarkModeIcon").addClass("fa-moon");
		localStorage.theme = 'dark';
	}
});

if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
	localStorage.theme = 'dark';
	document.documentElement.classList.add('dark');
	$("#ToggleDarkModeIcon").removeClass("fa-sun");
	$("#ToggleDarkModeIcon").addClass("fa-moon");
	$("#ToggleDarkMode").prop("checked",true);
} else {
	localStorage.theme = 'light';
	document.documentElement.classList.remove('dark');
	$("#ToggleDarkModeIcon").removeClass("fa-moon");
	$("#ToggleDarkModeIcon").addClass("fa-sun");
	$("#ToggleDarkMode").prop("checked",false);
}

// Box Alerts
if($(".boxInfo").is(':visible')){
	$(".boxInfo").delay(5000).fadeOut();
}