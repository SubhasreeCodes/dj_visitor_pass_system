from django.urls import path
from frontend.views import home, qr_code_view
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('qr/', qr_code_view, name='qr-code'),
    path('webcam/',views.webcam_feed, name='webcam-feed')
]