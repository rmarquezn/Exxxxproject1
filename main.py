# ask for input file and create file name
n = input('¿Que archivo deseas utilizar? (1/2)')
fileName = (f'test{n}.txt')

# import and read file
file = open(fileName, 'r')
reader = file.read()
print(reader)
# states = FIRST LINE
# symbols = SECOND LINE: a,b,lambda
# initialState = THIRD LINE
# finalStates = FOURTH LIINE
# transitionTable format: state, symbol(character) => states(csv) WHERE 'lambda'==spontaneous transition


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
