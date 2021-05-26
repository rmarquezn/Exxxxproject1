# Rodrigo Márquez A01022943
# Vicente Santamaría A01421801

# Integrative Practice - Part 1
# Computational Mathematics

# ask for input file and create file name
import numpy as np
n = input('¿Que archivo deseas utilizar? (1/2)')
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
# WHERE qx: currentState, s:character, qy:newState


def transitionFunction(state, character):
    # state = transitionTable['currentState']
    # character = transitionTable['currentState']['character']

    return transitionTable[f'{state}'][f'{character}']
# !!!! returns the new state depending on current state and character


def lambdaTransition(state, chars):
    if not transitionFunction(state, 'lambda'):
        return state
        print(f'lambda states: {state}\n')
    # if there are no lambda transitions we stay in the current state
    else:
        return transitionFunction(state, 'lambda')
        print(f'lambda states: {transitionFunction(state, "lambda")}\n')


def extendedTransitionFunction(state, chars):
    # receives current state and transition string
    # ∂'(qx,s)=∂(qx,c)=qy
    # WHERE qx:currentState, s:transition string, c: character, qy: new state
    # state must always be the initial state

    print(f'\nextendedTransition({state},{chars})')
    # finds lambda transition states
    lambdaStates = lambdaTransition(state, chars)
    # if the string is empty we return the current state
    if (len(chars) == 0):
        return lambdaStates

    # we evaluate the string until it's empty
    while(len(chars) != 0):
        print(f'string: {chars}')
        print(f'current states: {lambdaStates}')
        print(f'transition character: {chars[0]}')
        tempStates = []
        # we find the new states
        for stt in lambdaStates:
            if transitionFunction(str(stt), chars[0]) != None:
                tempStates = tempStates + \
                    (transitionFunction(str(stt), chars[0]))
        lambdaStates = tempStates
        print(f'new states: {tempStates}')

        # we evaluate lambda transitions to find the new lambda states
        for ls in tempStates[:]:
            if transitionFunction(str(ls), 'lambda'):
                lambdaStates.remove(ls)
                lambdaStates = lambdaStates + \
                    (transitionFunction(str(ls), 'lambda'))
        print(f'new lambda states: {lambdaStates}\n')
        # we remove the evaluated character from the string
        chars = chars[1:]

    tempList = []
    finalLast = None
    # we create a list with the last states and evaluate if they're final
    for lambS in lambdaStates:
        if not transitionFunction(str(lambS), 'lambda'):
            tempList.append(str(lambS))
        else:
            tempList.append(str(transitionFunction(str(lambS), 'lambda')))
        last = np.array([tempList])
        last = last.flatten()
        finalLast = np.unique(last)
    finalStates = np.array(final)

    # if a state is final we print it
    if np.any(np.in1d(finalLast, finalStates)):
        finishedSet = set(finalLast) & set(finalStates)
        print(f'\nYour final state is: {finishedSet}')
    # if no state is final we reject the string and print the last state
    else:
        print(
            f'\nYour string cannot be evaluated as your current state ({finalLast}) is not final')
    return finalLast


# ask for string to evaluate
evalString = input('Que string deseas evaluar?\n')

# run extended transition function
extendedTransitionFunction(initial, evalString)
