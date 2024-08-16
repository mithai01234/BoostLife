from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomAuthenticationForm  # Assuming you have a custom authentication form
AUTH_USER_MODEL = 'backendlogin.BackendCustomUser'
from django.utils import timezone


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log the user in
                login(request, user)
                # Check if the user is staff after login
                if not user.is_staff:
                    return redirect('backend/login')  # or some other page

                next_url = request.GET.get('next', reverse('backend/dashboard'))
                return redirect(next_url)
            else:
                return render(request, 'backend/login.html', {'form': form, 'error': 'Invalid login credentials'})
        else:
            return render(request, 'backend/login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = CustomAuthenticationForm()

    return render(request, 'backend/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('backend/login')
@login_required(login_url='backend/login')
def dashboard(request):
    if not request.user.is_staff:
        return redirect('backend/login')
    return render(request, 'backend/dashboard.html')

from registration.models import CustomUser,Otp
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import random

def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email).first()  # Use User model
        if user and user.is_staff:
            # Generate OTP
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

            # Send OTP email
            subject = 'OTP for Password Change'
            message = f'Your OTP for password change is: {otp}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            # Store OTP and its creation time in database
            otp_obj, created = Otp.objects.get_or_create(user=user)
            otp_obj.otp = otp
            otp_obj.otp_created_at = timezone.now()
            otp_obj.save()

            return redirect('verify_otp')
        else:
            error = "Email does not exist or user is not authorized."
            return render(request, 'send_otp.html', {'error': error})
    return render(request, 'send_otp.html')

def verify_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = CustomUser.objects.filter(email=email, is_staff=True).first()
        if user:
            # Generate OTP
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

            # Send OTP email
            subject = 'OTP for Email Verification'
            message = f'Your OTP for email verification is: {otp}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            # Store OTP and its creation time in database
            otp_obj, created = Otp.objects.get_or_create(user=user)
            otp_obj.otp = otp
            otp_obj.otp_created_at = timezone.now()
            otp_obj.save()

            # Store email in session
            request.session['verified_email'] = email

            return redirect('verify_otp')
        else:
            error = "Email does not exist or user is not authorized."
            return render(request, 'backend/verify_email.html', {'error': error})
    return render(request, 'backend/verify_email.html')
from django.contrib import messages

def verify_otp(request):
    email = request.session.get('verified_email')
    if not email:
        # If email is not found in session, redirect to the verify_email page
        messages.error(request, 'Please verify your email first.')
        return redirect('verify_email')

    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        user = CustomUser.objects.filter(email=email).first()
        if user and user.is_staff:
            otp_obj = Otp.objects.filter(user=user).first()
            if otp_obj:
                # Check if OTP matches
                if otp_obj.otp == otp_entered:
                    # Check if OTP is expired (5 minutes expiry)
                    if (timezone.now() - otp_obj.otp_created_at).total_seconds() > 300:
                        return render(request, 'backend/verify_otp.html', {'email': email, 'error': 'OTP has expired. Please request a new OTP.'})
                    else:
                        return redirect('change_password')
                else:
                    return render(request, 'backend/verify_otp.html', {'email': email, 'error': 'Invalid OTP. Please enter the correct OTP.'})
            else:
                return render(request, 'backend/verify_otp.html', {'email': email, 'error': 'OTP not found. Please request a new OTP.'})
        else:
            error = "Otp Does Not Match!!"
            return render(request, 'backend/verify_otp.html', {'error': error})
    return render(request, 'backend/verify_otp.html', {'email': email})
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        email = request.session.get('verified_email')
        if not email:
            # If email is not found in session, redirect to the verify_email page
            messages.error(request, 'Please verify your email first.')
            return redirect('change_password')

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'backend/change_password.html')

        user = CustomUser.objects.filter(email=email).first()
        if user:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Keep the user logged in after password change
            messages.success(request, "Password changed successfully.")
            return redirect('backend/login')
        else:
            messages.error(request, "User not found.")
            return redirect('verify_email')
    return render(request, 'backend/change_password.html')
