'''
title: Precipitate Calculator
author: Palaash Kolhe
date created: 2018-04-30
'''

## Subroutines
def tryAgain(usr):
    if usr in ('Y', 'y', ' '):
        return True
    elif usr in ('N', 'n'):
        return False
    else:
        usr = input("Please enter in Y/n: ")
        return tryAgain(usr)

def chkFloat(num):
    try:
        num = float(num)
        return num
    except ValueError:
        num = input("Please enter a number: ")
        return chkFloat(num)

def chkPos(num):
    if num > 0:
        return num
    else:
        num = input("Please enter a number above zero: ")
        num = chkFloat(num)
        return chkPos(num)

## Arrays
solubilityF = (('F', -1), (('Li', 'Mg', 'Ca', 'Sr', 'Ba', 'Fe', 'Hg2', 'Pb'), (1, 2, 2, 2, 2, 2, 2, 2)))
solubilityCl = (('Cl', 'Br', 'I', -1), (('Cu', 'Ag', 'Hg2', 'Pb', 'Tl'), (1, 1, 2, 2, 1)))
solubilitySO = (('So4', -2), (('Ca', 'Sr', 'Ba', 'Ag', 'Hg2', 'Pb', 'Ra'), (2, 2, 2, 1, 2, 2, 2)))

solubilityClO3 = (('Clo3', 'Clo4', 'Ch3coo', -1), (('Rb', 'Cs', 'Ag', 'Hg2'), (1, 2, 1, 2)))

charge1 = ('Li', 'Cu', 'Ag', 'Tl', 'Nh4', 'Rb', 'Nh4')
charge2 = ('Mg', 'Ca', 'Sr', 'Ba', 'Fe', 'Hg2', 'Pb', 'Ca', 'Sr', 'Ba', 'Ra', 'Cs')


massData = (('F', 19.00), ('Li', 6.94), ('Mg', 24.31), ('Ca', 40.08), ('Sr', 87.62), ('Ba', 137.33), ('Fe', 55.85), ('Hg2', 401.18), ('Pb', 207.2), ('Cl', 35.45), ('Br', 79.90), ('I', 126.90), ('Cu', 63.55), ('Ag', 107.87), ('Hg2', 401.18), ('Pb', 207.2), ('Tl', 204.38), ('So4', 96.07), ('Ca', 40.08), ('Sr', 87.62), ('Ba', 137.33), ('Ag', 107.87), ('Hg2', 401.18), ('Pb', 207.2), ('Ra', 226), ('Clo3', 83.45), ('Clo4', 99.45), ('Ch3coo', 58.04), ('Rb', 85.47), ('Cs', 132.91), ('Ag', 107.87))

### Main Code Starts Here ###

repeat = True
while repeat:
    pos = []  # (ion name, volume, concentration, charge, balance, mass)
    neg = []  # (ion name, volume, concentration, charge, balance, mass)
    finalProduct = []

    # Inputs
    posIon = input("Please enter the positive reacting ion. (No Charges): ")
    posVol = chkPos(chkFloat(input("What is the volume of the positive solution? (L): ")))
    posConc = chkPos(chkFloat(input("What is the concentration of the positive solution. (mol/L): ")))

    negIon = input("Please enter the negative reacting ion. (No Charges): ")
    negVol = chkPos(chkFloat(input("What is the volume of the negative solution? (L): ")))
    negConc = chkPos(chkFloat(input("What is the concentration of the negative solution? (mol/L): ")))

    posIon = posIon.lower()
    posIon = posIon.capitalize()

    negIon = negIon.lower()
    negIon = negIon.capitalize()


    ### Ion name, volume, and concentration
    pos.append(posIon)
    pos.append(posVol)
    pos.append(posConc)

    neg.append(negIon)
    neg.append(negVol)
    neg.append(negConc)


    if negIon in solubilityF[0] and posIon in solubilityF[1][0] or negIon in solubilityCl[0] and posIon in solubilityCl[1][0] or negIon in solubilityClO3[0] and posIon in solubilityClO3[1][0] or negIon in solubilitySO[0] and posIon in solubilitySO[1][0]:
        ### Charges
        if negIon in solubilityF[0] or negIon in solubilityCl[0] or negIon in solubilityClO3[0]:
            neg.append(-1)
        else:
            neg.append(-2)

        if posIon in solubilityF[1][0] or posIon in solubilityCl[1][0] or posIon in solubilitySO[1][0] or solubilityClO3[1][0]:
            if posIon in charge1:
                pos.append(1)
            elif posIon in charge2:
                pos.append(2)

        ### Balancing
        if neg[3] - (neg[3] * 2) == pos[3]:
            neg.append(neg[3] - (neg[3] * 2))
            pos.append(pos[3])
        else:
            neg.append(pos[3])
            pos.append(neg[3] - (neg[3] * 2))

        ### Product
        namePos = pos[0]
        chargePos = str(pos[4])

        nameNeg = neg[0]
        chargeNeg = str(neg[4])

        if chargePos == '1' and chargeNeg == '1':
            finalProduct = [namePos, nameNeg]
        elif chargePos == '1' and chargeNeg != '1':
            finalProduct = [namePos, nameNeg, '(', chargeNeg, ')']
        elif chargeNeg == '1' and chargePos != '1':
            finalProduct = [namePos, '(', chargePos, ')', nameNeg]
        else:
            finalProduct = [namePos, '(', chargePos, ')', nameNeg, '(', chargeNeg, ')']
        finalProduct = ''.join(finalProduct)

        ### Mass
        for i in range(len(massData)):
            if pos[0] == massData[i][0]:
                mass1 = massData[i][1]
            elif neg[0] == massData[i][0]:
                mass2 = massData[i][1]

        totalMass = pos[4] * mass1 + neg[4] * mass2

        ### Limiting Reagent
        nPos = posVol * posConc / pos[4]
        nNeg = negVol * negConc / neg[4]

        if nNeg < nPos:
            limit = nNeg * neg[4]
            limitingR = neg[0]
        elif nPos < nNeg:
            limit = nPos * pos[4]
            limitingR = pos[0]
        else:
            limit = nPos * pos[4]
            limitingR = pos[0]

        ### Calculating Mass
        if limitingR == neg[0]:
            mass = limit * pos[4] / neg[4] * totalMass
        else:
            mass = limit * neg[4] / pos[4] * totalMass
        mass = round(mass, 2)

        # Outputs
        print('''''')
        print(pos[4], pos[0], '+', neg[4], neg[0], ' ==> ', finalProduct)
        print('''''')
        print('Limiting Reagent is', limitingR)
        print('The mass of', finalProduct, 'is', mass)
    else:
        print('Solution is soluble so no precipitate is formed! ')

    print('''''')

    ### Try Again
    repeat = tryAgain(input("Would you like to calculate solubility again? Y/n: "))





