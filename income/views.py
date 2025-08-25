
from django.shortcuts import render,redirect,get_object_or_404
from .models import SERVICE,ServiceForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.views.generic import DeleteView



def Service_page(request):   
    uid=request.session.get('uid')
    if request.method=='POST':
        Customer_name=request.POST.get('Customer_name')
        Customer_fullname=request.POST.get('Customer_fullname')
        Date=request.POST.get('Date')
        Contact=request.POST.get('Contact')
        Email=request.POST.get('Email')
        Description=request.POST.get('Description')
        Address=request.POST.get('Address')
        inc=SERVICE()
        inc.Customer_name=Customer_name
        inc.Customer_fullname=Customer_fullname
        inc. Date= Date
        inc.Contact=Contact
        inc.Email=Email
        inc.Description=Description
        inc.Address=Address
        inc.user = request.user
        inc.user=User.objects.get(id=uid)
        inc.save()
        return redirect('/')
    else:
        f=ServiceForm
        context={"form":f}
        return render(request,'add_service.html',context)
    

from .models import MerModel,lamModel,PorModel,BmwModel

def bmwpage(request):
    pl = BmwModel.objects.all()
    return render(request, 'bmwpage.html', {'pl': pl})

def Mercedes_page(request):
    pl = MerModel.objects.all()
    return render(request, 'Mercedes_page.html', {'pl': pl})

def Lamborghini_page(request):
    pl = lamModel.objects.all()
    return render(request, 'Lamborghini_page.html', {'pl': pl})

def Porsche_page(request):
    pl = PorModel.objects.all()
    return render(request, 'Porsche_page.html', {'pl': pl})




from django.shortcuts import render
from .models import MerModel, lamModel, PorModel, BmwModel

def inc_search(request):
    query = request.GET.get('q')
    if query:
        mer_models = MerModel.objects.filter(model_name__icontains=query)
        lam_models = lamModel.objects.filter(model_name__icontains=query)
        por_models = PorModel.objects.filter(model_name__icontains=query)
        bmw_models = BmwModel.objects.filter(model_name__icontains=query)
        cars = list(mer_models) + list(lam_models) + list(por_models) + list(bmw_models)
    else:
        cars = list(MerModel.objects.all()) + list(lamModel.objects.all()) + list(PorModel.objects.all()) + list(BmwModel.objects.all())
    
    return render(request, 'search.html', {'cars': cars})


# servide page details customers come from database

def service_details(request):
    ser = SERVICE.objects.all()
    context={'ser':ser}
    return render(request,'service_page.html',context)

# servide page delete data function

class Ser_delete(DeleteView):
    model=SERVICE
    template_name='Ser_delete.html'
    success_url='/details'

# servide page details customers Fillter data function
def filter_by_date(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    customers = SERVICE.objects.all()

    if start_date and end_date:
        ser = customers.filter(Date__range=[start_date, end_date])
    else:
        print('thire is no data')

    return render(request, 'service_page.html', {'ser': ser})


#contact page code hire

def contact_page(request):
    return render(request,'contact_page.html')


def book_cars(request):
    query = request.GET.get('q')
    if query:
        try:
            # Assuming the query is a price range filter in the form of "min_price-max_price"
            min_price, max_price = map(int, query.split('-'))
            mer_models = MerModel.objects.filter(model_price__gte=min_price, model_price__lte=max_price)
            lam_models = lamModel.objects.filter(model_price__gte=min_price, model_price__lte=max_price)
            por_models = PorModel.objects.filter(model_price__gte=min_price, model_price__lte=max_price)
            bmw_models = BmwModel.objects.filter(model_price__gte=min_price, model_price__lte=max_price)
        except ValueError:
            # Fallback if query is not in the expected format
            mer_models = MerModel.objects.filter(model_price__icontains=query)
            lam_models = lamModel.objects.filter(model_price__icontains=query)
            por_models = PorModel.objects.filter(model_price__icontains=query)
            bmw_models = BmwModel.objects.filter(model_price__icontains=query)
    else:
        mer_models = MerModel.objects.all()
        lam_models = lamModel.objects.all()
        por_models = PorModel.objects.all()
        bmw_models = BmwModel.objects.all()

    # Combine all querysets
    cars = list(mer_models) + list(lam_models) + list(por_models) + list(bmw_models)

    # Optionally sort the combined list by price
    cars = sorted(cars, key=lambda car: car.model_price)

    return render(request, 'book_cars.html', {'pl': cars})


from django.shortcuts import render
from .models import MerModel, lamModel, PorModel, BmwModel

# def mercedes_cars(request):
#     query = request.GET.get('q')
#     if query:
#         try:
#             min_price, max_price = map(int, query.split('-'))
#             cars = MerModel.objects.filter(model_price__gte=min_price, model_price__lte=max_price)
#         except ValueError:
#             cars = MerModel.objects.filter(model_price__icontains=query)
#     else:
#         cars = MerModel.objects.all()

#     cars = sorted(cars, key=lambda car: car.model_price)
#     return render(request, 'book_cars.html', {'pl': cars})

# def lamborghini_cars(request):
#     query = request.GET.get('q')
#     if query:
#         try:
#             min_price, max_price = map(int, query.split('-'))
#             cars = lamModel.objects.filter(model_price__gte=min_price, model_price__lte=max_price)
#         except ValueError:
#             cars = lamModel.objects.filter(model_price__icontains=query)
#     else:
#         cars = lamModel.objects.all()

#     cars = sorted(cars, key=lambda car: car.model_price)
#     return render(request, 'lamborghini_cars.html', {'cars': cars})

# def porsche_cars(request):
#     query = request.GET.get('q')
#     if query:
#         try:
#             min_price, max_price = map(int, query.split('-'))
#             cars = PorModel.objects.filter(model_price__gte=min_price, model_price__lte=max_price)
#         except ValueError:
#             cars = PorModel.objects.filter(model_price__icontains=query)
#     else:
#         cars = PorModel.objects.all()

#     cars = sorted(cars, key=lambda car: car.model_price)
#     return render(request, 'porsche_cars.html', {'cars': cars})

# def bmw_cars(request):
#     query = request.GET.get('q')
#     if query:
#         try:
#             min_price, max_price = map(int, query.split('-'))
#             cars = BmwModel.objects.filter(model_price__gte=min_price, model_price__lte=max_price)
#         except ValueError:
#             cars = BmwModel.objects.filter(model_price__icontains=query)
#     else:
#         cars = BmwModel.objects.all()

#     cars = sorted(cars, key=lambda car: car.model_price)
#     return render(request, 'bmw_cars.html', {'pl': cars})




def all_cars(request):
    query = request.GET.get('q')
    if query:
        mer_models = MerModel.objects.all()
        lam_models = lamModel.objects.all()
        por_models = PorModel.objects.all()
        bmw_models = BmwModel.objects.all()
        cars = list(mer_models) + list(lam_models) + list(por_models) + list(bmw_models)
    else:
        cars = list(MerModel.objects.all()) + list(lamModel.objects.all()) + list(PorModel.objects.all()) + list(BmwModel.objects.all())
    
    return render(request, 'book_cars.html', {'pl': cars})


def Sports_cars(request):
    query = request.GET.get('q')
    if query:
        lam_models = lamModel.objects.all()
        por_models = PorModel.objects.all()
        cars = list(lam_models) + list(por_models) 
    else:
        cars =  list(lamModel.objects.all()) + list(PorModel.objects.all()) 
    
    return render(request, 'book_cars.html', {'pl': cars})


def comfort_cars(request):
    com=BmwModel.objects.all()
    context={'pl':com}
    return render(request,'book_cars.html',context)

def luxury_cars(request):
    com=MerModel.objects.all()
    context={'pl':com}
    return render(request,'book_cars.html',context)







# thise data while save database thise is a method
# def bookform(request):
#     uid = request.session.get('uid')
#     car_id = request.GET.get('model_id')

#     if not uid:
#         return render(request, 'error_template.html', {'error': 'User not logged in or session expired'})

#     user = get_object_or_404(User, id=uid)

#     # Initialize car_model to None
#     car_model = None

#     # Check each model sequentially until we find a match
#     if MerModel.objects.filter(id=car_id).exists():
#         car_model = MerModel.objects.get(id=car_id)

   

#     # If no car model is found, show an error
#     if car_model is None:
#         return render(request, 'error_template.html', {'error': 'No car model found with the provided ID.'})

#     if request.method == 'POST':
#         # Handle form submission here
#         return redirect('/')

#     # Pass the car model to the template
#     return render(request, 'bookform.html', {'pl': car_model})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import BookCars, MerModel  # Assuming MerModel is one of your car models
from django.contrib.auth.decorators import login_required

@login_required
def bookform(request):
    uid = request.session.get('uid')
    car_id = request.GET.get('model_id')

    if not uid:
        return render(request, 'error_template.html', {'error': 'User not logged in or session expired'})

    user = get_object_or_404(User, id=uid)

    # Initialize car_model to None
    car_model = None

    # Check if the car model exists
    if MerModel.objects.filter(id=car_id).exists():
        car_model = MerModel.objects.get(id=car_id)

    # If no car model is found, show an error
    if car_model is None:
        return render(request, 'error_template.html', {'error': 'No car model found with the provided ID.'})

    if request.method == 'POST':
        # Get data from the form
        Your_name = request.POST.get('Your_name')
        Your_fullname = request.POST.get('Your_fullname')
        Contact = request.POST.get('Contact')
        Email = request.POST.get('Email')
        Address = request.POST.get('Address')
        img = car_model.img  # Assuming you want to save the car image with the booking

        # Create and save the booking
        book_car = BookCars(
            Your_name=Your_name,
            Your_fullname=Your_fullname,
            Contact=Contact,
            Email=Email,
            Address=Address,
            img=img,
            user=user
        )
        book_car.save()

        return redirect('/list_booking_Cus')  # Redirect to the home page or a success page
    elif 'list_booking_Cus' in request.POST:
            # Handle the request to list all bookings
            return redirect('/')

    # Pass the car model to the template
    return render(request, 'bookform.html', {'pl': car_model})


 
def list_booking_Cus(request):
    # Filter BookCars where payment has not been made or no payment info is available
    li = BookCars.objects.filter(payment__isnull=True) | BookCars.objects.filter(payment__paid=False)
    context = {'li': li}
    return render(request, 'list_booking_Cus.html', context)

# def list_booking_Cus(request):
#     # Filter out customers who have already paid
#     li = BookCars.objects.all() 
#     context = {'li': li}
#     return render(request, 'list_booking_Cus.html', context)
# def bookformbmw(request):
#     uid = request.session.get('uid')
#     car_id = request.GET.get('modell_id')

#     if not uid:
#         return render(request, 'error_template.html', {'error': 'User not logged in or session expired'})

#     user = get_object_or_404(User, id=uid)

#     # Initialize car_model to None
#     car_model = None

#     # Check each model sequentially until we find a match
#     if BmwModel.objects.filter(id=car_id).exists():
#         car_model = BmwModel.objects.get(id=car_id)

   

#     # If no car model is found, show an error
#     if car_model is None:
#         return render(request, 'error_template.html', {'error': 'No car model found with the provided ID.'})

#     if request.method == 'POST':
#         # Handle form submission here
#         return redirect('/')

#     # Pass the car model to the template
#     return render(request, 'bmw_cars.html', {'pl': car_model})


# from django.shortcuts import render, redirect
# from .models import BookCars  # Import the BookCars model
# from django.contrib.auth.models import User  # Import the User model


# import razorpay
# from .models import PayMent

# def paynow(request):
#     if request.method=='POST':
#         name=request.POST.get("name")
#         amount=request.POST.get("amount")
#         client= razorpay.client(auth=("rzp_test_fUM1KpcBRriccx", "3vQiq6Uhi3kHAzqTPrefXqYN"))
#         payment = client.order.create({'amount':amount, 'currency':'INR','Payment_capture':'1'})
#         print(payment)
#         payment=PayMent(name=name,amount=amount,payment_id=payment['id'])

#     return render(request,'list_booking_Cus.html')

# def paynow1(request):
#     if request.method=="POST":
#         a= request.POST
#         print(a)
#     return render(request,'list_booking_Cus.html')


# views.py

import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from .models import PayMent

def create_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        
        # Debugging information
        print(f"Name: {name}")
        print(f"Amount: {amount}")

        if not name or not amount:
            return render(request, 'list_booking_Cus.html', {'error': 'Name and amount are required.'})
        
        amount_in_paise = int(float(amount) * 100)  # Convert amount to paise

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        order = client.order.create({
            'amount': amount_in_paise,
            'currency': 'INR',
            'payment_capture': '1'
        })

        # Create a PayMent instance
        payment = PayMent(
            name=name,
            amount=amount,
            payment_id=order['id'],
            paid=False
        )
        payment.save()

        context = {
            'order_id': order['id'],
            'amount': amount_in_paise,
            'razorpay_key': settings.RAZORPAY_KEY_ID
        }
        return render(request, 'payment/payment.html', context)
    
    return render(request, 'list_booking_Cus.html')



# views.py

from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import razorpay

@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        
        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            payment = PayMent.objects.get(payment_id=params_dict['razorpay_order_id'])
            payment.payment_id = params_dict['razorpay_payment_id']
            payment.paid = True
            payment.save()

            return render(request, 'payment/success.html')

        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest()

    return HttpResponseBadRequest()


def fill_form(request):
    return render(request,'payment/payment.html')