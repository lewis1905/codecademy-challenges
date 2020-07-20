let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

//generate a random number between 0 and 10.
const generateTarget = () => {
  const randomNumber = Math.floor(Math.random() * 10);
}

//determine which player is closest to the target number.
const compareGuesses = (humanGuess, computerGuesses, target) => {
if (Math.abs(target - humanGuess) < Math.abs(target - computerGuesses)){ 
return true;
  } else if (Math.abs(target - humanGuess) > Math.abs(target - computerGuesses)){
return false;
  } else {
return true;
  }
}

//increase the winner's score after each round.
const updateScore = (winner) => {
  if (winner === 'human'){
  humanScore +=1;
  } else {
  computerScore +=1;
  }
}

//update the round number after each turn.
const advanceRound =() => {
  currentRoundNumber += 1;
}