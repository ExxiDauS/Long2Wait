const timeDisplay = document.querySelector("#timedisplay")

let startTime = 90;
let elapsedTime = 0;
let currentTime = 0;
let intervalId;
let hrs = 0;
let mins = 0;
let secs = 0;

function updateTime(){
    elapsedTime = Date.now() - startTime;
    intervalId = setInterval(updateTime, 75);

    secs = Math.floor(elapsedTime / 1000 % 60);
    mins = Math.floor((elapsedTime / (1000 * 60)) % 60);
    hrs = Math.floor((elapsedTime / (1000 * 60 * 60)) % 60);

    timeDisplay.textContent = `${hrs}:${mins}:${secs}` ;

    function pad(unit){
        return (('0' + unit)).length > 2 ? unit : "0" + unit;
    }
}