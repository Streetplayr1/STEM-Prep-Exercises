#author: Trey Allen
#STEM Prep Project, Exercises 1

## START OF 4(a) ##

#random package
import random 

#need empty lists (initializers)
dice_results = []
dice_even_or_odd = []
combined_information = []

#roll the die 10 times
for i in range(10):

  #we will assign the "roll" to variable "dice"
  dice = random.randint(1, 6)

  #need to add the roll, "dice," to our results list
  dice_results.append(dice)

  #this "if" statement checks if the roll is even, if so, we add 'e'
  if (dice % 2 == 0):
    dice_even_or_odd.append('e')
  #if not, "else," we add 'o'
  else:
    dice_even_or_odd.append('o')
  
  #creating an entry for each pair of results (nested list, creating a list for each entry)
  combined_information.append([dice_results[i], dice_even_or_odd[i]])

print(dice_results)
print(dice_even_or_odd)
print(combined_information)

#need to extract all letters from combined_information
#the first loop will loop through the entire list, but each element is a list of its own
for i in combined_information:
  print(i)
  #because the list is nested, we will need an additional loop to check for e's and o's in each element
  for x in i:
    if (x == 'e') or (x == 'o'):
      #if we found a letter, good, let's "extract" or print it.
      print(x)

## PRINT STATEMENTS ARE IN PLACE TO ENSURE CODE IS WORKING PROPERLY ##

## END OF 4(a) ##

print('\n===================================================\n')

## START OF 4(b) ##

#we are creating a list, let's initialize
final_list = []

#we will be counting occurrences, let us start from 0 
numberOfEvens = 0
numberOfOdds = 0
numberOfSmalls = 0
numberOfMediums = 0
numberOfBigs = 0

#the list needs to contain 100 elements, let's loop
for i in range(100):
  
  #this is once again a nested list, we can refer to this as the sub list
  sub_list = []

  #let us generate a random number from 1-100
  randomInteger = random.randint(1,100)

  #add this random number to our sub list
  sub_list.append(randomInteger)

  #checking if the number is even and adding 'e' to our sub list
  if randomInteger % 2 == 0:
    sub_list.append('e')
    #we can increase our counter by 1 if we found a number that happened to be even
    numberOfEvens += 1

  #in any other case, the number is odd - add this to the sub list and increase the count.
  else:
    sub_list.append('o')
    #so we will increase our counter of odds
    numberOfOdds += 1

  #these are easy checks, copying the conditions listed from the PDF. (repeating steps above, add to list, and inc. count)
  if randomInteger < 20:
    sub_list.append('Small')
    numberOfSmalls += 1

  #elif implies multiple cases
  #we can ignore the number being >= 20 because this check has been made in the previous "if" statement
  #aka: if the number has failed the previous statement of being less than 20, we can assume it is bigger (only option)
  #therefore, we only need to check if its less than a higher number (59)
  elif randomInteger <= 59:
    sub_list.append('Medium')
    numberOfMediums += 1

  #one last time, it MUST be bigger than 59 if it failed the last two checks
  #the first check determined the number is/is not between 1-19, the second determined 20-59, and now we have the rest, "else"
  else:
    sub_list.append('Big')
    numberOfBigs += 1

  #great, now let us add our sub_lists that we have created to our huge, final list
  final_list.append(sub_list)

print(final_list)
print("e:", numberOfEvens, "\n" + "o:", numberOfOdds, "\n" + "small:", numberOfSmalls, "\n" +"medium:", numberOfMediums, "\n"+ "big:", numberOfBigs)

## END OF 4(b) ##