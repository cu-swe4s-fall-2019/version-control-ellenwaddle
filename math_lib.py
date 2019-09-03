import argparse

parser=argparse.ArgumentParser(
	description='supply numbers',
	prog='bay')

parser.add_argument('-numerator',
	type=int,
	help='supply numerator',
	required=True)
parser.add_argument('-denominator',
	type=int,
	help='supply denominator',
	required=True)

def div(a, b):
	if b>0:
    		return a/b

	else: 
		return None

args=parser.parse_args()
print(args)
