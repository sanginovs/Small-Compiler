'''
This is a traverser function which takes Abstract Syntax Tree as an input 
It should traverse through each node on the AST


'''
import copy


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



def transformer(ast):
	'''this function takes AST as an input and passes into traverser function with a visitor 
	and finally will create a new AST'''

	new_ast={
		type: "Program",
		"body": []

	}

	oldAst = ast
	ast = copy.deepcopy(oldAst)
	ast['_context'] = new_ast.get('body')

	def NumberLiteralVisitor(node, parent):
		parent['_context'].append({
			'type': 'NumberLiteral',
			'value': node['value']
		})

	def CallExpressionVisitor(node, parent):
		expression = {
			'type': 'CallExpression',
			'callee': {
				'type': 'Identifier',
				'name': node['name']
			},
			'arguments': []
		}

		node['_context'] = expression['arguments']

		if parent['type'] != 'CallExpression':
			expression = {
				'type': 'ExpressionStatement',
				'expression': expression
			}
		parent['_context'].append(expression)

	traverser(ast, {
		'NumberLiteral': NumberLiteralVisitor,
		'CallExpression': CallExpressionVisitor
	})

	return new_ast
