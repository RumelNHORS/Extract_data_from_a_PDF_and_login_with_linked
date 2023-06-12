
# ######################
# # Scrape All data
# ######################
# from pdfminer.high_level import extract_text

# def extract_text_from_pdf(pdf_path):
#     return extract_text(pdf_path)

# if __name__ == '__main__':
#     print(extract_text_from_pdf('exp.pdf'))

# ######################
# # End Scrape All data
# ######################

# import docx2txt
# import nltk
 
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

 
 
# def extract_text_from_docx(pdf_path):
#     txt = docx2txt.process(pdf_path)
#     if txt:
#         return txt.replace('\t', ' ')
#     return None
 
 
# def extract_names(txt):
#     person_names = [] 
#     for sent in nltk.sent_tokenize(txt):
#         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
#             if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
#                 person_names.append(
#                     ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
#                 )
 
#     return person_names
 
 
# if __name__ == '__main__':
#     text = extract_text_from_pdf('exp.pdf')
#     names = extract_names(text)
 
#     if names:
#         print(names[0])  # noqa: T001


# ###########################
# # Start Phone number Section
# ###########################
# import re
# import subprocess  # noqa: S404
 
# PHONE_REG = re.compile(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]")
 
 
# def pdf_to_text_catdoc(file_path):
#     try:
#         process = subprocess.Popen(  # noqa: S607,S603
#             ['catdoc', '-w', file_path],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             universal_newlines=True,
#         )
#     except (
#         FileNotFoundError,
#         ValueError,
#         subprocess.TimeoutExpired,
#         subprocess.SubprocessError,
#     ) as err:
#         return (None, str(err))
#     else:
#         stdout, stderr = process.communicate()
 
#     return (stdout.strip(), stderr.strip())
 
 
# def extract_phone_number(resume_text):
#     phone = re.findall(PHONE_REG, resume_text)
 
#     if phone:
#         number = ''.join(phone[0])
 
#         if resume_text.find(number) >= 0 and len(number) <= 16:
#             return number
#     return None
 
 
# if __name__ == '__main__':
#     text = pdf_to_text_catdoc('exp.pdf')
#     phone_number = extract_phone_number(text)
#     print(phone_number)  # noqa: T001
# ###########################
# #End Phone number Section
# ###########################


# ###########################
# # Start Email Section
# ###########################

# import re
# from pdfminer.high_level import extract_text
 
# EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
 
 
# def extract_text_from_pdf(pdf_path):
#     return extract_text(pdf_path)
 
 
# def extract_emails(resume_text):
#     return re.findall(EMAIL_REG, resume_text)
 
 
# if __name__ == '__main__':
#     text = extract_text_from_pdf('exp.pdf')
#     emails = extract_emails(text)
 
#     if emails:
#         print(emails[0])
# ###########################
# #End Email Section
# ###########################
 
# import re
# import subprocess  # noqa: S404
 
# PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
 
 
# def pdf_to_text_catdoc(file_path):
#     try:
#         process = subprocess.Popen(  # noqa: S607,S603
#             ['catdoc', '-w', file_path],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             universal_newlines=True,
#         )
#     except (
#         FileNotFoundError,
#         ValueError,
#         subprocess.TimeoutExpired,
#         subprocess.SubprocessError,
#     ) as err:
#         return (None, str(err))
#     else:
#         stdout, stderr = process.communicate()
 
#     return (stdout.strip(), stderr.strip())
 
 
# def extract_phone_number(resume_text):
#     phone = re.findall(PHONE_REG, resume_text)
 
#     if phone:
#         number = ''.join(phone[0])
 
#         if resume_text.find(number) >= 0 and len(number) <= 16:
#             return number
#     return None
 
 
# if __name__ == '__main__':
#     text = pdf_to_text_catdoc('exp.pdf')
#     phone_number = extract_phone_number(text)
 
#     print(phone_number)  # noqa: T001


import re
 
from pdfminer.high_level import extract_text
 
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
 
 
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)
 
 
def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)
 
 
if __name__ == '__main__':
    text = extract_text_from_pdf('exp.pdf')
    emails = extract_emails(text)
 
    if emails:
        print(emails[0])  # noqa: T001

