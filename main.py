import modules
import parse
from shared import termList
import sys

if len(sys.argv) == 1:
	print("no argument given")
	exit()
splits = sys.argv[1].split()
parse.buildTerm(splits)
termList.sort(key=lambda term: term.exponent)
parse.symplify()
poly = modules.Polynomial(termList)
print("Reduced form:", poly)
poly.print_degree()
poly.calculate()
