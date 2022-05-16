
var feeding_pics = new Array()

feeding_pics[0] = "static\\img\\mocha_pics\\feeding1.jpeg"
feeding_pics[1] = "static\\img\\mocha_pics\\feeding2.jpg"
feeding_pics[2] = "static\\img\\mocha_pics\\feeding3.jpg"
feeding_pics[3] = "static\\img\\mocha_pics\\feeding4.jpg"
feeding_pics[4] = "static\\img\\mocha_pics\\feeding5.jpg"

var number = Math.round(Math.random() * (feeding_pics.length-1))
function random_feed() {
    document.getElementById('mocha_feed').src = feeding_pics[number];
}

// var j = 0
// var p = theImages.length;
// var preBuffer = new Array()
// for (i = 0; i < p; i++){
//    preBuffer[i] = new Image()
//    preBuffer[i].src = theImages[i]
// }
// var whichImage = Math.round(Math.random()*(p-1));
// function showImage(){
// document.write('<img src="'+theImages[whichImage]+'">');
// }