function changeColor(background, color, className){
    var components = document.querySelectorAll(className)
    for(var i = 0; i < components.length; i++){
        components[i].style.backgroundColor = background;
        components[i].style.color = color;
    }
}

function removeDisable(){
    var buttons = document.getElementsByTagName('button');
    for (let i = 0; i < buttons.length; i++) {
        let button = buttons[i];
        button.disabled = false;
    }
}

function getCurrentTime(){
    var date = new Date();
    var seconds = date.getSeconds();
    var minutes = date.getMinutes();
    var hour = date.getHours();
    return `Time: ${hour}:${seconds}:${minutes}`
}
