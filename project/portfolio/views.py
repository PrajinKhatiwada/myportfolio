from django.shortcuts import render, redirect,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings  # Import settings here
from django.contrib import messages
from portfolio.models import Contact, Blog,Testimonial

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def service(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fphoneno = request.POST.get('num')
        fdesc = request.POST.get('desc')
        
        # Create and save a new contact entry
        query = Contact(name=fname, email=femail, phonenumber=fphoneno, description=fdesc)
        query.save()

        # Email details
        subject = 'Contact Form Submission'
        message = f"Name: {fname}\nEmail: {femail}\nPhone: {fphoneno}\n\nMessage:\n{fdesc}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['prajinkhatiwada@gmail.com']

        # Send email
        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Your message has been sent successfully.')
        except Exception as e:
            messages.error(request, f'Error sending message: {e}')
        return redirect('contact')  # Use named URL pattern here
    
    return render(request, 'contact.html')

def blog(request):
    posts = Blog.objects.all()
    context = {"posts": posts}
    return render(request, 'handleblog.html', context)

def blog_detail(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})

def testimonials(request):
    testimonials_list = Testimonial.objects.all()  # Fetch all testimonials from the database
    return render(request, 'testimonials.html', {'testimonials': testimonials_list})