import ft_math
import parse
from shared import termList
import sys

if len(sys.argv) == 1:
	print("no argument given")
	exit()
splits = sys.argv[1].split()
parse.buildTerm(splits)
termList.sort(key=lambda term: term.exponent)
print("termlist_len:", len(termList))
for item in termList:
	print(item)
# TODO: symplify equation and build Polynomial
