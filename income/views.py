
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







# from django.shortcuts import render, redirect, get_object_or_404
# from .models import BookCars, lamModel  # Import your car model
# from django.contrib.auth.models import User
def bookform(request):
    uid = request.session.get('uid')
    car_id = request.GET.get('model_id')

    if not uid:
        return render(request, 'error_template.html', {'error': 'User not logged in or session expired'})

    user = get_object_or_404(User, id=uid)

    # Initialize car_model to None
    car_model = None

    # Check each model sequentially until we find a match
    if MerModel.objects.filter(id=car_id).exists():
        car_model = MerModel.objects.get(id=car_id)

   

    # If no car model is found, show an error
    if car_model is None:
        return render(request, 'error_template.html', {'error': 'No car model found with the provided ID.'})

    if request.method == 'POST':
        # Handle form submission here
        return redirect('/')

    # Pass the car model to the template
    return render(request, 'bookform.html', {'pl': car_model})




