from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import LoginForm
from django.contrib.auth.models import User




# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'nav.html')


# def add_user(request):
#     if request.method=='POST':
#         f=UserCreationForm(request.POST)
#         f.save()
#         return redirect('/login')
#     else:
#         f=UserCreationForm
#         context={'form':f}
#         return render(request,'adduser.html',context)
    

# rajestration form
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new page or login after successful registration
            return redirect('/login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

    
# Create your LoginForm here.


def loginform(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            request.session['uid'] = user.id
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('/login')
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login.html', context)

def logout_v(request):
    logout(request)
    return redirect('/login')

def base2(request):
    return render(request,'header2.html')




from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Ensure you import the User model

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get the email from the POST request

        # Check if a user with the given email exists
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)  # Correct the user retrieval

            # Prepare the email content
            current_site = get_current_site(request)
            mail_subject = "Please reset your password"
            message = render_to_string('account/reset_password_email.html', {
                'user': user,
                'domain': current_site.domain,  # Use domain instead of the entire current_site object
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # Use 'pk' for the user ID
                'token': default_token_generator.make_token(user),
            })

            # Send the email
            send_email = EmailMessage(mail_subject, message, to=[email])
            send_email.send()

            # Add success message and redirect to login page
            messages.success(request, 'Password reset email sent successfully.')
            return redirect('/login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('/forgotPassword')

    return render(request, 'account/forgotpassword.html')


from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User

def restpassword_validate(request, uidb64, token):
    try:
        # Decode uidb64 to get the user ID
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # Store uid in session for password reset view
        request.session['uid'] = uid
        return redirect('/resetpassword')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('/login')

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render

def resetpassword(request):
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            if uid:
                try:
                    user = User.objects.get(pk=uid)
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'Password reset successfully')
                    return redirect('/login')
                except User.DoesNotExist:
                    messages.error(request, 'User not found')
            else:
                messages.error(request, 'Session expired or invalid request')
            return redirect('/resetpassword')  # Redirect back to reset password page
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('/resetpassword')  # Redirect back to reset password page

    return render(request, 'account/resetpassword.html')

    