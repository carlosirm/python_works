"""8-15. Printing Models: Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of print_models.py, and modify the file to use the imported functions."""
from p147_passing_a_list import print_models as pm, show_completed_models as scm

unprinted_designs = ['llave ajustable', 'piramide de guiza', 'circulo']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)


"""8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
--------------------------------------------
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
--------------------------------------------"""

"""8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section."""