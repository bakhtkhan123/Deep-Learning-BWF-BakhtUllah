# Exercise 8.16
import printing_fuction
printing_fuction.make_pizza(10)

import printing_fuction
from printing_fuction import make_pizza
make_pizza(33,'medium pizza')
from printing_fuction import make_pizza as mp
mp(27,'small pizza')
import printing_fuction as pf
pf.make_pizza(22,'large pizza')
from printing_fuction import *