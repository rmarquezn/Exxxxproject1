# import txt file

# initialize transition table
transitionTable = {'state': None, 'character': {
    'state': None, 'character': None}}


def transitionFunction(state, character):
    return transitionTable(state, character)


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
