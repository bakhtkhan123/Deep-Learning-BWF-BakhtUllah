# Exercise 8.15
def make_pizza(size,*toppings):
    for pizza in toppings:
        print('-',pizza.title())
make_pizza(13,'pepproni')
make_pizza(16,'pepproni','mashrooms','cheeses')