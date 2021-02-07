setTimeout(1000)
alert("hello world!")
var x = document.getElementsByTagName("text");
console.log(x.length)
for(var i = 0; i < x.length; i++) {
    console.log(x[i].style.fill);
    x[i].style.fill = "rgb(255,255,255)";
}