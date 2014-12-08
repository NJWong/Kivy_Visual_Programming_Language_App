# Type definitions

Integer = int
Boolean = bool
List = list

def tokenize(chars):
	return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program):
	return read_from_tokens(tokenize(program))

def read_from_tokens(tokens):
	if len(tokens) == 0:
		raise SyntaxError('unexpected EOF while reading')
	token = tokens.pop(0)
	if token == '(':
		L = []
		while tokens[0] != ')':
			L.append(read_from_tokens(tokens))
		tokens.pop(0) # remove the ending ')'
		return L
	elif token == ')':
		raise SyntaxError('unexpected')
	else:
		return atom(token)

def atom(token):
	try:
		return int(token)
	except ValueError:
		try:
			return bool(token)
		except ValueError:
			try:
				return list(token)
			except ValueError:
				print('Not recognised type')
				return str(token)

Env = dict

def standard_env():
	env = Env()
	env.update({}
	
	})