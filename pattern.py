import sys
MAX_PATTERN_LENGTH = 26*26*10
def pattern_generator(length):
	"""
	Generate a pattern in order to calculate the offset of stack.
	If the program has ASLR, it is hard to calculate the offset manually.
	Therefore, I decide to make my own tools to generate the input pattern 
	in order to help me to exploit the bof and some ctf problem
	"""
	if (length > MAX_PATTERN_LENGTH):
		return
	_first = 'A'
	_second = 'a'
	_third = '0'
	pattern = ''
	for i in range(26):
		_first = chr(ord(_first) + i )
		for j in range(26):
			_second = chr(ord(_second) + j)
			for k in range(10):
				_third = chr(ord(_third) + k)
				if( len(pattern) < int(length)):
					pattern += _first+_second+_third
					#print(pattern)
				else:
					ret = pattern[:length]
					#print(ret)
					return ret



def search_pattern(input_pattern):
	"""
	Searching the pattern and calculate the offset 
	from the pattern this generator generated.
	"""
def help():
	print ('Usage: %s [-g]LENGTH [-s]PATTERN ' % sys.argv[0])
	print ()
	print ('-g \t (or --generate) \tGenerate a pattern, such as Aa0Aa1...')
	print ('-s \t (or --search)   \tSearch offset from input pattern ')

if _name_ == '_main_':

	if( len(sys.argv) < 3):
		help()
	else:
		if(sys.argv[1] == '--generate' or sys.argv[1] == '-g'):
			pattern = pattern_generator(int(sys.argv[2]))
			print(pattern)
		elif (sys.argv[1] == '--search' or sys.argv[1] == '-s'):
			search_pattern(sys.argv[2])
		else:
			help();