'''
title: Precipitate Calculator
author: Palaash Kolhe
date created: 2018-04-30
'''

# Arrays
pos = [] # (ion name, volume, concentration, charge)
neg = [] # (ion name, volume, concentration, charge)
solubilityF = (('F', -1), (('Li', 'Mg', 'Ca', 'Sr', 'Ba', 'Fe', 'Hg2', 'Pb'), (1, 2, 2, 2, 2, 2, 2, 2)))
solubilityCl = (('Cl', 'Br', 'I', -1), (('Cu', 'Ag', 'Hg2', 'Pb', 'Tl'), (1, 1, 2, 2, 1)))
solubilitySO = (('SO4', -2), (('Ca', 'Sr', 'Ba', 'Ag', 'Hg2', 'Pb', 'Ra'), (2, 2, 2, 1, 2, 2, 2)))

charge1 = ('Li', 'Cu', 'Ag', 'Tl')
charge2 = ('Mg', 'Ca', 'Sr', 'Ba', 'Fe', 'Hg2', 'Pb', 'Ca', 'Sr', 'Ba', 'Ra')

# Subroutines


# Inputs
posIon = input("Please enter the positive reacting ion. (No Charges): ")
posVol = input("What is the volume of the positive solution? (L): ")
posConc = input("What is the concentration of the positive solution. (mol/L): ")

negIon = input("Please enter the negative reacting ion. (No Charges): ")
negVol = input("What is the volume of the negative solution? (L): ")
negConc = input("What is the concentration of the negative solution? (mol/L): ")

# Ion name, volume, and concentration
pos.append(posIon)
pos.append(posVol)
pos.append(posConc)

neg.append(negIon)
neg.append(negVol)
neg.append(negConc)

# Charges
if posIon in solubilityF[0] or posIon in solubilityCl[0]:
    pos.append(-1)
elif posIon in solubilitySO[0]:
    pos.append(-2)
else:
    pass

if negIon in solubilityF[1][0] or negIon in solubilityCl[1][0] or negIon in solubilitySO[1][0]:
    if negIon in charge1:
        neg.append(1)
    else:
        neg.append(2)

print(pos)
print(neg)





