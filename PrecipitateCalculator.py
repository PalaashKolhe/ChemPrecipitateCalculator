'''
title: Precipitate Calculator
author: Palaash Kolhe
date created: 2018-04-30
'''

## Subroutines
def tryAgain(usr):
    if usr in ('Y', 'y', ''):
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
solubilityF = (('F', -1), (('Li', 'Mg', 'Ca', 'Sr', 'Ba', 'Fe', 'Hg2', 'Pb'), (1, 2, 2, 2, 2, 2, 2, 2))) ## Charges added at the end to allow me to find charge of element quickly
solubilityCl = (('Cl', 'Br', 'I', -1), (('Cu', 'Ag', 'Hg2', 'Pb', 'Tl'), (1, 1, 2, 2, 1)))
solubilitySO = (('So4', -2), (('Ca', 'Sr', 'Ba', 'Ag', 'Hg2', 'Pb', 'Ra'), (2, 2, 2, 1, 2, 2, 2)))
solubilityClO3 = (('Clo4', 'Ch3coo', -1), (('Rb', 'Cs', 'Ag', 'Hg2'), (1, 2, 1, 2)))
solubilityCO3 = (('Co3', 'Po4', 'So3', -2. -3. -2), ('H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Nh4'))
solubilityIO3 = (('Io3', 'Ooccoo', -1, -2), ('H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Nh4', 'Co' , 'Fe')) # Co, Fe 3+
solubilityOH = (('Oh', -1), ('H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Nh4'))

charge1 = ('Li', 'Cu', 'Ag', 'Tl', 'Nh4', 'Rb', 'Nh4', 'Na', 'K', 'Rb', 'Cs', 'Fr', 'Ag')
charge2 = ('Mg', 'Ca', 'Sr', 'Ba', 'Fe', 'Hg2', 'Pb', 'Ca', 'Sr', 'Ba', 'Ra', 'Cs', 'Be', 'Mn', 'Co', 'Ni', 'Pd', 'Zn', 'Cd', 'Po', 'Md', 'No')
charge3 = ('Sc', 'Y', 'La', 'Ac', 'Cr', 'Rh', 'Au', 'Al', 'Ga', 'In', 'Sb', 'Bi', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Lr')
charge4 = ('Ti', 'Zr', 'Hf', 'Rf', 'Ir', 'Pt', 'Ge', 'Sn',
           'Th', 'Pu')
charge5 = ('V', 'Nb', 'Ta', 'Pa', 'Np')
charge6 = ('Mo', 'W', 'U')
charge7 = ('Tc', 'Re')

massData = (('Fe', 55.85), ('Hg2', 401.18), ('So4', 96.07), ('Ra', 226), ('Clo3', 83.45), ('Clo4', 99.45), ('Ch3coo', 58.04), ('H', 1.008), ('He', 4.003), ('Li', 6.941),('Be', 9.012), ('B', 10.811), ('C', 12.011), ('N', 14.007), ('O', 15.999), ('F', 18.998), ('Ne', 20.18), ('Na', 22.99), ('Mg', 24.305), ('Al', 26.982), ('Si', 28.086), ('P', 30.974), ('S', 32.065), ('Cl', 35.453), ('Ar', 39.948), ('K', 39.098), ('Ca', 40.078), ('Sc', 44.956), ('Ti', 47.867), ('V', 50.942), ('Cr', 51.996), ('Mn', 54.938), ('Fe', 55.845), ('Co', 58.933), ('Ni', 58.693), ('Cu', 63.546), ('Zn', 65.39), ('Ga', 69.723), ('Ge', 72.64), ('As', 74.922), ('Se', 78.96), ('Br', 79.904), ('Kr', 83.8), ('Rb', 85.468), ('Sr', 87.62), ('Y', 88.906), ('Zr', 91.224), ('Nb', 92.906), ('Mo', 95.94), ('Tc', 98), ('Ru', 101.07), ('Rh', 102.906), ('Pd', 106.42), ('Ag', 107.868), ('Cd', 112.411), ('In', 114.818), ('Sn', 118.71), ('Sb', 121.76), ('Te', 127.6), ('I', 126.905), ('Xe', 131.293), ('Cs', 132.906), ('Ba', 137.327), ('La', 138.906), ('Ce', 140.116), ('Pr', 140.908), ('Nd', 144.24), ('Pm', 145), ('Sm', 150.36), ('Eu', 151.964), ('Gd', 157.25), ('Tb', 158.925), ('Dy', 162.5), ('Ho', 164.93), ('Er', 167.259), ('Tm', 168.934), ('Yb', 173.04), ('Lu', 174.967), ('Hf', 178.49), ('Ta', 180.948), ('W', 183.84), ('Re', 186.207), ('Os', 190.23), ('Ir', 192.217), ('Pt', 195.078), ('Au', 196.967), ('Tl', 204.383), ('Pb', 207.2), ('Bi', 208.98), ('Po', 209), ('At', 210), ('Rn', 222), ('Fr', 223), ('Ra', 226), ('Ac', 227), ('Th', 232.038), ('Pa', 231.036), ('U', 238.029), ('Np', 237), ('Pu', 244), ('Am', 243), ('Cm', 247), ('Bk', 247), ('Cf', 251), ('Es', 252), ('Fm', 257), ('Md', 258), ('No', 259), ('Lr', 262), ('Rf', 261), ('Db', 262), ('Sg', 266), ('Bh', 264), ('Hs', 277), ('Mt', 268), ('Ds', 271), ('Rg', 272), ('Uub', 285), ('Uut', 284), ('Uuq', 289), ('Uup', 288), ('Uuh', 292), ('Uuo', 294), ('Co3', 60.01), ('Po4', 94.97), ('So3', 80.07), ('Io3', 174.9), ('Ooccoo', 88.02), ('Oh', 17.01))

## Translations
Subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

### Main Code Starts Here ###

## Start Menu
print('''
Welcome to Precipitate Calculator!
Enter your two elements and we figure out if the solution forms a precipitate. If it does we give you the balanced reaction, the limiting reagent, and the mass of tbe precipitate.
''')

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

    # Processing
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


    if negIon in solubilityF[0] and posIon in solubilityF[1][0] or negIon in solubilityCl[0] and posIon in solubilityCl[1][0]  or negIon in solubilitySO[0] and posIon in solubilitySO[1][0] or negIon == solubilityClO3[0][0] and posIon == solubilityClO3[1][0][0] or negIon == solubilityClO3[0][0] and posIon == solubilityClO3[1][0][1] or negIon == solubilityClO3[0][1] and posIon == solubilityClO3[1][0][2] or negIon == solubilityClO3[0][1] and posIon == solubilityClO3[1][0][3] or negIon in solubilityCO3[0] and posIon not in solubilityCO3[1] or negIon in solubilityIO3[0] and posIon not in solubilityIO3[1] or negIon in solubilityOH[0] and posIon not in solubilityOH[1]:

        ### Charges
        if negIon in solubilityF[0] or negIon in solubilityCl[0] or negIon in solubilityClO3[0] or negIon == 'Io3' or negIon in solubilityOH[0]:
            neg.append(-1)
        elif negIon == 'Po4':
            neg.append(-3)
        else:
            neg.append(-2)

        if posIon in charge1:
            pos.append(1)
        elif posIon in charge2:
            pos.append(2)
        elif posIon in charge3:
            pos.append(3)
        elif posIon in charge4:
            pos.append(4)
        elif posIon in charge5:
            pos.append(5)
        elif posIon in charge6:
            pos.append(6)
        elif posIon in charge7:
            pos.append(7)

        ### Balancing
        if neg[3] == -2 and pos[3] == 4:
            pos.append(1)
            neg.append(int(pos[3] / (neg[3] - (neg[3] * 2))))
        else:
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
            finalProduct = [namePos,'(', nameNeg,')', chargeNeg]
        elif chargeNeg == '1' and chargePos != '1':
            finalProduct = ['(', namePos, ')',  chargePos, nameNeg]
        else:
            finalProduct = ['(', namePos,')', chargePos,'(',  nameNeg, ')',  chargeNeg]
        finalProduct = ''.join(finalProduct)

        finalProduct = finalProduct.translate(Subscript)

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
        neg[0] = neg[0].translate(Subscript)
        pos[0] = pos[0].translate(Subscript)

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
print('''
Thank you for using Precipitate Calculator!''')
