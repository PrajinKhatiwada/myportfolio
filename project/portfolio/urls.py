from portfolio import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
