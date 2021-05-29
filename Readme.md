# Python
- everything in python is object
- function in python is first class function (you can pass function as a parameter)
# Closure
- access to variables, functions, classes from different (outer, actual retrieved) scope
- variables are stored in function object
## Creation
1. Need to have min 2 function, one outer and one inner
2. Outer function should return declaration of inner function
3. Inner function have to use something from outer function (variable, other function, class), and only this will be
   recorded
## Use case:
- persistence (trwałość)
## Cons
- if you not understand you can leak memory

--DRY--don't repeart 

#Decorator
- add additional functionality to function(augmented function)
-- 3 types of decorator
   1. function decorator
      -need to use closure for creating
   2. class decorator
   3. decorator as a desing pattern
     - different from python decorator functionality 
      

