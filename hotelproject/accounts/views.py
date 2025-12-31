import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import UserProfile


# =========================
# EMAIL OTP (TERMINAL MODE)
# =========================

def login_email(request):
    if request.method == "POST":
        email = request.POST.get('email')
        otp = random.randint(1000, 9999)

        request.session['otp'] = otp
        request.session['email'] = email

        send_mail(
            subject='Your Login OTP',
            message=f'Your OTP is {otp}',
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )

        return redirect('verify_email')

    return render(request, 'accounts/email_login.html')


def verify_email_otp(request):
    if request.method == "POST":
        user_otp = request.POST.get('otp')
        real_otp = request.session.get('otp')
        email = request.session.get('email')

        if str(real_otp) == str(user_otp):
            user, created = UserProfile.objects.get_or_create(email=email)
            request.session['user_id'] = user.id
            return redirect('/')   # menu page
        else:
            return render(request, 'accounts/email_verify.html', {
                'error': 'Invalid OTP'
            })

    return render(request, 'accounts/email_verify.html')
