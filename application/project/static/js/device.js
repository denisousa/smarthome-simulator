var connect_{{device}} = true;

socket.on('{{device}}', function(data) {
    console.log('{{device}} working...' + data);
    document.querySelector("#{{device}}-sensors").innerHTML = '';
    delete data['data_from'];
    for(sensor in data){
        var p = document.createElement("p");
        if (sensor == 'temperature'){
            var value = document.createTextNode(capitalize(sensor + ": " + data[sensor] + " °C"));
        } else {
            var value = document.createTextNode(capitalize(sensor + ": " + data[sensor]));
        }
        p.appendChild(value);
        document.querySelector("#{{device}}-sensors").appendChild(p);
    }
});

document.getElementById("connect_{{device}}").addEventListener("click", function () {
    let Http = new XMLHttpRequest();
    if(connect_{{device}}) {
        Http.open("GET", "http://localhost:5002/disconnect_device_by_device_name/{{device}}", true);
        Http.send();
        connect_{{device}} = false;
        document.getElementById("connect_{{device}}").innerText = "Connect";
        document.getElementById("connect_{{device}}").className = "btn btn-info font-weight-bold";
        document.getElementById("{{device}}-sensors").style.color = "#990000";
        // updateStatus(connect_{{device}});
    } 
    else {
        Http.open("GET", "http://localhost:5002/connect_device_by_device_name/{{device}}", true);
        Http.send();
        connect_{{device}} = true;
        document.getElementById("connect_{{device}}").innerText = "Disconnect";
        document.getElementById("connect_{{device}}").className = "btn btn-warning text-dark font-weight-bold";
        document.getElementById("{{device}}-sensors").style.color = "#212529";
        // updateStatus(connect_{{device}});
    }
});


function updateStatus(connect_device) {
    try {
        document.getElementById("{{device}}-status").innerHTML = "";
     }
     catch (e) {
      console.log(e);  
     }
    if (connect_device) {
        var div = document.createElement("div");
        var node = document.createElement("p");
        div.setAttribute("id", "{{device}}-status");
        var textnode = document.createTextNode("Status: Connected");
        node.appendChild(textnode);
        div.appendChild(node);
        document.getElementById("header-{{device}}").appendChild(div);
    }
    else {
        var div = document.createElement("div");
        var node = document.createElement("p");
        div.setAttribute("id", "{{device}}-status");
        var textnode = document.createTextNode("Status: Disconnected");
        node.appendChild(textnode);
        div.appendChild(node);
        document.getElementById("header-{{device}}").appendChild(div);
    }
}

// socket.on('{{device}}_adapt', function(data) {
//     alert("Success Adapt: \n " + data);
// });