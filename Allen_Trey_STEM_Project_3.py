#author: Trey Allen
#STEM Prep Project, Exercises 3

## START OF 3-1 ##

#the good ol' reliable
import random

#we will initialize variables, as per usual for keeping track of numbers
#first, our list(s), noting that activity (1) does not change
#we will need a list to keep track of the state, and a list of lists with the rest of the information
stateTracker = [[0, 1]]
animal = []

#next, our gut level, activity level, the timestep, and the prob. of success
timeStep = 0
gutLevel = 0
activityLevel = 1
probabilityOfSuccess = 0.5

#we need a for loop that runs 100 times
for i in range(1,101):
  #we need a random number to test against our probability of success (b) value, let's call this "number"
  number = random.random()

  #as the PDF requests, check if this randomly generated number is <= our probability of success, then ...
  if number <= probabilityOfSuccess:
    #increase our gut level (h)
    gutLevel += 1

  #we need to keep track of the time step as well, so we can increase this after every loop
  timeStep += 1

  #add the results to the list
  stateTracker.append([gutLevel, activityLevel])

  #combined list
  instance = [timeStep, number, stateTracker[i]]
  animal.append(instance)

print(animal)

## END OF 3-1 ##

print("\nEND OF FIRST MODEL\n")

## START OF 3-2 ##

#we will intialize lists and constants as we did in the previous exercise
stateTracker = [[0,1]]
animal = []

timeStep = 0
gutLevel = 0
activityLevel = 1
probabilityOfSuccessfulFeed = 0.5
probablityOfSuccessfulRest = 0.5

huntingCounter = 0 
restingCounter = 0
feedToRest = 0
restToFeed = 0

for i in range(1,101):
  #we are going to increase which step we are on for every loop
  timeStep += 1

  s = random.random()
  m = random.random()

  if activityLevel == 0: #resting
    if s <= probablityOfSuccessfulRest: #successful rest
      gutLevel -= 1 #gets hungrier
      activityLevel = 0 
    
  else: #hunting
    if m <= probabilityOfSuccessfulFeed: #successful feed
      gutLevel += 1 #gets fuller
      activityLevel = 1

  if gutLevel == 5:
    activityLevel = 0

  if gutLevel == 0:
    activityLevel = 1

  stateTracker.append([gutLevel, activityLevel])
  instance = [timeStep, s, stateTracker[i]]
  print(instance)
  animal.append(instance)

print("\nEND OF FIRST 100\n")

stateTracker = [[0,1]]
animal = []

timeStep = 0
gutLevel = 0
activityLevel = 1
probabilityOfSuccessfulFeed = 0.5
probablityOfSuccessfulRest = 0.5

huntingCounter = 0 
restingCounter = 0
feedToRest = 0
restToFeed = 0


for i in range(1,1001):
  #we are going to increase which step we are on for every loop
  timeStep += 1

  s = random.random()
  m = random.random()

  if activityLevel == 0: #resting
    restingCounter += 1
    if s <= probablityOfSuccessfulRest: #successful rest
      gutLevel -= 1 #gets hungrier
      activityLevel = 0 

  else: #hunting
    huntingCounter += 1
    if m <= probabilityOfSuccessfulFeed: #successful feed
      gutLevel += 1 #gets fuller
      activityLevel = 1

  if gutLevel == 5:
    feedToRest += 1
    activityLevel = 0

  if gutLevel == 0:
    restToFeed += 1
    activityLevel = 1

  stateTracker.append([gutLevel, activityLevel])
  instance = [timeStep, s, stateTracker[i]]

  print(instance)
  animal.append(instance)

#print(animal) --- print this if needs to be list of lists; otherwise, just use line36

print("The animal rested", restingCounter, "times.")
print("The animal hunted", huntingCounter, "times.")
print("The animal stopped feeding and started resting", feedToRest, "times.")
print("The animal stopped resting and started feeding", restToFeed, "times.")

## END OF 3-2 ##