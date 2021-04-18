# import txt file
file = open('test1.txt', 'r')
reader = file.read()
# print(reader)
# states = FIRST LINE
# symbols = SECOND LINE
# initialState = THIRD LINE
# finalStates = FOURTH LIINE
# transitionTable format: state, symbol => states(csv) WHERE 'lambda'==spontaneous transition


# initialize transition table
transitionTable = {'currentState': None, 'transition': {
    'character': None, 'newState': None}}


def transitionFunction(state, character):
    return transitionTable(state, character)
    # returns a state


def extendedTransitionFunction(state, chars):
    if (len(chars) == 0):
        return state
    else:
        if(len(chars) == 1):
            return transitionFunction(state, chars)
        else:
            firstPart = chars[-1]
            lastChar = chars[-1]+''

            transitionFunction(extendedTransitionFunction(
                state, firstPart), lastChar)
