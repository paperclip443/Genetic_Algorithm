# Run in PyCharm
import random
from math import *

def fitness_score(population_array, city_list):
   # city_list = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
   #              "San Diego", "Dallas", "San Jose", "Austin", "Charlotte", "Denver", "Seattle", "Portland",a
   #              "Miami", "Atlanta"]
   # NY to LA, to Chicago.... LA to Chicago, to Houston..
                   # NY     LA    Chi   Hous  Phoe  Phi   SAnt  SDi   Dal   SJos  Aus   Cha  Den   Sea   Por    Mia   Atl
   distance_list = [[    0, 2806,  813, 1662, 2519,   95, 1821, 2838, 1578, 3032, 1773,  619, 1882, 2956, 2905, 1371,  873], # NY1
                    [ 2806,    0, 2126, 1667,  479, 2758, 1492,  127, 1453,  340, 1492, 2462, 1183, 1135,  961, 2746, 2174], # LA2
                    [  813, 2126,    0, 1074, 1763,  783, 1233, 2065,  959, 2380, 1154,  788, 1002, 2071, 2137, 1347,  717], # Chicago3
                    [ 1662, 1667, 1074,    0, 1204, 1582,  222, 1537,  260, 1888,  192, 1152, 1084, 2278, 2205, 1473,  793], # Houston4
                    [ 2519,  479, 1763, 1204,    0, 2327, 1216,  405, 1048,  735, 1006, 2051,  790, 1507, 1298, 2378, 1846], # Phoenix5
                    [   95, 2758,  783, 1582, 2327,    0, 1774, 2773, 1514, 2967, 1709,  523, 1765, 2859, 2874, 1219,  800], # Philadelphia6
                    [ 1821, 1492, 1233,  222, 1216, 1774,    0, 1386,  274, 1750,   88, 1228,  945, 2253, 2180, 1538, 1015], # San Antonio7
                    [ 2838,  127, 2065, 1537,  405, 2773, 1386,    0, 1350,  466, 1299, 2384, 1078, 1259, 1085, 2671, 2139], # San Diego8
                    [ 1578, 1453,  959,  260, 1048, 1514,  274, 1350,    0, 1710,  195, 1026,  795, 2100, 2026, 1345,  782], # Dallas9
                    [ 3032,  340, 2380, 1888,  735, 2967, 1750,  466, 1710,    0, 1716, 2669, 1273,  838,  664, 3003, 2431], # San Jose10
                    [ 1773, 1492, 1154,  192, 1006, 1709,   88, 1299,  195, 1716,    0, 1186,  915, 2139, 2066, 1460,  905], # Austin11
                    [  619, 2462,  788, 1152, 2051,  523, 1228, 2384, 1026, 2669, 1186,    0, 1598, 2796, 2755,  786,  245], # Charlotte12
                    [ 1882, 1183, 1002, 1084,  790, 1765,  945, 1078,  795, 1273,  915, 1598,    0, 1363, 1258, 2091, 1430], # Denver13
                    [ 2956, 1135, 2071, 2278, 1507, 2859, 2253, 1259, 2100,  838, 2139, 2796, 1363,    0,  174, 3297, 2635], # Seattle14
                    [ 2905,  961, 2137, 2205, 1298, 2874, 2180, 1085, 2026,  664, 2066, 2755, 1258,  174,    0, 3256, 2594], # Portland15
                    [ 1371, 2746, 1347, 1473, 2378, 1219, 1538, 2671, 1345, 3003, 1460,  786, 2091, 3297, 3256,    0,  730], # Miami16
                    [  873, 2174,  717,  793, 1846,  800, 1015, 2139,  782, 2431,  905,  245, 1430, 2635, 2594,  730,    0]  #Atlanta17
                    ]

   a = -1
   b = -1
   c = -1
   d = -1
   fitness_array = []

   for i in range(len(population_array)):
       total = 0
       for j in range(len(population_array[i])): #0, 1,2 ,3 ,4
           if j + 1 < len(population_array[i]):

               #This gets coordinates for above array
               for x in range(len(city_list)):
                   if population_array[i][j] == city_list[x]:
                       a = x
                   if population_array[i][j+1] == city_list[x]:
                       b = x
                   #End city
                   if population_array[i][len(population_array[i])-1] == city_list[x]:
                       c = x
                   #Start City
                   if population_array[i][0] == city_list[x]:
                       d = x
               #print("Should Have Four of These: ", distance_list[a][b])
               total = total + distance_list[a][b]
               #print("The Four total is: ", total)
       #print("End to Start: ", distance_list[c][d])
       total = total + distance_list[c][d]
       #print("The final total should be: ", total)
       fitness_array.append(total)
   return fitness_array

def crossover (population_array, crossover_chance):
   #pop array sorted so shortest paths are in start of array
   crossover_array = []
   child_array = []
   weighted_array = []
   x = random.randint(0, 100)
   if crossover_chance == 0:
       return population_array
   if x > crossover_chance: #No crossover
       return population_array
   else:
       while len(crossover_array) < len(population_array):
           #CREATE WEIGHTED LIST TO DRAW FROM
           weighted_array.clear()
           i = len(population_array) #number of cities
           x = 0
           #from 0 up to i-1
           while x < len(population_array) : # X goes from 0 to 4
               temporary = [population_array[x]] * i
               weighted_array = weighted_array + temporary
               x += 1
               i -=1
           random.shuffle(weighted_array)

           #Trouble
           draw1 = random.randint(0, len(weighted_array)-1) #Integer
           draw2 = random.randint(0, len(weighted_array)-1) #Integer
           while draw1 == draw2:
               draw2 = random.randint(0, len(weighted_array) - 1)
           parent1 = weighted_array[draw2]
           parent2 = weighted_array[draw1]



           #Random length from random position in parent 1 put in same spot in new array
           #Start with Parent1------------------------------------
           child_array = [None] * len(population_array[0])
           length_segment = random.randint(1, (len(child_array) - 1)) #if len is 5, 5-1=4//Ex segment is 3
           #L4 in 5 cities: goes 0 or 1 //L3 in a 5: goes 0,1,or 2//L2 in a 5 goes 0,1,2,3//L1 goes 01234
           up_to = len(child_array) - length_segment #5 - 3 = 2
           starting_positon = random.randint(0, up_to) #rand from 0 to 2
           #from parent 1, grab starting positon and next length segment
           for y in range(length_segment):
               child_array[starting_positon+y] = parent1[starting_positon+y]


           #PUT PARENT 2 INTO CHILD---------------------------------------------------------------------
           short_parent2 = [x for x in parent2 if x not in child_array]
           #print("New parent2 is:", short_parent2)
           none_positions = []
           for i in range(len(child_array)):
               if child_array[i] == None:
                   none_positions.append(i)
           random.shuffle(none_positions)

           for i in range(len(none_positions)):
               child_array[none_positions[i]] = short_parent2[i]
           #print("This is the Final Child", child_array)
           crossover_array.append(child_array)
       return crossover_array

def mutation (population_array, mutation_rate):
   if mutation_rate == 0:
       return population_array
   #   Each city has a X% chance of being swapped with another random city that's not itself
   for i in range(len(population_array)):
       x = random.randint(0,100)
       if x < mutation_rate:
           y = random.randint(0, len(population_array[i]) - 1)
           j = random.randint(0, len(population_array[i]) - 1)
           while y == j:
               j = random.randint(0, len(population_array[i]) - 1)
           population_array[i][j], population_array[i][y] = population_array[i][y], population_array[i][j]
   return population_array

# MAIN STARTS HERE---------------------------------------------------------------------------------------
city_list = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
           "San Diego", "Dallas", "San Jose", "Austin", "Charlotte", "Denver", "Seattle", "Portland",
           "Miami", "Atlanta"]
           
#Input number of cities
x = 0
while x == 0:
   try:
       num_cities = input("Enter Number of Cities: ")
       num_cities = int(num_cities)
       if num_cities >17 or num_cities < 4:
           print("Number of cities has to be between 4 and 17.")
       else:
           x = 1
   except ValueError:
       print("This is not an interger.")

# Input Populaton Size
x = 0
while x == 0:
   try:
       chosen_population = input("Enter Population Size: ")
       chosen_population = int(chosen_population)
       if chosen_population < 5 or chosen_population >100:
           print("Population needs to be between 5 and 100.")
       else:
           x = 1
   except:
       print("This is not an interger.")

# Input Crossover Chance
x = 0
while x == 0:
   try:
       crossover_chance = input("Enter Crossover Chance: ")
       crossover_chance = float(crossover_chance)
       if crossover_chance < 0 or crossover_chance >100:
           print("Crossover chance needs to be between 0 and 100.")
       else:
           x = 1
   except:
       print("This is not a number.")

# Input Mutation Chance
x = 0
while x == 0:
   try:
       mutation_rate = input("Enter Mutation Chance: ")
       mutation_rate = float(mutation_rate)
       if mutation_rate < 0 or mutation_rate >100:
           print("Mutation Rate needs to be between 0 and 100.")
       else:
           x = 1
   except:
       print("This is not a number.")

#Target Goal
x = 0
while x == 0:
   try:
       target_goal = input("Same best score for how many generations: ")
       target_goal = int(target_goal)
       if target_goal < 0 or target_goal >100000:
           print("Best score needs to be between 0 and 100,000.")
       else:
           x = 1
   except:
       print("This is not a number.")

#----------------------------------------------------------------------------------------------------
#GENERATION ZERO
#Random city has to be assigned a random spot in the array
#2D array with inner array lenght of num_cities and total arrays equal to population
population_array = []
chromosome = [None] * num_cities #Length of chromosome is now 5 of "None"
temp_city_list = city_list[0:num_cities]
pop_length = 0

while pop_length < chosen_population:
   # Random positon in array (0,5) is from 0 to 5, thus num_cities - 1
   rand_pos = random.randint(0,num_cities - 1)
   # Random city from City1 to CityX
   rand_city = temp_city_list[random.randint(0,len(temp_city_list)-1)]
   #Check that space is open and city is not repeated
   #Using temp list will remove cities that are already used
   if chromosome[rand_pos] == None:
       chromosome[rand_pos] = rand_city
       temp_city_list.remove(rand_city)
   if len(temp_city_list) == 0:
       population_array.insert(pop_length, chromosome)
       pop_length += 1
       #Reset chromosome and temp city list
       chromosome = [None] * num_cities
       temp_city_list = city_list[0:num_cities]
pop_length = 0

#------------------------------------------------------------------------------------------
shortest_distance = 9999999
best_route = []
generation_number = 0
best_generation_number=0
best_score_counter = 0
#while loop// one counter for total number of generations//one to say when algorythm is done
   #ie shortest distance doesn't change for 1k generations, 2k generations, 50k generations
while best_score_counter < target_goal:
   if generation_number % 1000 == 0:
       print("Generation: ", generation_number)
   #------------------------------------------------------------------------------------------------------
   #DETERMINE FITNESS - each separate path in total miles
   score = fitness_score(population_array, city_list)
   #print("This is the score: ", score)
   #--------------------------------------------------------------------------
   #SORT FITNESS ARRAY
   sort_score = score.copy()
   sort_score.sort() #Represents shortest to longest path
   placement = []
   #put pop array in same order as sorted score
   for i in range(len(sort_score)):
       for j in range(len(sort_score)):
           if score[i] == sort_score[j]  and j not in placement:
               placement.append(j)

   sorted_population_array = [None] * len(population_array)
   for i in range(len(population_array)):
       sorted_population_array[placement[i]] = population_array[i]

   if sort_score[0] < shortest_distance:
       best_score_counter = 0
       shortest_distance = sort_score[0]
       best_generation_number = generation_number
       print("New Shortest Distance in generation:", generation_number," is: ", shortest_distance, "miles.")
       best_route = sorted_population_array[0]
       print("New Best Route is: ", best_route)

   #--------------------------------------------------------------------------------
   #CROSSOVER
   population_array = crossover(sorted_population_array, crossover_chance)
   #-----------------------------------------------------------------------------

   #MUTATION STEP - For TSP problem, swap two cities
   population_array = mutation(population_array, mutation_rate)
   best_score_counter += 1
   generation_number += 1
print("Shortest Distance Found:", shortest_distance, "miles.")
print("Generation Number: ", best_generation_number)
print("Best Route Found: ", best_route)

