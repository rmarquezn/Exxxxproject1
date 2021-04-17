transitionTable = dict(string, dict(string, string))


def transitionFunction(state, character):
    return transitionTable(state, character)


def extendedTransitionFunction(state, chars):
    if (len(chars) == 0):
        return state
    else:
        if(len(chars) == 1):
            return transitionFunction(state, chars)
        else:
            firstPart = 'x'
            lastChar = 'y'

            transitionFunction(extendedTransitionFunction(
                state, firstPart), lastChar)
