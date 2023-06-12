from pypdf import PdfReader
import pdfplumber
import io, os
#from Resume import settings
import json


reader = PdfReader("exp.pdf")

# Get the first page (index 0) 
page = reader.pages[0]
#Get all the page of this pdrf
#page = reader.pages['all']
# Use extract_text() to get the text of the page
#print(page.extract_text())


with open('exp.pdf', 'rb') as file:
        # Create a PDF reader object
        reader = PdfReader(file)
        
        # Extract text from each page of the PDF
        num_pages = len(reader.pages)
        skill_section_found = False
        skills = []

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            
            # Look for the skill section header and extract the skills
            if "Skills" in text:
                skill_section_found = True
                # Extract the lines following the header as skills
                lines = text.split('\n')
                for line in lines:
                    if line.strip().lower() == "skills":
                        continue  # Skip the header line
                    if line.strip():  # Check if the line is not empty
                        skills.append(line.strip())
            elif skill_section_found:
                break  # Exit loop if the skill section has already been found and no more skills are present
                
    #return skills

# Provide the path to your CV PDF file
cv_pdf_path = 'exp.pdf'

# Extract the skills from the CV PDF
cv_skills = cv_pdf_path

# Print the extracted skills
for skill in cv_skills:
    print(skill)


#Scrape Data(Image) From a PDF File
# for img in page.images:
#     with open(img.name, "wb") as fp:
#         fp.write(img.data)

# Go through every page and get the text
"""for i in range(len(reader.pages)):
  page = reader.pages[i]
  print(page.extract_text())"""



with pdfplumber.open('exp.pdf') as pdf:
     # Create an empty dictionary to store the scraped data
     scraped_data = {}
     # iterate over each page
     for page in pdf.pages:
         # extract text
         text = page.extract_text()
         #print(text)
#         #Extract Table
#         #table = page.extract_tables()
         scraped_data = {text}
         #print(scraped_data)
         json_data = json.dumps(list(scraped_data))
         #print(json_data)
         #print(type(json_data))
#         #print(text)
#         #Extract Table
#         #print(table)

#         # Store the scraped data in the dictionary
#         #scraped_data[page.page_number] = text


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

    scraped_data = {text}
json_str = json.dumps(scraped_data, cls=SetEncoder)
#print(json_str) # 👉️ '["b", "c", "a", "d"]'

import mysql
import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="1234",
#   database="resume" 
# )
# print(mydb)
# cursor = mydb.cursor()


"""def testFn(number):
    print('#'*10,number,'#'*10)
    file_path = os.path.join(settings.MEDIA_ROOT, 'exp.pdf')
    reader = PdfReader(file_path)
    print(f"There are {len(reader.pages)} Pages")
    print('#'*10,number,'#'*10)"""

    #New
#    with pdfplumber.open('exp.pdf') as pdf:
#        scraped_data = {}
#        for page in pdf.pages:
#         # extract text
#         text = page.extract_text()
#         scraped_data = {text}
#         print(scraped_data)





