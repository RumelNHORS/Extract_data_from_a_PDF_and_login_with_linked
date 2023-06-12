from django.urls import path
from .views import upload_cv, SuccessView
from Myapp import views

urlpatterns = [
    path('', upload_cv, name='upload_cv'),
    path('success/', SuccessView, name='success'),

    #API
    path('api/', views.JsonDetailsView.as_view(), name='api'),
    path('api/edu', views.Edu_jsonView.as_view(), name='api'),

    path('linkedin/', views.linkedin_auth, name='api'),
    path('login/', views.linkedin_login, name='api'),

]
    