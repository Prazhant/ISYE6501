#Importing all the libraries needed for the homework
from pulp import *;
import pandas as pa;
import xlrd as xlrd;
import matplotlib.pyplot as plt

#reading xls spreadsheet data
foodDataRaw = pa.read_excel("diet.xls")

#converting the raw data into a list
foodData = foodDataRaw[0:64].values.tolist()

#Extracting each column of the data and adding to datadictionary
foods = {x[0] for x in foodData}
cost = {x[0]: float(x[1]) for x in foodData}
calories = {x[0]: float(x[3]) for x in foodData}
cholestrol = {x[0]: float(x[4]) for x in foodData}
totalFats = {x[0]: float(x[5]) for x in foodData}
sodium = {x[0]: float(x[6]) for x in foodData}
carbohydrates = {x[0]: float(x[7]) for x in foodData}
fiber = {x[0]: float(x[8]) for x in foodData}
protein = {x[0]: float(x[9]) for x in foodData}
vitaminA = {x[0]: float(x[10]) for x in foodData}
vitaminC = {x[0]: float(x[11]) for x in foodData}
calcium = {x[0]: float(x[12]) for x in foodData}
iron = {x[0]: float(x[13]) for x in foodData}

#Extracting min and max values of each nutrient
minCalories = foodDataRaw['Calories'].values[65]
maxCalories = foodDataRaw['Calories'].values[66]

minCholestrol = foodDataRaw['Cholesterol mg'].values[65]
maxCholestrol = foodDataRaw['Cholesterol mg'].values[66]

minTotalFat = foodDataRaw['Total_Fat g'].values[65]
maxTotalFat = foodDataRaw['Total_Fat g'].values[66]

minSodium = foodDataRaw['Sodium mg'].values[65]
maxSodium = foodDataRaw['Sodium mg'].values[66]

minCarbohydrates = foodDataRaw['Carbohydrates g'].values[65]
maxCarbohydrates = foodDataRaw['Carbohydrates g'].values[66]

minFiber = foodDataRaw['Dietary_Fiber g'].values[65]
maxFiber = foodDataRaw['Dietary_Fiber g'].values[66]

maxProtien = foodDataRaw['Protein g'].values[66]
minProtien = foodDataRaw['Protein g'].values[65]

minVitaminA = foodDataRaw['Vit_A IU'].values[65]
maxVitaminA = foodDataRaw['Vit_A IU'].values[66]

minVitaminC = foodDataRaw['Vit_C IU'].values[65]
maxVitaminC = foodDataRaw['Vit_C IU'].values[66]

minCalcium = foodDataRaw['Calcium mg'].values[65]
maxCalcium = foodDataRaw['Calcium mg'].values[66]

minIron = foodDataRaw['Iron mg'].values[65]
maxIron = foodDataRaw['Iron mg'].values[66]

#printing mins and max to cross check the data read
print("mins: ", minCalories, minCholestrol, minTotalFat, minSodium, minCarbohydrates, minFiber, minProtien,
      minVitaminA, minVitaminC, minCalcium, minIron)

print("max:", maxCalories, maxCholestrol, maxTotalFat, maxSodium, maxCarbohydrates, maxFiber, maxProtien,
      maxVitaminA, maxVitaminC, maxCalcium, maxIron)

#Starting the optimization problem which is to minimize cost
problem2a = LpProblem("Diet_Problem", LpMinimize)

#Variable declaration for the amounts of food
amountVars = LpVariable.dicts("Amounts", foods, 0)

# define the variables - binary
chosenFoods = LpVariable.dicts("Chosen", foods, 0, 1, LpBinary)

# objective function
problem2a += lpSum([cost[i] * amountVars[i] for i in foods]), 'totalCost'

# constraints
problem2a += lpSum([calories[i] * amountVars[i] for i in foods]) >= minCalories, 'min_cals'
problem2a += lpSum([calories[i] * amountVars[i] for i in foods]) <= maxCalories, 'max_cals'

problem2a += lpSum([cholestrol[i] * amountVars[i] for i in foods]) >= minCholestrol, 'min_cholestrol'
problem2a += lpSum([cholestrol[i] * amountVars[i] for i in foods]) <= maxCholestrol, 'max_cholestrol'

problem2a += lpSum([totalFats[i] * amountVars[i] for i in foods]) >= minTotalFat, 'min_totalFats'
problem2a += lpSum([totalFats[i] * amountVars[i] for i in foods]) <= maxTotalFat, 'max_totalFats'

problem2a += lpSum([sodium[i] * amountVars[i] for i in foods]) >= minSodium, 'min_sodium'
problem2a += lpSum([sodium[i] * amountVars[i] for i in foods]) <= maxSodium, 'max_sodium'

problem2a += lpSum([carbohydrates[i] * amountVars[i] for i in foods]) >= minCarbohydrates, 'min_carbohydrates'
problem2a += lpSum([carbohydrates[i] * amountVars[i] for i in foods]) <= maxCarbohydrates, 'max_carbohydrates'

problem2a += lpSum([fiber[i] * amountVars[i] for i in foods]) >= minFiber, 'min_fiber'
problem2a += lpSum([fiber[i] * amountVars[i] for i in foods]) <= maxFiber, 'max_fiber'

problem2a += lpSum([protein[i] * amountVars[i] for i in foods]) >= minProtien, 'min_protien'
problem2a += lpSum([protein[i] * amountVars[i] for i in foods]) <= maxProtien, 'max_protien'

problem2a += lpSum([vitaminA[i] * amountVars[i] for i in foods]) >= minVitaminA, 'min_vitamin_a'
problem2a += lpSum([vitaminA[i] * amountVars[i] for i in foods]) <= maxVitaminA, 'max_vitamin_a'

problem2a += lpSum([vitaminC[i] * amountVars[i] for i in foods]) <= maxVitaminC, 'max_vitamin_c'
problem2a += lpSum([vitaminC[i] * amountVars[i] for i in foods]) >= minVitaminC, 'min_vitamin_c'

problem2a += lpSum([calcium[i] * amountVars[i] for i in foods]) >= minCalcium, 'min_calcium'
problem2a += lpSum([calcium[i] * amountVars[i] for i in foods]) <= maxCalcium, 'max_calcium'

problem2a += lpSum([iron[i] * amountVars[i] for i in foods]) >= minIron, 'min_iron'
problem2a += lpSum([iron[i] * amountVars[i] for i in foods]) <= maxIron, 'max_iron'

# new constraints for 2.a
for food in foods:
    problem2a += amountVars[food] >= 0.1 * chosenFoods[food]
    problem2a += amountVars[food] <= 10000 * chosenFoods[food]

# add contraints to include broccoli or celery
problem2a += chosenFoods['Frozen Broccoli'] + chosenFoods['Celery, Raw'] <= 1, 'broccoli or celery'

# add contraints to include atleast 3 protiens
problem2a += chosenFoods['Neweng Clamchwd'] + chosenFoods['Roasted Chicken'] + chosenFoods['Poached Eggs'] + \
  chosenFoods['Scrambled Eggs'] + chosenFoods['Frankfurter, Beef'] + \
  chosenFoods['Kielbasa,Prk'] + chosenFoods['Hamburger W/Toppings'] + \
  chosenFoods['Hotdog, Plain'] + chosenFoods['Pork'] + \
  chosenFoods['Bologna,Turkey'] + chosenFoods['Ham,Sliced,Extralean'] + \
  chosenFoods['White Tuna in Water'] + chosenFoods['2% Lowfat Milk']\
  >= 3, 'three protiens'

# solve the optimization problem
problem2a.solve()

#print the output: food combination to meet the constraints and keep cost down
varsDictionary = {}
for v in problem2a.variables():
    varsDictionary[v.name] = v.varValue
    if (v.varValue > 0):
        if str(v.name).find('Chosen'):
            print(str(v.varValue) + " servings of " + str(v.name))


#print the cost
print("Total cost 2a: ", pulp.value(problem2a.objective))
