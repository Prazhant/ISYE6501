from pulp import *;
import pandas as pa;
import numpy as np;
import xlrd as xlrd;

foodDataRaw = pa.read_excel("diet_large.xls", skiprows = 1, header=0)

foodData = foodDataRaw[0:7146].values.tolist()

# There are lot of blank cells in the spread sheet.
# As mentioned in the office hours, am setting them to zero.
for row in range(1, 7146):
    for column in range(1, 30):
        if np.isnan(foodData[row][column]):
            foodData[row][column] = 0



foods = {x[0] for x in foodData}
protien = {x[0]: float(x[1]) for x in foodData}
carbohydrates = {x[0]: float(x[2]) for x in foodData}
energy = {x[0]: float(x[3]) for x in foodData}
water = {x[0]: float(x[4]) for x in foodData}
energy2 = {x[0]: float(x[5]) for x in foodData}
calcium = {x[0]: float(x[6]) for x in foodData}
iron = {x[0]: float(x[7]) for x in foodData}
magnesium = {x[0]: float(x[8]) for x in foodData}
phosphorous = {x[0]: float(x[9]) for x in foodData}
potassium = {x[0]: float(x[10]) for x in foodData}
sodium = {x[0]: float(x[11]) for x in foodData}
zinc = {x[0]: float(x[12]) for x in foodData}
copper = {x[0]: float(x[13]) for x in foodData}
manganese = {x[0]: float(x[14]) for x in foodData}
selenium = {x[0]: float(x[15]) for x in foodData}
vitaminA = {x[0]: float(x[16]) for x in foodData}
vitaminE = {x[0]: float(x[17]) for x in foodData}
vitaminD = {x[0]: float(x[18]) for x in foodData}
vitaminC = {x[0]: float(x[19]) for x in foodData}
thiamin = {x[0]: float(x[20]) for x in foodData}
riboflavin = {x[0]: float(x[21]) for x in foodData}
niacin = {x[0]: float(x[22]) for x in foodData}
pantothenic = {x[0]: float(x[23]) for x in foodData}
vitaminB = {x[0]: float(x[24]) for x in foodData}
folate = {x[0]: float(x[25]) for x in foodData}
vitaminB12 = {x[0]: float(x[26]) for x in foodData}
vitaminK = {x[0]: float(x[27]) for x in foodData}
cholesterol = {x[0]: float(x[28]) for x in foodData}
fattyAcids1 = {x[0]: float(x[29]) for x in foodData}
fattyAcids2 = {x[0]: float(x[30]) for x in foodData}

#miniumConstraint values for each nutrient
minimumConstraints = foodDataRaw[7147:7148].values.tolist()

#maximumConstraint values for each nutrient
maximumConstraints = foodDataRaw[7149:7151].values.tolist()

#printing the minimum & maximum constraint values
print("minium constraints list:",minimumConstraints)
print("maximum constraints list:",maximumConstraints)

#deleting the first NA value from the constraints list
del minimumConstraints[0][0]
del maximumConstraints[0][0]


#confirming the first NA value is removed
print("first constraint values: ",float(float(minimumConstraints[0][2])), "-", float(maximumConstraints[0][2]))

print(energy)








#Creating a new LpProblem for minimizing the cholestrol
problem = LpProblem("Diet_Problem", LpMinimize)

#Defining variable for amount of the foods
amountVars = LpVariable.dicts("Amounts", foods, 0)

# objective funciton
problem += lpSum([cholesterol[i] * amountVars[i] for i in foods]), 'totalCost'

# constraints --start
problem += lpSum([protien[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][0])
problem += lpSum([protien[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][0])

problem += lpSum([carbohydrates[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][1])
problem += lpSum([carbohydrates[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][1])

problem += lpSum([energy[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][2])
problem += lpSum([energy[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][2])

problem += lpSum([water[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][3])
problem += lpSum([water[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][3])

problem += lpSum([energy2[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][4])
problem += lpSum([energy2[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][4])

problem += lpSum([calcium[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][5])
problem += lpSum([calcium[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][5])

problem += lpSum([iron[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][6])
problem += lpSum([iron[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][6])

problem += lpSum([magnesium[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][7])
problem += lpSum([magnesium[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][7])

problem += lpSum([phosphorous[i] * amountVars[i] for i in foods]) <= float(minimumConstraints[0][8])
problem += lpSum([phosphorous[i] * amountVars[i] for i in foods]) >= float(maximumConstraints[0][8])


problem += lpSum([potassium[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][9])
problem += lpSum([potassium[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][9])

problem += lpSum([sodium[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][10])
problem += lpSum([sodium[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][10])

problem += lpSum([zinc[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][11])
problem += lpSum([zinc[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][11])

problem += lpSum([copper[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][12])
problem += lpSum([copper[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][12])

problem += lpSum([manganese[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][13])
problem += lpSum([manganese[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][13])

problem += lpSum([selenium[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][14])
problem += lpSum([selenium[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][14])

problem += lpSum([vitaminA[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][15])
problem += lpSum([vitaminA[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][15])

problem += lpSum([vitaminE[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][16])
problem += lpSum([vitaminE[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][16])

problem += lpSum([vitaminD[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][17])
problem += lpSum([vitaminD[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][17])

problem += lpSum([vitaminC[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][18])
problem += lpSum([vitaminC[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][18])

problem += lpSum([thiamin[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][19])
problem += lpSum([thiamin[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][19])

problem += lpSum([riboflavin[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][20])
problem += lpSum([riboflavin[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][20])

problem += lpSum([niacin[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][21])
problem += lpSum([niacin[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][21])

problem += lpSum([pantothenic[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][22])
problem += lpSum([pantothenic[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][22])

problem += lpSum([vitaminB[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][23])
problem += lpSum([vitaminB[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][23])

problem += lpSum([folate[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][24])
problem += lpSum([folate[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][24])

problem += lpSum([vitaminB12[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][25])
problem += lpSum([vitaminB12[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][25])

problem += lpSum([vitaminK[i] * amountVars[i] for i in foods]) >= float(minimumConstraints[0][26])
problem += lpSum([vitaminK[i] * amountVars[i] for i in foods]) <= float(maximumConstraints[0][26])
# constraints --end

#solving problem
problem.solve()

varsDictionary = {}

#printing the optimized solution
print("Optimal solution includes: ")
for var in problem.variables():
    varsDictionary[var.name] = var.varValue
    if(var.varValue>0):
        print(var.name , ": ", var.varValue)

print("Total cholestrol: ",pulp.value(problem.objective))
