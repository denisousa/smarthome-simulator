socket.on('{{device}}', function(data) {
    console.log('{{device}} working...' + data);
    document.querySelector(".{{device}}-sensors").innerHTML = '';
    delete data['data_from'];
    for(sensor in data){
        var p = document.createElement("p");
        if (sensor == 'temperature'){
            var value = document.createTextNode(capitalize(sensor + ": " + data[sensor] + " °C"));
        } else {
            var value = document.createTextNode(capitalize(sensor + ": " + data[sensor]));
        }
        p.appendChild(value);
        document.querySelector(".{{device}}-sensors").appendChild(p);
    }
});

// socket.on('{{device}}_adapt', function(data) {
//     alert("Success Adapt: \n " + data);
// });