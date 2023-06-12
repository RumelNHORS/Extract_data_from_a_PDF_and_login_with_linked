from pypdf import PdfReader
import pdfplumber
import io, os
import json
import mysql
import mysql.connector
import random
from datetime import datetime
from .models import ScrapedDataModel
from .serializers import ScrapedDataSerializer

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="resume" 
)
#print(mydb)
cursor = mydb.cursor()

reader = PdfReader("exp.pdf")
page = reader.pages[0]


def scrape_data():
    # Your scraping logic here
    with pdfplumber.open('exp.pdf') as pdf:
        scraped_data = {}
        for page in pdf.pages:
            text = page.extract_text()
            scraped_data = {text}
            return scraped_data
    # Return the scraped data
        return scraped_data

# Save the scraped data to the database
def save_to_database(data):
    serializer = ScrapedDataSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)