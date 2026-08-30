let quizData = []; // will be filled in by fetch

const c = document.getElementById("back");
const quizContainer = document.getElementById('quiz');
const resultContainer = document.getElementById('result');
const submitBtn = document.getElementById('submit-btn');
c.style.cursor = "unset";
submitBtn.style.cursor = "pointer";

async function loadQuiz() {
    const response = await fetch('/api/quiz5');
    quizData = await response.json();

    let output = '';
    quizData.forEach((q, index) => {
        output += `<div class="question">
            <p>${q.question}</p>
            <input type="radio" name="q${index}" value="a"> ${q.a}<br>
            <input type="radio" name="q${index}" value="b"> ${q.b}<br>
            <input type="radio" name="q${index}" value="c"> ${q.c}<br>
            <input type="radio" name="q${index}" value="d"> ${q.d}<br>
        </div>`;
    });
    quizContainer.innerHTML = output;
}

function checkAnswers() {
    let score = 0;
    quizData.forEach((q, index) => {
        const answer = document.querySelector(`input[name="q${index}"]:checked`);
        if (answer && answer.value === q.correct) {
            score++;
        }
    });
    resultContainer.innerHTML = `You scored ${score} out of ${quizData.length}`;

    const radios = document.querySelectorAll('input[type="radio"]');
    radios.forEach((radio) => {
        radio.disabled = true;
        radio.style.cursor = "unset";
    });
    localStorage.setItem("score6", score);
    localStorage.setItem("scorel6", quizData.length);

    submitBtn.disabled = true;
    submitBtn.style.cursor = "unset";
    c.disabled = false;
    c.style.cursor = "pointer";
}

window.onload = loadQuiz;