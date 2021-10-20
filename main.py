from mail import *
import pandas as pd

#your excel path here
file_excel_path = "DSach.xlsx"

SHEET = pd.read_excel(file_excel_path)
FROM = "TBL"      
SUBJECT = "TEST MAI"    

with open('template.txt', encoding='utf-8') as f:
    BODY = f.read()


CONTENT_COL = ['gen', 'name']  #put value of columns in {} of BODY 
TO_COL = 'mail'  #Name of mail column in your sheet
ATTACHMENT_PATH_COL = None #attachments path column 
ATTACHMENT_NAME_COL = None #attachments name column 


if(valid_col(SHEET ,TO_COL, CONTENT_COL) == True):
    send_mail(SUBJECT, FROM, BODY, SHEET, TO_COL, CONTENT_COL, ATTACHMENT_PATH_COL, ATTACHMENT_NAME_COL)


