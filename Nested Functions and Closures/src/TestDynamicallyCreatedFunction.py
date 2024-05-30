# https://www.geeksforgeeks.org/defining-a-python-function-at-runtime/

# importing the module 
from types import FunctionType 
  
# function during run-time 
f_code = compile('def gfg(): return "GEEKSFORGEEKS"', "<string>", "exec") 
f_func = FunctionType(f_code.co_consts[0], globals(), "gfg") 
  
# calling the function 
print(f_func())
