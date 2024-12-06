from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import people ,  comic
from django.http import HttpResponse ,JsonResponse
from django.forms import forms
from razorpay import Client
from resume.settings import RAZORPAY_API_KEY , RAZORPAY_API_SECRET_KEY
def index(request):
    return render(request , 'index.html')
# Create your views here.

# def register(request):
#     if request.method == 'POST':

#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         email = request.POST['email']
#         value = request.POST['value']

#         if firstname == lastname:
#             messages.info(request ,"bro your equal from front and back, how even it can be possible ")
#             return redirect('register')

#         else:
#             User.objects.filter(email = email).exists()
#             messages.info(request ,"this email has been used earlier , i hope this belongs to you only")
#             User.objects.create_user(firstname = firstname , lastname = lastname , email = email , value = value)
#             User.save()
#     else:
#         return render(request , 'index.html')
            
def register(request):
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        value = request.POST['value']
        if not firstname:
            messages.info(request ,"First name is required ")
            return redirect('register')
        
        elif firstname == lastname:
            messages.info(request ,"bro your equal from front and back, how even it can be possible ")
            return redirect('register')
            
        
        if people.objects.filter(email = email ,firstname = firstname , lastname = lastname).exists() :
            messages.info(request ,f"Welcome Back, {firstname}! ")
            
            
        else:
            user =people.objects.create(firstname = firstname , lastname = lastname , email = email , value = value)
            messages.info(request ,f"Thank you for registering, {firstname}!")
            # people.save()
        
        return render(request ,"index.html")
    else:
        return render(request ,'index.html')

    # if forms.is_valid():
    #     return render(request ,"index.html",{JsonResponse({'success': True})}) 
    # else:
    #             return render(request ,"index.html",{JsonResponse({'success': False, 'errors': forms.errors})})

def real_state(request):
    context = {}  
    return render(request, 'real states prize pridiction.html', context)

        
def movie_app(request):
    context = {}  
    return render(request, 'movie app.html', context)

def movie_live(request):
    context = {}  
    return render(request, 'movie live.html', context)

def comics(request):
    products = comic.objects.all()

    # Set your Razorpay API keys securely (consider environment variables)
    # razorpay_client = Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

    context = {'products': products, 'razorpay_key':RAZORPAY_API_KEY}
    return render(request, 'product.html', context)


        
def payment(request, product_id):
    if request.method == 'POST':
        try:
            # Fetch the product based on product_id
            product = comic.objects.get(pk=product_id)
            razorpay_client = Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
            # Create Razorpay order
            order_data = {
                'amount': int(product.price * 100),  # Convert to paise
                'currency': 'INR',
                'receipt': 'receipt_123',  # Replace with a unique identifier
                'payment_capture': 1  # Capture payment automatically
            }
            response = razorpay_client.order.create(data=order_data)
            order_id = response.get('id')

            # Prepare data for Razorpay checkout (pass product details)
            context = {
                'product_id': product_id,
                'product_image': product.image,
                'order_id': order_id,
                'product_name': product.name,
                'product_price': product.price,  # Keep for display
                'razorpay_key': RAZORPAY_API_KEY
            }
            return render(request, 'payment.html', context)
        except comic.DoesNotExist:
            return render(request, 'payment.html', {'message': 'Product not found'})

    return render(request, 'payment.html', {'message': 'Invalid request method'})


    





def payment_failure(request):
    
    product_id = request.GET.get('product_id')
    
    product = comic.objects.get(pk=product_id)
    context = {
        'product_image': product.image,
        'product_name': product.name,
    }
    return render(request, 'payment_failure.html',context)

def payment_success(request):


    product_id = request.GET.get('product_id')
    product = comic.objects.get(pk=product_id)
    # Handle missing product ID gracefully
    error_message = "Missing product ID in payment success request."
    context = {
        'product_image': product.image,
        'product_name': product.name,
    }

    return render(request, 'payment_success.html', context)