#creating a class for the pokemon.
class Pokemon:

  def __init__(self, name, level, health, max_health, group, knocked_out = False):
    self.name = name
    self.level = level
    self.health = health
    self.max_health = max_health
    self.group = group
    self.knocked_out = knocked_out

#method for losing health when attacked.
  def lose_health(self, decrease):
    hp_decrease = self.health - decrease
    print("{} health was lost! {} has " + str(self.health) + " points remaining!".format(hp_decrease, self.name))
    return self.health - decrease

#Method for regaining health.
  def regain_health(self, increase):
    hp_increase = self.health + increase
    print("{} health was gained! {} has " + str(self.health) + " points remaining!".format(hp_increase, self.name))
    return self.health + increase

#Method for a pokemon who has lost all health points.
  def knock_out(self):
    if self.knocked_out == True and self.health < 1:
      print("{} has died, choose your next pokemon!".format(self.name))

#Method to revive a pokemon with a potion.
  def revive(self):
    potion = 25
    if self.health < 1:
      print("{} has been revived! You can win this!".format(self.name))
    return self.health + potion

#Method for pokemon when attacking, which gives damage depending on type of pokemon.
  def attack(self, rival):
    damage = 5

    if self.group == "fire" and rival.group == "grass":
      print("{} has dealt double the damage!").format(self.name)
    elif self.group == "water" and rival.group == "fire":
      print("{} has dealt double the damage!").format(self.name)
    elif self.group == "grass" and rival.group == "water":
      print("{} has dealt double the damage!").format(self.name)
    return rival.lose_health(damage * 2)

    if self.group == "fire" and rival.group == "water":
      print("{} has only dealt half the damage!".format(self.name))
    elif self.group == "water" and rival.group == "grass":
      print("{} has only dealt half the damage!".format(self.name))
    elif self.group == "grass" and rival.group == "fire":
      print("{} has only dealt half the damage!".format(self.name))
    return rival.lose_health(damage * 0.5)


#Creating a trainer class.
class Trainer:

  def __init__(self, pokemons, potions, current_pokemon, name, knocked_out = True):
    self.pokemons = []
    self.potions = potions
    self.current_pokemon = current_pokemon
    self.name = name
    self.knocked_out = knocked_out
    if len(self.pokemons) > 6:
      print("a trainer has a limit of 6 pokemon")

#Method for using a potion on the current pokemon with a potion.
  def heal(self):
    print("You have used a potion on {}!".format(self.current_pokemon))
    if self.potions > 0:
     self.current_pokemon.gain_health(15)
     self.potions -= 1
    else:
      print("You're out of potions!")

#Method for the trainer attacking the opponent with both current pokemons.
  def attack(self, rival):
    atk = self.current_pokemon
    defe = rival.current_pokemon
    print("{} attacks {} with {}".format(self.name, rival.name, self.current_pokemon))
    return atk.attack(defe)

#Method for switching pokemon whilst in battle.
  def switch(self):
    if self.current_pokemon == self.knocked_out and self.pokemons > 1:
      print("Your pokemon has been defeated, please choose another!")
    else:
      print("You have sadly lost this battle, dont give up and train harder!")

    
squirtle = Pokemon("squirtle", 4, 99, 99, "water")
charmeleon = Pokemon("charmeleon", 9, 99, 99, "fire")
venusaur = Pokemon("venusaur", 8, 99, 99, "grass")
 
lewis = Trainer([squirtle, charmeleon, venusaur], 5, 3, "Lewis") 
brok = Trainer([charmeleon, venusaur], 2, 2, "Brok")  

