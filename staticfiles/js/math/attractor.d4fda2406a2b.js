
//P5 gives error that ellipse needs a real number until I click the canvas, annoying, doesn't change anything. Probably a clever way to fix this, I just muted P5 errors
p5.disableFriendlyErrors = true;

var dots = [0];
var increment = 1;
var currentPos = [0];


//a is a
var a;

//both x and y are temporary vals used in the loop (add them in the loop to lower memory usage)
var x;
var y;


window.onload = function () {
    var button = document.getElementById("reset");
    button.addEventListener("click", reset);
    console.log(currentPos);

}




function setup() {
    //create canvas 400 by 400
    
    var canvas = createCanvas(window.innerWidth/2, window.innerHeight/2);
    
    //black background
    background(0);

    //don't fill the ellipses being drawn
    noStroke();

    //fill ellipses white
    fill(255);

    //the itteration, itteration is 1 in a new window and the input value when window is not loaded
    text("Itterations Per Click: " + increment, 10, 30);

    //canvas fits inside canvas-div id
    canvas.parent('canvas-div');

    //attatch a mouse pressed function only to canvas (so you cant click outside canvas)
    canvas.mousePressed(updatePascal);
    console.log("made it");
}

function reset() {
    //clear dots, draw should clear screen anyway
    dots = [0];
    increment = getInputVal("increment");
    console.log("hi");
    console.log(increment);
    setup();
}



function draw() {
    if (dots.length > 0) {
        for (var i = 0; i < dots.length; i++) {
            ellipse(dots[i].xPos, dots[i].yPos, 2, 2);
        }
    }

}



function pascal() {
    a = random(dots);
    x = (a.xPos - currentPos.xPos) / 2;
    y = (a.yPos - currentPos.yPos) / 2;
    currentPos = {
        xPos: currentPos.xPos + x,
        yPos: currentPos.yPos + y
    }
}
function updatePascal() {
    if (dots.length == 1) {
        var pos = { xPos: mouseX, yPos: mouseY };
        dots.push(pos);
        dots = dots.filter(function (value, index, arr) {
            return value != 0;

        });
    } else if (dots.length < 3) {
        let pos = { xPos: mouseX, yPos: mouseY };
        dots.push(pos);
        dots = dots.filter(function (value, index, arr) {
            return value != 0;
        });
        a = random(dots);
        var filtered = dots.filter(function (value, index, arr) {
            return value != a;
        });
        currentPos = random(filtered);

    } else {
        for (var i = 0; i < increment; i++) {
            pascal();
            ellipse(currentPos.xPos, currentPos.yPos, 2, 2);
        }
    }
}
function getInputVal(id) {
    return document.getElementById(id).value;
}