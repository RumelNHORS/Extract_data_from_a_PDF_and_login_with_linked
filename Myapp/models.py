from django.db import models
#from jsonfield.fields import JSONField


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cv_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class ScrapedDataModel(models.Model):
    json_detail = models.JSONField()

class EduDataModel(models.Model):
    json_edu = models.JSONField()