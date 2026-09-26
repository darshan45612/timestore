from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from timestore.models import Product


from .cart import Cart




def cart_summary(request):


    cart = Cart(request)


    cart_products = cart.get_prods()


    quantities = cart.get_quants()


    return render(
        request,
        'cart_summary.html',
        {
            'cart_products': cart_products,
            'quantities': quantities,
        }
    )




def cart_add(request):


    cart = Cart(request)


    if request.method == 'POST':


        product_id = int(request.POST.get('product_id'))


        product_qty = int(request.POST.get('product_qty'))


        product = get_object_or_404(
            Product,
            id=product_id
        )


        cart.add(
            product=product,
            quantity=product_qty
        )


        cart_quantity = len(cart)


        return JsonResponse({
            'qty': cart_quantity
        })


    return JsonResponse({
        'error': 'Invalid request'
    }, status=400)




def cart_update(request):


    cart = Cart(request)


    if request.method == 'POST':


        product_id = int(request.POST.get('product_id'))


        product_qty = int(request.POST.get('product_qty'))


        cart.update(
            product=product_id,
            quantity=product_qty
        )


        return JsonResponse({
            'qty': product_qty
        })


    return JsonResponse({
        'error': 'Invalid request'
    }, status=400)





def cart_delete(request):


    cart = Cart(request)


    if request.method == 'POST':


        product_id = int(request.POST.get('product_id'))


        cart.delete(
            product=product_id
        )


        return JsonResponse({
            'product': product_id
        })


    return JsonResponse({
        'error': 'Invalid request'
    }, status=400)
