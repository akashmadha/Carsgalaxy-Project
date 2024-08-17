from django.shortcuts import render, redirect
from .models import TestDrive, ServiceForm,chousejender, ModelsChouse, ChouseCentre
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render, redirect, get_object_or_404


def testdrive(request):
    uid = request.session.get('uid')
    
    if request.method == 'POST':
        if uid is None:
            # Handle the case where uid is not set in the session
            return render(request, 'error_template.html', {'error': 'User not logged in or session expired'})

        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            return render(request, 'error_template.html', {'error': 'User not found'})

        # Fetch data from POST request
        Customer_name = request.POST.get('Customer_name')
        Customer_fullname = request.POST.get('Customer_fullname')
        Date = request.POST.get('Date')
        Contact = request.POST.get('Contact')
        Email = request.POST.get('Email')
        Description = request.POST.get('Description')
        Address = request.POST.get('Address')
        Chouse_jender_id = request.POST.get('Chouse_jender')
        Models_chouse_id = request.POST.get('Models_chouse')
        Model_centers_id = request.POST.get('Model_centers')

        try:
            # Fetch related objects with error handling
            chouse_jender = get_object_or_404(chousejender, id=Chouse_jender_id)
            models_chouse = get_object_or_404(ModelsChouse, id=Models_chouse_id)
            model_centers = get_object_or_404(ChouseCentre, id=Model_centers_id)
            
            # Create and save the TestDrive instance
            inc = TestDrive(
                Customer_name=Customer_name,
                Customer_fullname=Customer_fullname,
                Date=Date,
                Contact=Contact,
                Email=Email,
                Description=Description,
                Address=Address,
                Chouse_jender=chouse_jender,
                Models_chouse=models_chouse,
                Model_centers=model_centers,
                user=user
            )
            inc.save()
            return redirect('/')
        except ObjectDoesNotExist as e:
            # Handle cases where the gender, car model, or center doesn't exist
            return render(request, 'error_template.html', {'error': f'Invalid selection: {str(e)}'})
        
    else:
        f = ServiceForm()
        context = {"form": f}
        return render(request, 'test_drive.html', context)



