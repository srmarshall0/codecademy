# import packages 
from random import randint
from getpass import getpass

# define goalie
class goalie:
  # write constructor 
  def __init__(self, in_name, in_location, in_speed, in_react, in_recognize):
    
    # define locations
    # locations = ["top left", "top right", "bottom left", "bottom right"]
    
    # outline attributes
    self.name = in_name
    self.location = in_location
    self.speed = in_speed
    self.react = in_react
    self.recognize = False

  # define method 1: reaction time 
  def reaction(self, other_player):
    # if react, remove one from speed 
    if (self.react):
      self.location = other_player.location
      self.speed = self.speed - 1
  
  # define method 2: practice
  def practice(self):
    # if practice, add one to speed 
    self.speed = self.speed + 1 
  
  # define method 3:
  def familiar(self, other_player):
    # if familiar, get other players location 
    self.location = other_player.location
  
  # have object describe itself 
  def __repr__(self):
    description = "{player_name} is defending the net tonight".format(player_name = self.name)

    # add information based on decisions 
    if (self.recognize):
      decription += "{player_name} has been up against this shooter before, and may have the competive edge!".format(player_name = self.name)

    # return description 
    return description

# define players 
class player:
  # write constructor
  def __init__(self, in_name, in_location, in_power, in_trick):
    
    # define location options
    # locations = ["top left", "top right", "bottom left", "bottom right"]
    
    # outline attributes
    self.name = in_name
    self.location = in_location
    self.power = in_power 
    self.trick = in_trick

  # define method 1: trick shot 
  def trick_shot(self):
    if (self.trick):
      # if trick shot, randomize location
      self.location = locations[randint(0, 3)]

  # define method 2: practice 
  def practice(self):
    self.power = self.power + 1

  # define method 3: take a shot 
  def take_shot(self, other_player):
    # check if the locations are identical 
    if (self.location == other_player.location):
      # check who gets there first 
      if(self.power > other_player.speed):
        # print score method 
        print("{player_name} scores on {other_name}!".format(player_name = self.name, other_name = other_player.name))
      else:
        print("{other_name} saves the shot from {player_name}".format(other_name = other_player.name, player_name = self.name))
    else:
      print("{player_name} scores on {other_name}!".format(player_name = self.name, other_name = other_player.name))

  # have object describe itself 
  def __repr__(self):
    description = "{player_name} is taking a shot on goal".format(player_name = self.name)

    # add information based on decisions 
    if (self.trick):
      decription += "{player_name} has decided to attempt a trick shot".format(player_name = self.name)

    # return description 
    return description


# begin testing 
# keeper  = goalie("sophie", 1, 2, False, False)
# shooter = player("anna", 1, 2, False)

# i am expecting sophie to save the shot from anna 
# shooter.take_shot(keeper)

# write console interaction 

# get player information 
goalie_name = input("Welcome to Sophie's PK console game! Please decide amongst yourself who would like to defend the net, and who would like to take the shot. If you are going to defend the net, please enter your name and hit enter. \n\nPlayer 1 (goalie) name: ")

shooter_name = input("\nHi " + goalie_name + "! Welcome to the PK shoot-out! Let's see who you'll be up against. If you are taking the shot on goal, enter your name now. \n\nPlayer 2 (shooter) name: ")

# define classes for each player 
shooter_location = input("\nHi " + shooter_name + "! Let's pick how where we'll aim our shot. We have 4 options. \n\n Option 1 = Top Right \n Option 2 = Top Left \n Option 3 = Bottom Right \n Option 4 = Bottom Left \n\nPlease enter the number associated with cour choice here: ")

shooter_power = input("\nGreat choice! How much power would you like to apply to your shot? You can select any number from 1-5 with 5 being the most powerful, and 1 being the least. \n\nPlease type your choice here: ")

shooter_practice = input("\nWould you like to take a practice shot before heading out to the field? If you would type 'True', if you're already game ready type 'False'. \n\nEnter your choice here: ")

shooter_trick = input("\nNow that you've calibrated your shot, there's only one decision left. Would you like to try that trick shot you've been working on? If you think it's ready for a game day debut, type 'True', if it's not ready for the big stage yet, type 'False'. \n\nPlease enter your choice here: ")

print("Please pass the device to " + goalie_name +"!")

# define goalie hcoices 
goalie_location = input("\n\nHi " + goalie_name + "! It's nearly game time. Make your prediction about where Player 1 will shoot the ball. You can select from 4 options. \n\n Option 1 = Top Right \n Option 2 = Top Left \n Option 3 = Bottom Right \n Option 4 = Bottom Left. \n\nPlease enter the number associated with your choice here: ")

goalie_speed = input("\nYou also need to make a prediciton about the speed of Player 1's shot on goal. You can select any number from 1-5 with 5 being the most powerful and 1 being the least. \n\nPlease enter your choice here: ")

goalie_react = input("\nAs the goalie, you can make the choice to commit to your decision above, or wait and react to Player 1's shot. If you want to commit early, type 'False'. If you would like to wait, and react to Player 1 type 'True'. \n\nEnter your choice here: ")

goalie_recognize = input("\nYou've played a lot of games in your career. Does this player look familiar to you? If you've played against Player 1 in a prior match, type 'True', if not type 'False'. \n\nDo you recognize this player? ")
# # keep track of user choices 
# shooter_choices = []
# goalie_choices = []

# create object 
goalie_stats  = goalie(goalie_name, goalie_location, goalie_speed, goalie_react, goalie_recognize)
shooter_stats = player(shooter_name, shooter_location, shooter_power, shooter_trick)

# # have players react to decitiosn 
# shooter_stats.practice()
# shooter_stats.trick_shot()

# print game time message
print("")
print("")
print("")
print("")

print("Time to take the field! Players take your position!")


print("")
print("")
shooter_stats.take_shot(goalie_stats)

# print end-screen message
print("")
print("")
print("Great game all! See you next time!")