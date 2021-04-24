# Rodrigo Márquez A01022943
# Vicente Santamaría A01421801

# Integrative Practice - Part 1
# Computational Mathematics

# ask for input file and create file name
import numpy as np
n = 1  # input('¿Que archivo deseas utilizar? (1/2)')
fileName = (f'test{n}.txt')

# import and read file
file = open(fileName, 'r')
reader = file.read()
reader = reader.splitlines()

# states = FIRST LINE
states = reader.pop(0)
states = states.split(',')
print(f'states = {states}\n')

# symbols = SECOND LINE: a,b,lambda
symbols = reader.pop(0)
symbols = symbols.split(',')
symbols.append('lambda')
print(f'symbols = {symbols}\n')

# initialState = THIRD LINE
initial = reader.pop(0)
print(f'initial state = {initial}\n')

# finalStates = FOURTH LIINE
final = reader.pop(0)
final = final.split(',')
print(f'final states = {final}\n')

# transitionTable format: state, symbol(character) => states(csv) WHERE 'lambda'==spontaneous transition
currentStateList = []
transitionsList = []
finalTransitionList = []
for element in reader:
    currentStateList.append(element[:2])
    transitionsList.append(element[3:])
for trans in transitionsList:
    trans = trans.split('=>')
    finalTransitionList.append(trans)
for t in finalTransitionList:
    t[1] = t[1].split(',')

# initialize transition table
transitionTable = {}
for s in states:
    transitionTable[str(s)] = {}
    for sym in symbols:
        transitionTable[str(s)][str(sym)] = []

# tabla = {'state': {'character': newStateList[]}

# populate transition table
index = 0
for st in currentStateList:
    transitionTable[str(st)][str(finalTransitionList[index]
                                 [0])] = finalTransitionList[index][1]
    index = index+1
print(f'transition table = {transitionTable}\n')
# ∂(qx,s)=qy
# WHERE qx: currentState, s:transition,character, qy:transition,newState


def transitionFunction(state, character):
    # state = transitionTable['currentState']
    # character = transitionTable['currentState']['character']

    # return = transitionTable['transition']['newState']
    print(f'transitionfunction({state},{character})')
    print(f'state = {state}')
    print(f'character = {character}')
    print('new states = ')
    print(transitionTable[f'{state}'][f'{character}'])
    return transitionTable[f'{state}'][f'{character}']


# !!!! returns the new state depending on current state and character
# ∂(qx,s)=qy
# WHERE qx: state, s:character, qy: transitionTable(transition,newState)


def extendedTransitionFunction(state, chars):
    # receives current state and transition string
    # ∂'(qx,s)=∂(qx,c)=qy
    # WHERE qx:currentState, s:transition string, c: currentChar, qy:  newState
    # WHERE state = currentState[0], chars stringChar
    lambdaStates = transitionFunction(state, 'lambda')
    if (len(chars) == 0):
        return lambdaStates
    else:
        tempStates = []
        for s in lambdaStates:
            if transitionFunction(str(s), chars[0]) != None:
                tempStates.append(transitionFunction(str(s), chars[0]))
        lambdaStates = []

        for ls in tempStates:
            if transitionFunction(str(ls), 'lambda') != None:
                lambdaStates.append(transitionFunction(str(ls), 'lambda'))
        chars = chars[1:]
    tempEL = []
    for lambS in lambdaStates:
        tempEL.append(transitionFunction(str(lambS), 'lambda'))
        finished = np.array([tempEL])
        finished = finished.flatten()
        finished2 = np.unique(finished)
    return finished2

    # if(len(chars) == 1):
    #     return transitionFunction(state, chars[0])
    # else:
    #     firstPart = chars[:-1]  # character string minus the last character
    #     lastChar = chars[-1]  # only the character, not a string

    #     transitionFunction(extendedTransitionFunction(
    #         state, firstPart), lastChar)


# ask for string to evaluate
evalString = input('Que string deseas evaluar?\n')
extendedTransitionFunction(initial, evalString)
