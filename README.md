# Exxxxproject1
## Práctica Integradora

Make a program that reads from a file the elements that define an DFA-l and then, shows the processing of a string, step by step.
The transition table will be defined in a txt file. The file shall be defined as follows:
- The first line indicates the set of states of the automata separated by commas. - The second line indicates the alphabet symbols separated by commas
- The third line indicates the initial state
- The fourth line indicates the set of final states separated by commas.
- The following lines indicate the transition table in the following format: state, symbol = > states
states is a list of elements separated by commas.
Example, the following line
q0, a => q1,q2
indicates that the DFA processes the following: d(q0,a) = {q1,q2}
To indicate a spontaneous transition, the word “lambda” will be used.
It is not necessary that all transitions are specified in this file. An evaluation may not appear if a state indicating that the result of that evaluation is the empty set
The program should print step by step the processing. And this should be repeated while the user wants to.
Do not worry about validating the values in the input file. Suppose that were built correctly.