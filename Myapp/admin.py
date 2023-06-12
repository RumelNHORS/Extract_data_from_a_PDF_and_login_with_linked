from django.contrib import admin
#from . import models
from Myapp.models import Applicant, ScrapedDataModel, EduDataModel

# Register your models here.
admin.site.register(Applicant)
admin.site.register(ScrapedDataModel)
admin.site.register(EduDataModel)
