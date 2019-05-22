#!python3
# Returns the price raise needed to cover for exchange fees

import sys

EXCHANGE_FEE = 95 # price fee for GMO click s.

# Usage----
# fee.py Volume
#where Volume is an int
if len(sys.argv)>1:
    Volume = int(sys.argv[1])
    print(round(EXCHANGE_FEE/Volume,2))
