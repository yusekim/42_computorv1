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
poly.calculate()      # 판별식이 음수일 때 허근 구해야함 α + β*i.
