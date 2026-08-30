// Display the value on the page
//quiz buttosn
const q1 = document.getElementById("q1");
const q2 = document.getElementById("q2");
const q3 = document.getElementById("q3");
const q4 = document.getElementById("q4");
const q5 = document.getElementById("q5");
const q6 = document.getElementById("q6");
const q7 = document.getElementById("q7");
const q8 = document.getElementById("q8");
const q9 = document.getElementById("q9");
const q10 = document.getElementById("q10");
//the quiz scores
let score1 = localStorage.getItem('score1');
let score2 = localStorage.getItem('score2');
let score3 = localStorage.getItem('score3');
let score4 = localStorage.getItem('score4');
let score5 = localStorage.getItem('score5');
let score6 = localStorage.getItem('score6');
let score7 = localStorage.getItem('score7');
let score8 = localStorage.getItem('score8');
let score9 = localStorage.getItem('score9');
let score10 = localStorage.getItem('score10');
//the quiz question number
let scorel1 = localStorage.getItem('scorel1');
let scorel2 = localStorage.getItem('scorel2');
let scorel3 = localStorage.getItem('scorel3');
let scorel4 = localStorage.getItem('scorel4');
let scorel5 = localStorage.getItem('scorel5');
let scorel6 = localStorage.getItem('scorel6');
let scorel7 = localStorage.getItem('scorel7');
let scorel8 = localStorage.getItem('scorel8');
let scorel9 = localStorage.getItem('scorel9');
let scorel10 = localStorage.getItem('scorel10');
//the score output
const numDisplay = document.getElementById("valueoutput");

// Check if the scores from the quizzes are null or undefined, and disable buttons if the scores arn't underfind or null
if (score1 === null || score1 === undefined) {
    score1 = "";  // No score recorded
} else {
    q1.disabled = true; 
    q1.style.cursor = "unset";
}

if (score2 === null || score2 === undefined) {
    score2 = "";
} else {
    q2.disabled = true;
    q2.style.cursor = "unset";
}

if (score3 === null || score3 === undefined) {
    score3 = "";
} else {
    q3.disabled = true;
    q3.style.cursor = "unset";
}

if (score4 === null || score4 === undefined) {
    score4 = "";
} else {
    q4.disabled = true;
    q4.style.cursor = "unset";
}
if (score5 === null || score5 === undefined) {
    score5 = "";
} else {
    q5.disabled = true;
    q5.style.cursor = "unset";
}
if (score6 === null || score6 === undefined) {
    score6 = "";
} else {
    q6.disabled = true;
    q6.style.cursor = "unset";
}
if (score7 === null || score7 === undefined) {
    score7 = "";
} else {
    q7.disabled = true;
    q7.style.cursor = "unset";
}
if (score8 === null || score8 === undefined) {
    score8 = "";
} else {
    q8.disabled = true;
    q8.style.cursor = "unset";
}
if (score9 === null || score9 === undefined) {
    score9 = "";
} else {
    q9.disabled = true;
    q9.style.cursor = "unset";
}
if (score10 === null || score10 === undefined) {
    score10 = "";
} else {
    q9.disabled = true;
    q9.style.cursor = "unset";
}
//cheacking if a quiz's questions don't exist/arn't in local storage is null
if (scorel1 === null) scorel1 = "";
if (scorel2 === null) scorel2 = "";
if (scorel3 === null) scorel3 = "";
if (scorel4 === null) scorel4 = "";
if (scorel5 === null) scorel5 = "";
if (scorel6 === null) scorel6 = "";
if (scorel7 === null) scorel7 = "";
if (scorel8 === null) scorel8 = "";
if (scorel9 === null) scorel9 = "";
if (scorel10 === null) scorel10 = "";
// Calculate and display the score
//adding the score
let score = Number(score1) + Number(score2) + Number(score3) + Number(score4) + Number(score5)+ Number(score6)+ Number(score7)+ Number(score8) + Number(score9) + Number(score10);
//adding the quizzes question number
let questions = Number(scorel1) + Number(scorel2) + Number(scorel3) + Number(scorel4) + Number(scorel5)+ Number(scorel6)+ Number(scorel7)+ Number(scorel8)  + Number(scorel9) + Number(scorel10);
//getting the percentage
let percentage = (score / questions) * 100;

if (!isNaN(percentage)) {
    percentage = percentage.toFixed(2);
    const display = `${score} out of ${questions} \n (${percentage}%)`;
    numDisplay.innerHTML = display;
} else {
    //if there isn't a quiz answered/isn't in local storage
    numDisplay.innerHTML = "No quiz data available.";
}