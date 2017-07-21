from tokenizer import tokenizer
from parser import parser
from traverser import traverser, transformer
from code_generator import codeGenerator


#this is a file where you can run the program



def main():
    user_input=input("Please, type your Lisp-like function:")
    tokens = tokenizer(user_input)
    abs_syntax_tree    = parser(tokens)
    new_ast = transformer(abs_syntax_tree)
    output = codeGenerator(new_ast)
    return output



if __name__ == "__main__":
    main()
