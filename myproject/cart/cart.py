from timestore.models import Product




class Cart:


    def __init__(self, request):


        # Get the current user's session
        self.session = request.session


        # Get the cart from the session
        cart = self.session.get('session_key')


        # If cart does not exist, create an empty cart
        if cart is None:
            cart = self.session['session_key'] = {}


        # Store cart in self.cart
        self.cart = cart


    def add(self, product, quantity):


        # Convert product ID to string
        product_id = str(product.id)


        # Convert quantity to integer
        product_qty = int(quantity)


        # Add product if it does not already exist
        if product_id not in self.cart:
            self.cart[product_id] = product_qty


        # Tell Django that session data has changed
        self.session.modified = True


    def update(self, product, quantity):


        # Convert product ID to string
        product_id = str(product)


        # Convert quantity to integer
        product_qty = int(quantity)


        # Update quantity
        self.cart[product_id] = product_qty


        # Tell Django that session has changed
        self.session.modified = True


    def delete(self, product):


        # Convert product ID to string
        product_id = str(product)


        # Check whether product exists
        if product_id in self.cart:


            # Remove product
            del self.cart[product_id]


        # Tell Django that session has changed
        self.session.modified = True


    def __len__(self):


        # Return number of different products
        return len(self.cart)


    def get_prods(self):


        # Get product IDs from cart
        product_ids = self.cart.keys()


        # Get products from database
        products = Product.objects.filter(id__in=product_ids)


        # Return products
        return products


    def get_quants(self):


        # Return cart dictionary
        return self.cart


