var socket = io.connect('http://localhost:5000');
var disconnect_bm = false;
var data_bm = false;

// colocar no util
const capitalize = (s) => {
    if (typeof s !== 'string') return ''
    return s.charAt(0).toUpperCase() + s.slice(1)
}

function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false);
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

{% for environment in environments %}
socket.on('{{environment}}', function (msg) {
    for (data in msg) {
        var p = document.createElement("p");
        if (data == 'temperature'){
            var value = document.createTextNode(capitalize(data + ": " + msg[data] + " °C"));
        } else {
            var value = document.createTextNode(capitalize(data + ": " + msg[data]));
        }
        p.appendChild(value);
        document.querySelector("#{{environment}}").appendChild(p);
    }
});
{% endfor %}

document.getElementById("start-environments").addEventListener("click", function () {
    console.log('Working...');
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "http://localhost:5001", false);
    xhr.send();
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            console.log(JSON.parse(xhr.responseText));
        }
    }
});
