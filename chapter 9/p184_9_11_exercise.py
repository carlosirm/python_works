"""9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly."""

from p178_exercises import Admin
from p178_exercises import Privileges


new_user = Admin('Carlos','Rosas')
new_user.privileges.show_privileges()