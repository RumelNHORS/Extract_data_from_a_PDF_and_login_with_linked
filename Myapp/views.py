import os
from Resume import settings
from django.shortcuts import render, redirect
from .forms import ApplicantForm
#from Scrape.scrape import testFn
from Scrape.scrape_data import scrape_data
from Scrape.test import extract_education
from pypdf import PdfReader
import pdfplumber

#View for api
from rest_framework.generics import ListAPIView
from Myapp.models import ScrapedDataModel, EduDataModel
from . serializers import ScrapedDataSerializer, EduSerializer


def upload_cv(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page after successful
    else:
        form = ApplicantForm()
    return render(request, 'myapp/upload_cv.html', {'form': form})

def SuccessView(request):
    print("#"*100)
    #testFn(5)
    scrape_data()
    return render(request, 'myapp/sucess.html')

def Scrape_edu(request):
    print("#"*100)
    #testFn(5)
    extract_education()
    return render(request, 'myapp/sucess.html')

class Edu_jsonView(ListAPIView):
    queryset = EduDataModel.objects.all()
    serializer_class = EduSerializer



class JsonDetailsView(ListAPIView):
    queryset = ScrapedDataModel.objects.all()
    serializer_class = ScrapedDataSerializer


################
#LinkedIn
##############
import requests
from bs4 import BeautifulSoup
from django.shortcuts import redirect
from django.http import JsonResponse

# Set your LinkedIn application credentials
CLIENT_ID = '78al3a9zifmgwi'
CLIENT_SECRET = 'pCpdSH4SiItWOmw2'
REDIRECT_URI = 'http://localhost:8000/linkedin-auth/'

def linkedin_login(request):
    # Redirect the user to the LinkedIn authorization page
    auth_url = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state=random_state_string&scope=r_liteprofile'
    return redirect(auth_url)

def linkedin_auth(request):
    # Extract the authorization code from the request
    authorization_code = request.GET.get('code')

    # Exchange the authorization code for an access token
    token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    payload = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    response = requests.post(token_url, data=payload)

    if response.status_code == 200:
        access_token = response.json()['access_token']

        # Use the access token to fetch the user's profile data
        profile_url = 'https://api.linkedin.com/v2/me?projection=(id,firstName,lastName,profilePicture(displayImage~:playableStreams))'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'api.linkedin.com',
        }
        response = requests.get(profile_url, headers=headers)

        if response.status_code == 200:
            profile_data = response.json()
            # Extract the desired profile information
            first_name = profile_data['firstName']['localized']['en_US']
            last_name = profile_data['lastName']['localized']['en_US']
            picture_url = profile_data['profilePicture']['displayImage~']['elements'][0]['identifiers'][0]['identifier']

            # Create a dictionary with the extracted data
            profile_data = {
                'first_name': first_name,
                'last_name': last_name,
                'picture_url': picture_url,
            }

            return JsonResponse(profile_data)
        else:
            return JsonResponse({'error': 'Failed to fetch LinkedIn profile data.'})
    else:
        return JsonResponse({'error': 'Failed to authenticate with LinkedIn.'})


#################################
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    return render(request, 'myapp/login.html')
@login_required
def home(request):
    return render(request, 'myapp/home.html')
