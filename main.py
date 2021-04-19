# ask for input file and create file name
n = 1  # input('¿Que archivo deseas utilizar? (1/2)')
fileName = (f'test{n}.txt')

# import and read file
file = open(fileName, 'r')
reader = file.read()
reader = reader.splitlines()
print(f'file array = {reader}\n')
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
newTransitionsList = []
for element in reader:
    currentStateList.append(element[:2])
    transitionsList.append(element[3:])
print(f'current state list = {currentStateList}\n')
for trans in transitionsList:
    trans = trans.split('=>')
    newTransitionsList.append(trans)
for t in newTransitionsList:
    t[1] = t[1].split(',')
print(f'transitions = {newTransitionsList}\n')

# initialize transition table
transitionTable = {'currentState': None, 'transition': {
    'character': None, 'newState': None}}
# ∂(qx,s)=qy
# WHERE qx: currentState, s:transition,character, qy:transition,newState


def transitionFunction(state, character):
    # state = transitionTable['currentState']
    # character = transitionTable['transition']['character']

    # return = transitionTable['transition']['newState']
    return transitionTable['transition']['newState']

    # !!!! returns the new state depending on current state and character
    # ∂(qx,s)=qy
    # WHERE qx: state, s:character, qy: transitionTable(transition,newState)


def extendedTransitionFunction(state, chars):
    # receives current state and transition string
    # ∂'(qx,s)=∂(qx,c)=qy
    # WHERE qx:currentState, s:transition string, c: currentChar, qz:  newState
    # WHERE
    if (len(chars) == 0):
        return state
    else:
        if(len(chars) == 1):
            return transitionFunction(state, chars[0])
        else:
            firstPart = chars[:-1]  # character array minus the last character
            lastChar = chars[-1]  # only the character, not a string

            transitionFunction(extendedTransitionFunction(
                state, firstPart), lastChar)
