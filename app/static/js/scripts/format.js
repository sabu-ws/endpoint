$(document).ready(function(e){
	var socket = io.connect("/format");
    socket.emit(type);
	socket.on("recv_format",function(){
		window.location = "/format/end"
	})
});