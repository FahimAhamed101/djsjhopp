from django.shortcuts import render,redirect
from django.conf import settings
from store.models import Product, ReviewRating
from news.models import News
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt
from carts.models import CartItem
import stripe
import json
from events.models import Event
from category.models import Category
def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    news = News.objects.filter(approved_post=1)
    

    context = {
        'products': products,
        'news': news,
    
       
    }
    return render(request, 'home.html', context)

def specialoffer(request):
    course = Category.objects.filter(category_name="course").first()
    products = Product.objects.filter(category=course)
    
    

    
    events = Event.objects.all()
    context = { 'events':events, 'products': products,}
    return render(request, 'specialoffer.html',context)

def contact(request):
    
    return render(request, 'contact.html')
def success(request):
    return render(request,'success.html')

def Quotation(request):
    
    return render(request, 'Quotation.html')

def Invoice(request):
    
    return render(request, 'Invoice.html')
def Receipt(request):
    
    return render(request, 'Receipt.html')
    
#cancel view
def cancel(request):
    return render(request,'cancel.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)



@csrf_exempt
def create_checkout_session(request ):
    
    current_user = request.user
    total=0
    quantity=0
    # If the cart count is less than or equal to 0, then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')

    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total)/100
    grand_total = total + tax
    totalprice= int(round(float(grand_total)*100))
 

    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                
        payment_method_types=['card'],
                mode='payment',
                line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                    'name': 't-shirt',
                    },
                      'unit_amount': totalprice,
      },
      
                'quantity': 1,
            }
        ],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})