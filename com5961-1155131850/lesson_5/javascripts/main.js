// console.log("Hello world from Javascipt");
// developers use this to debug the webpage => console.log()
// alert("Hello and welcome to my page!");

function revealMessage(){
    document.getElementById("hiddenMessage").style.display = 'block';
}

function countDown(){
    var currentVal = document.getElementById("countDownButton").innerHTML;
    // var newVal = currentVal - 1;
    var newVal = 0;
    if (currentVal > 0) {
        newVal = currentVal - 1;
    }
    document.getElementById("countDownButton").innerHTML = newVal;
}