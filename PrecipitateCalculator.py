'''
title: Precipitate Calculator
author: Palaash Kolhe
date created: 2018-04-30
'''

# Arrays
pos = [] # (ion name, volume, concentration, charge, balance, mass)
neg = [] # (ion name, volume, concentration, charge, balance, mass)
finalProduct = []
solubilityF = (('F', -1), (('Li', 'Mg', 'Ca', 'Sr', 'Ba', 'Fe', 'Hg2', 'Pb'), (1, 2, 2, 2, 2, 2, 2, 2)))
solubilityCl = (('Cl', 'Br', 'I', -1), (('Cu', 'Ag', 'Hg2', 'Pb', 'Tl'), (1, 1, 2, 2, 1)))
solubilitySO = (('SO4', -2), (('Ca', 'Sr', 'Ba', 'Ag', 'Hg2', 'Pb', 'Ra'), (2, 2, 2, 1, 2, 2, 2)))

charge1 = ('Li', 'Cu', 'Ag', 'Tl')
charge2 = ('Mg', 'Ca', 'Sr', 'Ba', 'Fe', 'Hg2', 'Pb', 'Ca', 'Sr', 'Ba', 'Ra')

massData = (('F', 19.00), ('Li', 6.94), ('Mg', 24.31), ('Ca', 40.08), ('Sr', 87.62), ('Ba', 137.33), ('Fe', 55.85), ('Hg2', 401.18), ('Pb', 207.2), ('Cl', 35.45), ('Br', 79.90), ('I', 126.90), ('Cu', 63.55), ('Ag', 107.87), ('Hg2', 401.18), ('Pb', 207.2), ('Tl', 204.38), ('SO4', 96.07), ('Ca', 40.08), ('Sr', 87.62), ('Ba', 137.33), ('Ag', 107.87), ('Hg2', 401.18), ('Pb', 207.2), ('Ra', 226))

# Inputs
posIon = input("Please enter the positive reacting ion. (No Charges): ")
posVol = float(input("What is the volume of the positive solution? (L): "))
posConc = float(input("What is the concentration of the positive solution. (mol/L): "))

negIon = input("Please enter the negative reacting ion. (No Charges): ")
negVol = float(input("What is the volume of the negative solution? (L): "))
negConc = float(input("What is the concentration of the negative solution? (mol/L): "))

# Ion name, volume, and concentration
pos.append(posIon)
pos.append(posVol)
pos.append(posConc)

neg.append(negIon)
neg.append(negVol)
neg.append(negConc)

# Charges
if negIon in solubilityF[0] or negIon in solubilityCl[0]:
    neg.append(-1)
elif negIon in solubilitySO[0]:
    neg.append(-2)
else:
    pass

if posIon in solubilityF[1][0] or posIon in solubilityCl[1][0] or posIon in solubilitySO[1][0]:
    if posIon in charge1:
        pos.append(1)
    else:
        pos.append(2)

# Balancing
if neg[3] - (neg[3] * 2) == pos[3]:
    neg.append(neg[3] - (neg[3] * 2))
    pos.append(pos[3])
else:
    neg.append(pos[3])
    pos.append(neg[3] - (neg[3] * 2))

# Product
name1 = pos[0]
charge1 = str(pos[4])

name2 = neg[0]
charge2 = str(neg[4])

if charge1 == '1' and charge2 == '1':
    finalProduct = [name1, name2]
elif charge1 == '1' and charge2 != '1':
    finalProduct = [name1, name2, charge2]
elif charge2 == '1' and charge1 != '1':
    finalProduct = [name1, charge1, name2]
else:
    finalProduct = [name1, charge1, name2, charge2]
finalProduct = ''.join(finalProduct)

# Mass
for i in range(len(massData)):
    if pos[0] in massData[i][0]:
        mass1 = massData[i][1]
    elif neg[0] in massData[i][0]:
        mass2 = massData[i][1]

totalMass = pos[4] * mass1 + neg[4] * mass2

# Limiting Reagent
nPos = posVol * posConc / pos[4]
nNeg = negVol * negConc / neg[4]

if nNeg < nPos:
    limit = nNeg
    limitingR = neg[0]
elif nPos < nNeg:
    limit = nPos
    limitingR = pos[0]
else:
    limit = nPos
    limitingR = pos[0]

# Calculating Mass
if limitingR == neg[0]:
    mass = limit * pos[4] / neg[4]
else:
    mass = limit * neg[4] / pos[4]

## Outputs
print(pos[4], pos[0], '+', neg[4], neg[0], ' ==> ', finalProduct)
print('Limiting Reagent is', limitingR)
print(totalMass)
print(pos)
print(neg)





