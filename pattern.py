import sys
MAX_PATTERN_LENGTH = 52*52*10
def pattern_generator(len):
	"""
	Generate a pattern in order to calculate the offset of stack.
	If the program has ASLR, it is hard to calculate the offset manually.
	Therefore, I decide to make my own tools to generate the input pattern 
	in order to help me to exploit the bof and some ctf problem
	"""

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

if __name__ == '__main__':

	if( len(sys.argv) < 3):
		help()
	else:
		if(sys.argv[1] == '--generate' or sys.argv[1] == '-g'):
			pattern_generator(sys.args[2])
		elif (sys.argv[1] == '--search' or sys.argv[1] == '-s'):
			search_pattern(sys.argv[2])
		else:
			help();