import random
import time

class Character:

  # Attributes of a character
  def __init__(self, name, hp, attack_points, defense_points, special_points):
    self.name = name
    self.hp = hp
    self.attack_points = attack_points
    self.defense_points = defense_points
    self.special_points = special_points

  def attack(self, opponent):
    """
    Creates a method for attacking an opponent.
    Using the random import, character attacking has a chance of missing.
    If character attacking has higher attack points than opponents defense points,
    the difference is subtracted from opponents HP.
    """
    miss = random.randint(0, 6)
    if miss == 0:
      print(f"{self.name}'s attack missed")
      print("-------------------------")
      print("")
      print("")
    elif self.attack_points > opponent.defense_points:
      print("-------------------------")
      print(f"{self.name} attacked {opponent.name}.")
      opponent.hp = opponent.hp + opponent.defense_points - self.attack_points
      print(f"{opponent.name} has {opponent.hp} HP left.")
      print("-------------------------")
      print("")
      print("")

  def special_attack(self, opponent):
    '''
    Creates other method for attacking opponent with
    stronger attack. Has higher chance of missing.
    '''
    miss = random.randint(0, 1)
    if miss == 0:
      print("-------------------------")
      print(f"{self.name}'s special attack missed")
      print("-------------------------")
      print("")
      print("")
    elif self.special_points > opponent.defense_points:
      print("-------------------------")
      print(f"{self.name} attacked {opponent.name} with special.")
      opponent.hp = opponent.hp + opponent.defense_points - self.special_points
      print(f"{opponent.name} has {opponent.hp} HP left.")
      print("-------------------------")
      print("")
      print("")



# Creates a instance of the Character class, hero.
hero = Character("Hero", 80, 22, 14, 38)
# Creates a instance of the Character class, villain.
villain = Character("Villain", 90, 21, 12, 40)


def game():
  '''
  Initiates battle that continues to loop until player
  or computers HP reaches zero.
  Player has option of attacking or using special attack.
  Computer will choose attack by random.
  '''
  print('{} has challenged you to a fight!'.format(villain.name))
  time.sleep(2)

  while villain.hp or hero.hp > 0:
    print("Type an option from the menu: (attack, special)  ")
    menu = input()
    villain_special = random.randint(0, 2)

    if menu == 'attack':
      hero.attack(villain)
    elif menu == 'special':
      hero.special_attack(villain)

    if villain.hp <= 0:
      return f"{villain.name} has been defeated. Congratulations!"

    time.sleep(2)

    if villain_special == 1:
      villain.special_attack(hero)
    else:
      villain.attack(hero)

    if hero.hp <= 0:
      return f"{hero.name} has been defeated. Game over!"
    
game()
