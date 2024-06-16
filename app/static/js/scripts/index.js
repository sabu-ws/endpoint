$(document).ready(function(e){
	console.log("start")
	var socket = io.connect("/usb");
	socket.emit("state_usb");
	socket.on("ret_state_usb",function(data){
		if (data){
			if($("#state_usb").text() == "Not connected"){
				$("#state_usb").text("Connected")
				$("#state_usb").removeClass("text-red-500")
				$("#state_usb").addClass("text-green-500")
			}
		}else{
			if($("#state_usb").text() == "Connected"){
				$("#state_usb").text("Not connected")
				$("#state_usb").removeClass("text-green-500")
				$("#state_usb").addClass("text-red-500")
			}
		}
	})
});