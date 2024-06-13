from .cart import Cart

# create context processor so our cart can work on all pages of the website

def cart(request):
    # return the default data fromour cart
    return {'cart' : Cart(request)}
