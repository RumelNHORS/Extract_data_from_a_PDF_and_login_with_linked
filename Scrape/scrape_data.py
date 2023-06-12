from pypdf import PdfReader
import pdfplumber
import io, os
import json
# import mysql
# import mysql.connector
import random
from django.conf import settings
#from datetime import datetime
from Myapp.models import ScrapedDataModel
#import Myapp
#from Myapp.serializers import ScrapedDataSerializer

# To indecate the Database of this file
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="1234",
#   database="resume" 
# )
#print(mydb)
# cursor = mydb.cursor()

#For convert the python Data as JSONdata
class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


# Scrape Data and save the data to the Database
def scrape_data():
    file_path = os.path.join(settings.MEDIA_ROOT, 'exp.pdf')
    reader = PdfReader(file_path)
    #print(f"There are {len(reader.pages)} Pages")
    # Your scraping logic here
    with pdfplumber.open(file_path) as pdf:
        scraped_data = {}
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            scraped_data = lines
            # convert Python Dictonary Data To json data
            json_str = json.dumps(scraped_data, cls=SetEncoder, indent=4)
            json_detail = json_str
            # Sava the json data to the database
            pdf_data = ScrapedDataModel(json_detail=json_detail)
            pdf_data.save()
            print(pdf_data)
            return pdf_data
    # Return the scraped json data
        return pdf_data
    

