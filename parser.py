'''
Parser function
*takes generated tokens array by the tokenizer function and turns them into Abstract Syntax Tree.
This basically means that the function takes these tokens and reformats them into a representation that 
describes each part of the syntax and their relationship to one another. Each token is a node in AST.

{



}


Input: array of tokens e.g: (add 2 (subtract 4 2)) 
 [
 {<class 'type'>: 'paren', 'value': '('}, 
 {<class 'type'>: 'name', 'value': 'add'}, 
 {<class 'type'>: 'number', 'value': '2'}, 
 {<class 'type'>: 'paren', 'value': '('}, 
 {<class 'type'>: 'name', 'value': 'subtract'}, 
 {<class 'type'>: 'number', 'value': '4'}, 
 {<class 'type'>: 'number', 'value': '2'}, 
 {<class 'type'>: 'paren', 'value': ')'}, 
 {<class 'type'>: 'paren', 'value': ')'}
 ]
 Output: [{ type: 'paren', value: '(' }, ...]   =>   { type: 'Program', body: [...] }


'''

def parser(token_array):
    current=0





    def recusive_walk(current):
        token=token_array[current]

        #test if it's a string token
        if token.type == "string":
            current+=1
            return {type: 'StringLiteral', "value" : token.value}
        #test if token is a number
        elif token.type == "number":
            current+=1
            return {type:'NumberLiteral', "value":token.value}

        #test for call expressions. In our functions, right after parentheses comes callExpression
        #e.g (add 2 2) --> add(2,2)

        # skip it since we don't need it
        elif token.type == 'paren' and token.value=='(':
            current+=1
            token=token_array[current]

            node={type: "CallExpressions",
                "name": token.value,
                "params": []  #takes parameter: e.g (add 2 2) --> add is a CallExpression params=[2,2]
            }

            current+=1
            token=token_array[current]


            while token.type != 'paren' and token.value !=")":
                node["params"].push(recusive_walk(current))
                token=token_array[current]


            current+=1 #skip the closing parentheses
            return node

        raise TypeError


    abstract_syntax_tree={
        type: "Program",
        "body": []
    }



    #push everything into abstract_syntax_tree

    while current < token_array.length:
        abstract_syntax_tree["body"].append(recusive_walk(current))


    return abstract_syntax_tree




