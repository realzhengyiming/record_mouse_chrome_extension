

$(document).ready(function(){  //打开页面执行

    console.log("hello i am extension, I have jquery! ");



});

var press = false;
var log_list = new Array();
// The mousedown event is fired when a pointing device button (usually a mouse button) is pressed on an element.
document.addEventListener('mousedown', function(e) {
    press = true;

});

// The mouseup event is fired when a pointing device button (usually a mouse button) is released over an element.
document.addEventListener('mouseup', function(e) {
    press = false;
    ;});

// The mousemove event is fired when a pointing device (usually a mouse) is moved while over an element.
document.addEventListener('mousemove', function(e) {
    if (!press) return;

    var timestamp=new Date().getTime();

    chrome.storage.local.set({x: e.clientX, y: e.clientY}, function(items) {
            console.log('--> move x: ' + e.clientX + ', y: ' + e.clientY + ', timestamp: '+ timestamp);

    })
    ;});


