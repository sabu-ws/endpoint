$(document).ready(function(e){
	console.log("start")
	var socket = io.connect("/usb");
	socket.emit("state_usb");
	socket.on("ret_state_usb",function(data){
		if (data){
			console.log(data)
		}else{
			console.log(data)
		}
	})
});