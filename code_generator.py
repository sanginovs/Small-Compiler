'''This is a code generator function which recursively calls itself to print each node in
 the tree into one string'''



def codeGenerator(node):

    if node['type'] == 'Program':
        return '\n'.join([code for code in map(codeGenerator, node['body'])])
    elif node['type'] == 'ExpressionStatement':
        expression = codeGenerator(node['expression'])
        return '%s;' % expression
    elif node['type'] == 'CallExpression':
        callee = codeGenerator(node['callee'])
        params = ', '.join([code for code in map(codeGenerator, node['arguments'])])
        return "%s(%s)" % (callee, params)
    elif node['type'] == 'Identifier':
        return node['name']
    elif node['type'] == 'NumberLiteral':
        return node['value']
    else:
        raise TypeError(node['type'])