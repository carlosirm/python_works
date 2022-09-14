"""9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working
properly."""

from p171_exercises import Restaurant

restaurant = Restaurant('One Town','Chinese')
restaurant.print_customers_number()

restaurant.number_served = 12
restaurant.print_customers_number()

restaurant.set_number_served(20)
restaurant.print_customers_number()

restaurant.increment_number_served(10)
restaurant.print_customers_number()