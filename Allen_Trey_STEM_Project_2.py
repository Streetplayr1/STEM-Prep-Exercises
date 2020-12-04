#author: Trey Allen
#STEM Prep Project, Exercises 1

## START OF 2-1 ##

#we will need the random package again
import random

#we need to define where the flea can nextMove, chosen at random from the elements
directions = ['N', 'E', 'S', 'W']

#the start location will be [5, 5]
currentPositionX = 5
currentPositionY = 5

#we will log the current position of the flea after each iteration of the loop
currentPosition = []

#this is the list that contains the nextMove number, the direction, and the new current position
combined_information = []

#we will need to initialize the counters, starting at 0
moveCounter = 0
upCounter = 0
downCoutner = 0
leftCounter = 0
rightCounter = 0

#we can print the start location for our own records
print("Starting location:", [currentPositionX, currentPositionY])

#we want 100 moves, let's create a for loop. Inside each iteration will be the tracking information of the flea's movement
for i in range (1 ,101):
  
  #we will increase which "turn" the flea is on at the start of each iteration
  moveCounter += 1

  #the next nextMove the flea makes will be decided at random from our directions list
  nextMove = random.choice(directions)

  #now we check what the nextMove was...
  if nextMove == 'N':
    #If we nextMove north, only the y-cordinate will change
    currentPositionY += 1
    #this also implies we have moved "up," we can increase this counter too.
    upCounter += 1
  
  #we will repeat the process with the other conditions, same process, different outcomes.
  elif nextMove == 'W':
    currentPositionX -= 1
    leftCounter += 1

  elif nextMove == 'S':
    currentPositionY -= 1
    downCoutner += 1

  #we don't have to specify "E" here because it is assumed, it's the only other element left.
  else: 
    currentPositionX += 1
    rightCounter += 1

  #we will need to update every time
  currentPosition.append([currentPositionX, currentPositionX])

  #and at last, we create our nested list
  combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]

  #and let us print out the information we have
  print(combined_information[0], combined_information[1], combined_information[2])

#all information
print("The flea moved up", upCounter, "times.\n" + "The flea moved down", downCoutner, "times.\n" + "The flea moved left", leftCounter, "times.\n" + "The flea moved right", rightCounter, "times.")

## END OF 2-1 ##

print("\nEND OF GAME 1\n")

## START OF 2-2 ##

#we will redefine our directions list
directions = ['N','NE','E','SE','S','SW','W','NW']

#the start location will be [5, 5]
currentPositionX = 5
currentPositionY = 5

#basically, a total reset: just adding new features later in the code.
currentPosition = []
combined_information = []

moveCounter = 0
upCounter = 0
downCounter = 0
leftCounter = 0
rightCounter = 0

print("Starting location: ", [currentPositionX, currentPositionY])

#we will repeat the moves and loops from above, just adjusting to the new directions added to the list
for i in range(1,101):

  moveCounter += 1
  nextMove = random.choice(directions)

  if nextMove == 'N':
    currentPositionY += 1
    upCounter += 1

  elif nextMove == 'NW':
    currentPositionY += 1
    currentPositionX -= 1
    upCounter += 1
    leftCounter += 1

  elif nextMove == 'W':
    currentPositionX -= 1
    leftCounter += 1

  elif nextMove == 'SW':
    currentPositionX -= 1    
    currentPositionY -= 1
    downCounter += 1
    leftCounter += 1

  elif nextMove == 'S':
    currentPositionY -= 1
    downCounter += 1

  elif nextMove == 'SE':
    currentPositionY -= 1
    currentPositionX += 1
    downCounter += 1
    rightCounter += 1

  elif nextMove == 'E':
    currentPositionX += 1
    rightCounter += 1

  else:
    currentPositionX += 1
    currentPositionY += 1
    upCounter += 1
    rightCounter += 1
  
  currentPosition.append([currentPositionX, currentPositionY])
  combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]

  print(combined_information[0], combined_information[1], combined_information[2])

#the counts will be a little different (higher), as some moves may increase two counters at once
#sorry for the lack of notes, assignment was self-explanatory apart from additional moves
print("The flea moved up", upCounter, "times.\n" + "The flea moved down", downCounter, "times.\n" + "The flea moved left", leftCounter, "times.\n" + "The flea moved right", rightCounter, "times.")

## END OF 2-2 ##

print("\nEND OF GAME 2\n")

## START OF 2-3 ##

#RESET -- code will look the same for a bit until we enforce the new rules and calculate new numbers.
directions = ['N','NE','E','SE','S','SW','W','NW']

currentPositionX = 5
currentPositionY = 5

currentPosition = []
combined_information = []

moveCounter = 0
upCounter = 0
downCounter = 0
leftCounter = 0
rightCounter = 0

#we are introducing new counters, as per the PDF
illegalMoveCounter = 0
numberOfTimesYWas5 = 0

print("Starting location: ", [currentPositionX, currentPositionY])

for i in range(1,101):

  moveCounter += 1
  nextMove = random.choice(directions)

  if nextMove == 'N':
    #the number can't go negative if we are increasing the value, so no need to have a check here.
    currentPositionY += 1
    upCounter += 1

    currentPosition.append([currentPositionX, currentPositionY])
    combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]

    #because we have extra checks in this loop, we will print after each "if" statement rather than at the end of the loop
    #this is so we don't duplicate any prints if it turns out the flea moved out of quadrant one
    print(combined_information[0], combined_information[1], combined_information[2])

  elif nextMove == 'NW':
    #we know that moving Northwest will ONLY decrease the X Position, so we will only check if that goes negative
    #no need to check if Y goes negative as this move results in +1 for the Y cordinate
    #we will check currentPositionX-1 because -1 implies the move has been made, but we don't want to move yet
    if (currentPositionX - 1 < 0):
      #if the "if" statement turns out to be true, we will warn the player
      print(moveCounter, "The flea tried to move off of the plane. Turn skipped!")

      #this is an illegal move, we shall increase the new counter introduced
      illegalMoveCounter += 1

      #there were no moves made, no counters increase.

      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])

    #we can move the flea like normal if the previous condition fails, also adjusting the counters as needed
    #we will once again have to print the information, just in case the previous condition never runs
    else:
      currentPositionY += 1
      currentPositionX -= 1

      upCounter += 1
      leftCounter += 1

      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])

  #this process will continue throughout the rest of the program
  #we will CHECK a new condition, (move-1), and execute a turn skip if we go negative (with no moves)
  #otherwise, we execute like normal in the first two programs
  #where the flea moves and the counters increase

  elif nextMove == 'W':
    if (currentPositionX - 1 < 0):
      print(moveCounter, "The flea tried to move off of the plane. Turn skipped!")

      illegalMoveCounter += 1

      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])

    else:
      currentPositionX -= 1

      leftCounter += 1

      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])

  elif nextMove == 'SW':
    #we will treat this one a little differently
    #since both positions will decrease by one, we will just need to check if AT LEAST one of them goes negative (or statement)
    #if either or go negative,  we will not move -> in any other case, it is safe to move
    if (currentPositionX - 1 < 0) or (currentPositionY - 1 < 0):
      print(moveCounter,"The flea tried to move off of the plane. Turn skipped!")

      illegalMoveCounter += 1
      
      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])

    else:
      currentPositionX -= 1    
      currentPositionY -= 1

      leftCounter += 1
      downCounter += 1

      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])

  elif nextMove == 'S':
    if (currentPositionY - 1 < 0):
      print(moveCounter,"The flea tried to move off of the plane. Turn skipped!")

      illegalMoveCounter += 1
      
      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])
  
    else:
      currentPositionY -= 1

      downCounter += 1

      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])

  elif nextMove == 'SE':
    if (currentPositionY - 1 < 0):
      print(moveCounter,"The flea tried to move off of the plane. Turn skipped!")

      illegalMoveCounter += 1
      
      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])
    
    else:
      currentPositionY -= 1
      currentPositionX += 1

      downCounter += 1
      rightCounter += 1

      currentPosition.append([currentPositionX, currentPositionY])
      combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
      print(combined_information[0], combined_information[1], combined_information[2])

  elif nextMove == 'E':
    currentPositionX += 1
    
    rightCounter += 1

    currentPosition.append([currentPositionX, currentPositionY])
    combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
    print(combined_information[0], combined_information[1], combined_information[2])

  #"else" in this case can imply a NE move because this is the only element left in the list
  #in other words, any other case => NE
  else:
    currentPositionX+=1
    currentPositionY+=1

    upCounter += 1
    rightCounter += 1

    currentPosition.append([currentPositionX, currentPositionY])
    combined_information = [moveCounter, nextMove, [currentPositionX, currentPositionY]]
    print(combined_information[0], combined_information[1], combined_information[2])

  #we want to print out the # of times the "Y" position is 5, so we can just check *when* this is true
  #if it's true, add 1
  if currentPositionY == 5:
    numberOfTimesYWas5 += 1

#now we print everything
print("The flea moved up", upCounter, "times.\n" + "The flea moved down", downCounter, "times.\n" + "The flea moved left",leftCounter, "times.\n" + "The flea moved right", rightCounter, "times.")

print("The flea had a y-coordinate of '5'", numberOfTimesYWas5, "times.")

print("The flea attempted to move off of the plane", illegalMoveCounter, "times.")

## END OF 2-3 ##