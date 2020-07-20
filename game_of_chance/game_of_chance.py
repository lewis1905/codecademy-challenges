import random

money = 100

#Game functions are written below:

#function produces randomly number 1 or 2 (heads or tails), and the user has to guess the outcome.
def flipCoin(guess, bet):

  if bet > money:
    print('You dont have enough money!')

  if bet < 0:
    print('Please place a higher bet!')

  flip = random.randint(1, 2)

  if flip == 1:
    print('The result was heads')

  if flip == 2:
    print('The result was tails')

  if flip == 1 and guess == 'heads':
    print('You guessed heads and was correct, you have won £' + str(bet))
    return +bet

  elif flip == 2 and guess == 'tails':
    print('You guessed tails and was correct, you have won £' + str(bet))
    return +bet

  else:
    print('Bad luck you were wrong, you have lost £' + str(bet))
    return -bet



#function randomly produces two numbers and adds them together. The user then has to guess wether the addition is odd or even.
def choHan(guess, bet):

  if bet > money:
    print('You dont have enough money!')

  if bet < 0:
    print('Please place a higher bet!')

  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  result = dice1 + dice2

  if result %2 == 0:
    print('The result was even')

  if result %2 != 0:
    print('The result was odd')

  if result %2 == 0 and guess == 'even':
    print('You guessed even and was correct, you have won £' + str(bet))
    return +bet

  elif result %2 != 00 and guess == 'odd':
    print('You guessed odd and was correct, you have won £' + str(bet))
    return +bet
  
  else:
    print('Bad luck you were wrong, you have lost £' + str(bet))
    return -bet


#Function first makes a list of numbers to simulate a pack of cards. Then two cards will be picked and removed from the list. Whoever draws the highest number will win.
def cardDeck(bet):

  if bet > money:
    print('You dont have enough money!')

  if bet < 0:
    print('Please place a higher bet!')

  available_cards = list(range(1,14))*4

  card1 = available_cards[random.randint(0,len(available_cards)-1)]
  print("Player's card is "+str(card1))
  available_cards.remove(card1)

  card2 = available_cards[random.randint(0,len(available_cards)-1)]
  print("Opponents card is "+str(card2))
  available_cards.remove(card2)

  if card1 > card2:
    print("Player wins £"+str(bet)+" with "+str(card1)+" vs "+str(card2))
    return +bet

  if card1 < card2:
    print("Opponent wins £"+str(bet)+" with "+str(card1)+" vs "+str(card2))
    return -bet

  else:
    print("It is a draw!")
    return 0


#Function first sets up an array of the black numbers and picks a random number from 0 - 36. Next it checks if the spin was even or odd. Then it checks if the guess was the excat number spun. And finally checks wether the guess was the colour red or black.
def roulette(guess, bet):

  if bet > money:
    print('You dont have enough money!')

  if bet < 0:
    print('Please place a higher bet!')
  
  black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
  spin = random.randint(0, 36)
  print('The number was '+str(spin)+'!')
  
  if spin %2 == 0 and guess == 'even':
    print('You guessed even and was correct, you have won £' + str(bet))
    return +bet

  elif spin %2 != 00 and guess == 'odd':
    print('You guessed odd and was correct, you have won £' + str(bet))
    return +bet

  elif guess == spin:
    print('You guessed the number correct, AMAZING!! You have won £' + str(bet * 35) + '!!')
    return +(bet*35)

  elif guess == 'black' and spin in black:
    print('You guessed black and was correct, you have won £' + str(bet))
    return +bet

  elif guess == 'red' and spin not in black:
    print('You guessed red and was correct, you have won £' + str(bet))
    return +bet
  
  else:
    print('Bad luck you were wrong, you have lost £' + str(bet))
    return -bet



#calling all the functions and updating the money the user has left.
if money > 0:
    money += flipCoin("heads", 24)
    print('You have £' + str(money) + ' left!')
else:
    print('You are broke, bad luck!')

if money > 0:
    money += choHan("Odd", 25)
    print('You have £' + str(money) + ' left!')
else:
    print('You are broke, bad luck!')

if money > 0:
    money += cardDeck(5)
    print('You have £' + str(money) + ' left!')
else:
    print('You are broke, bad luck!')

if money > 0:
   money += roulette(17, 8)
else:
    print('You are broke, bad luck!')

print('You finished your session with £' +str(money)+' left!')