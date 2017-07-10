#Author: Sher Sanginov
"""
This is a tokenizer function for the compiler which divides the user input into tokens


Regardless of where the program comes from it must first pass through a Tokenizer, 
or as it is sometimes called, a Lexer. The tokenizer is responsible for dividing the 
input stream into individual tokens, identifying the token type, and passing tokens one 
at a time to the next stage of the compiler. Source: Anatomy of a Compiler: http://www.cs.man.ac.uk/~pjj/farrell/comp3.html


"""


def tokenizer(input):
	'''takes user input in Lisp-like format e.g (add 2 (sub 4 2 )) and spits out an array of 
		each piece of tokens
		
		pre: Lisp-like functions e.g. (add 2 (sub 4 2 )
		post: returns array e.g. [{type: 'paren', 'value': '('}, {type: 'name', 'value':'add'}...]
		'''

	current=0
	tokens=[]
	while current < len(input):
		char=input[current]
		
		#check for open parentheses
		if char == "(":
			tokens.append({type: 'paren', "value": '('})
		#increment current
			current+=1
			continue

		
		#check for closing parentheses
		if char==")":
			tokens.append({type:"paren", "value": ")"})
			current+=1
			continue

		#check for whitespaces. we care that whitespaces exists to separate characters and we won't store it as a token
		
		if char.isspace():
			current+=1
			continue
		#the next step is to check numbers
		#a little different because numbers can be any length, thus
		#we want to capture entire number from beginning to end and put them in one token
		#e.g (add 123 546) - two separate tokens
		
		if char.isdigit():
			value=""
			while char.isdigit() != False:
				value=value+char
				current+=1
				char=input[current]
			tokens.append({type: 'number', "value": value})
			continue
		
		#support for strings: anything surrounder by quotes on both sides
				 
		if char == '"':
			value=""
			#we not going to insert quote in our token array
			current+=1
			char=input[current]
			
			#iterate through each character until we reach closing quote
			while char !='"':
				value=value+char
				current=current+1
				char=input[current]
			
			#skipping closing quote
			current=current+1
			char=input[current]
		
		#add string to token array
			tokens.append({type:"string", "value": value})
			continue

#finally the last token will be a name token, basically name of our function like (add 2 4), name token will be add
		
		if char.isalpha():
			value=""
			while char.isalpha():
				value=value+char
				current=current+1
				char=input[current]
			tokens.append({type: "name", "value":value})
			continue

		raise ValueError("Error, this character is not defined:"+char)
		
	return tokens

user_input=input("What is your LispLike Function?")
tokens=tokenizer(user_input)
print ("Here is each tokens stored in an array: ", tokens)
