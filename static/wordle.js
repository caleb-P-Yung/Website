let randomWord;
async function getword(){
          

try
{const res = await fetch("/api/wordle");
const data = await res.json();
 randomWord = data.message;
    }
catch(e)
{console.log("error fetching wordle word: "+e)}
}

let remainingGuesses = 6;
let remainingHints = 4;
let hintIndex = 0;
const guesses = [];
const hints = [];
let correctA = Number(localStorage.getItem("correct")) || 0;
let incorrectA = Number(localStorage.getItem("incorrect")) || 0;

// Display elements
const hintDiv = document.querySelector(".hint");
const resultDiv = document.querySelector(".result");
const guessesLeftDiv = document.querySelector(".guesses-left");
const wordInput = document.getElementById("wordInput");
const submitWordButton = document.getElementById("submitWord");
const hintButton = document.getElementById("hint");
const giveUpButton = document.getElementById("giveUp");
const guessLog = document.getElementById("guessHistory");
const hintLog = document.getElementById("hintLog");
let score = document.getElementById("score");
score.innerText = `${incorrectA}/${correctA}`;
submitWordButton.disabled = true;

async function initWordle() {
  await getword(); // wait for API
  submitWordButton.disabled = false;
}

initWordle();
// Utility to compare words
function compareWords(input, target) {
  if (target != null){
  const result = [];
  for (let i = 0; i < input.length; i++) {
    if (target[i] === input[i]) {
      result.push(`${input[i]} *`);
    } else if (target.includes(input[i])) {
      result.push(`${input[i]} ^`);
    } else {
      result.push(`${input[i]} x`);
    }
  }
  return result.join(" ");
}else{alert("word not loaded yet, try again in a moment")}
}

// Update logs
function updateLogs() {
  guessLog.innerHTML = guesses.map(g => `<li>${g}</li>`).join("");
  hintLog.innerHTML = hints.map(h => `<li>${h}</li>`).join("");
}

// Hint logic
function giveHint() {
  if (remainingHints > 0) {
    let hint = "";
    switch (hintIndex) {
      case 0:
        hint = `The word is ${randomWord.length} letters long.`;
        break;
      case 1:
        hint = `The word begins with "${randomWord[0]}".`;
        break;
      case 2:
        hint = `The word ends with "${randomWord[randomWord.length - 1]}".`;
        break;
      case 3:
        hint = `The first two letters are "${randomWord[0]}" and "${randomWord[1]}".`;
        break;
    }
    hintIndex++;
    remainingHints--;
    hints.push(hint);
    updateLogs();
    hintDiv.innerText = hint;
    guessesLeftDiv.innerText = `You have ${remainingGuesses} guesses left.`;
  } else {
    hintButton.disabled = true;
  }
}

// Event handlers
submitWordButton.addEventListener("click", async() => {
  const input = wordInput.value.toLowerCase();
  if (!input) return;

  if (input === randomWord) {
    resultDiv.innerText = "You guessed the word! 🎉";
    correctA++;
    incorrectA++
    localStorage.setItem("correct", correctA);
    localStorage.setItem("incorrect", incorrectA);
    guesses.push(`Correct Guess: ${input}`);
    updateLogs();
    submitWordButton.disabled = true;
    hintButton.disabled = true;
    giveUpButton.disabled = true;
  } else if (remainingGuesses > 0) {
    const feedback = compareWords(input, randomWord);
    resultDiv.innerText = feedback;
    guesses.push(`Guess: ${input} - ${feedback}`);
    remainingGuesses--;
    updateLogs();
    guessesLeftDiv.innerText = `You have ${remainingGuesses} guesses left.`;
    
    // Decrease incorrectA on each wrong guess
    localStorage.setItem("incorrect", incorrectA);
    
    if (remainingGuesses === 0) {
      resultDiv.innerText += `\nGame Over! The word was "${randomWord}".`;
    }
  } else {
    resultDiv.innerText = `No guesses left! The word was "${randomWord}".`;
    incorrectA--;
    localStorage.setItem("incorrect", incorrectA);
  }
  wordInput.value = ""; // Clear input field
  score.innerText = `${incorrectA}/${correctA}`; // Update score display
});

hintButton.addEventListener("click", giveHint);

giveUpButton.addEventListener("click", () => {
  resultDiv.innerText = `You gave up! The word was "${randomWord}".`;
  guesses.push("Game ended - Player gave up.");
  updateLogs();
  submitWordButton.disabled = true;
  hintButton.disabled = true;
});