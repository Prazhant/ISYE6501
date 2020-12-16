from pulp import *;
import pandas as pa;
import xlrd as xlrd;

#1.read the excel raw data
foodDataRaw = pa.read_excel("diet.xls")

#2.converting raw data to list
foodData = foodDataRaw[0:64].values.tolist()



#3. Extracting each column of the data and adding to datadictionary
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

#5. Starting the optimization problem which is to minimize cost
problem = LpProblem("Diet_Problem", LpMinimize)

#6. Variable declaration for the amounts of food
amountVars = LpVariable.dicts("Amounts", foods, 0)

#7. objective function
problem += lpSum([cost[i] * amountVars[i] for i in foods]), 'totalCost'

# constraints
problem += lpSum([calories[i] * amountVars[i] for i in foods]) >= minCalories, 'min_cals'
problem += lpSum([calories[i] * amountVars[i] for i in foods]) <= maxCalories, 'max_cals'

problem += lpSum([cholestrol[i] * amountVars[i] for i in foods]) >= minCholestrol, 'min_cholestrol'
problem += lpSum([cholestrol[i] * amountVars[i] for i in foods]) <= maxCholestrol, 'max_cholestrol'

problem += lpSum([totalFats[i] * amountVars[i] for i in foods]) >= minTotalFat, 'min_totalFats'
problem += lpSum([totalFats[i] * amountVars[i] for i in foods]) <= maxTotalFat, 'max_totalFats'

problem += lpSum([sodium[i] * amountVars[i] for i in foods]) >= minSodium, 'min_sodium'
problem += lpSum([sodium[i] * amountVars[i] for i in foods]) <= maxSodium, 'max_sodium'

problem += lpSum([carbohydrates[i] * amountVars[i] for i in foods]) >= minCarbohydrates, 'min_carbohydrates'
problem += lpSum([carbohydrates[i] * amountVars[i] for i in foods]) <= maxCarbohydrates, 'max_carbohydrates'

problem += lpSum([fiber[i] * amountVars[i] for i in foods]) >= minFiber, 'min_fiber'
problem += lpSum([fiber[i] * amountVars[i] for i in foods]) <= maxFiber, 'max_fiber'

problem += lpSum([protein[i] * amountVars[i] for i in foods]) >= minProtien, 'min_protien'
problem += lpSum([protein[i] * amountVars[i] for i in foods]) <= maxProtien, 'max_protien'

problem += lpSum([vitaminA[i] * amountVars[i] for i in foods]) >= minVitaminA, 'min_vitamin_a'
problem += lpSum([vitaminA[i] * amountVars[i] for i in foods]) <= maxVitaminA, 'max_vitamin_a'

problem += lpSum([vitaminC[i] * amountVars[i] for i in foods]) <= maxVitaminC, 'max_vitamin_c'
problem += lpSum([vitaminC[i] * amountVars[i] for i in foods]) >= minVitaminC, 'min_vitamin_c'


problem += lpSum([calcium[i] * amountVars[i] for i in foods]) >= minCalcium, 'min_calcium'
problem += lpSum([calcium[i] * amountVars[i] for i in foods]) <= maxCalcium, 'max_calcium'

problem += lpSum([iron[i] * amountVars[i] for i in foods]) >= minIron, 'min_iron'
problem += lpSum([iron[i] * amountVars[i] for i in foods]) <= maxIron, 'max_iron'

# solve the optimization problem
problem.solve()

varsDictionary = {}

#print the output: food combination to meet the constraints and keep cost down
for v in problem.variables():
    varsDictionary[v.name] = v.varValue
    if(v.varValue>0):
        print(v.name , ": ", v.varValue)


#print the cost
print("Total cost: ",pulp.value(problem.objective))

