'''
This is a traverser function which takes Abstract Syntax Tree as an input 
It should traverse through each node on the AST


'''


def traverser(ast, visitor):
	    

	def traverse_array(array, parent):
		for child in array:
			traverse_node(child, parent)


	def traverse_node(node, parent):

		methods= visitor[node[type]]

		if methods and methods.enter:
			methods.enter(node, parent)



		def switch_case(node_type):
			try:
				return {
					'Program': traverse_array(node["body"], node),
					'CallExpression': traverse_array(node["params"], node),
					"NumberLiteral": None,
					"StringLiteral": None
				}[node_type]
			except:
				raise TypeError

		switch_case(node["type"])

		if methods and methods.exit:
			methods.exit(node, parent)

	traverse_node(ast, None)



def transformer():
	'''this function takes AST as an input and passes into traverser function with a visitor 
	and finally will create a new AST'''

	new_ast={
		type: "Program",
		"body": []

	}