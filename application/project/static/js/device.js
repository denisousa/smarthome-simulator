socket.on('{{device}}', function(data) {
    console.log('{{device}} working...' + data);
    document.querySelector(".{{device}}-sensors").innerHTML = '';
    for(sensor in data){
        var p = document.createElement("p");
        var value = document.createTextNode(sensor + ": " + data[sensor]);
        p.appendChild(value);
        document.querySelector(".{{device}}-sensors").appendChild(p);
    }
});