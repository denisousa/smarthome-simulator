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