//transition table
HashTable<String,HashTable<String,String> transitionTable;


public String transitionFunction(String state, String character){
    return transitionTable.get(state).get(character);
}

public extendedTransitionFunctioin(String state, String chars){
    //empty string
    if (chars.length()==0){
        return state;
    } else{
        if(chars.length()==1){
            return transitionFunction(state,chars);
        }else{
            String firstPart = chars.substring(chars.length()-1);
            String lastChar = chars.charAt(chars.length()-1)+"";

            return transitionFunction(extendedTransitionFunction(state,firstPart),lastChar);
        }
    }
}