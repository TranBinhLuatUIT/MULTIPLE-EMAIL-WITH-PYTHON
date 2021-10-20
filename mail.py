import smtplib, ssl, email
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
 

port = 465 


def create_mail(subject, fr, to, body, attachment=None):
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = fr
    message["To"] = to
    message.attach(MIMEText(body, "HTML"))
    
    if(attachment != None):
        message.attach(attachment)
    
    return message.as_string()
    
def get_attachment(filepath, filename):
    # Open PDF file in binary mode
    with open(filepath, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        
    encoders.encode_base64(part)
    
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    
    return part


def send_mail(SUBJECT,FROM ,BODY, sheet, mail_col, args, attach_path_col=None, attach_name_col=None):
    
    your_mail = input("Your mail: ")
    password = input("password: ")
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(your_mail,password)
        
        if (attach_path_col != None and attach_name_col!=None):

            for row in sheet.iterrows():
                content = BODY.format(*row[1][args].values)
                TO = row[1][mail_col]
                attach = get_attachment(row[1][attach_path_col], row[1][attach_name_col])
                mail_content = create_mail(SUBJECT, FROM, TO, content, attach)
                
                try:
                    server.sendmail(your_mail, TO, mail_content)
                except:
                    print("Fail when send email to", TO)
        else:
            print("Send mail without attachment, right? ")
            option = input("YES or NO: ")
            while(1):
                if(option == 'YES'):
                    break
                elif(option == "NO"):
                    return
                else:
                    print("Invalid option")
                    option = input("YES or NO: ")
                    
            for row in sheet.iterrows():
                content = BODY.format(*row[1][args].values)
                TO = row[1][mail_col]
                mail_content = create_mail(SUBJECT, FROM, TO, content)
                              
                try:
                    server.sendmail(your_mail, TO, mail_content)
                except:
                    print("Fail when send email to", TO)
    

def valid_col(SHEET, to_col, fill_content_col):
    if (to_col in SHEET.columns):
        for i in fill_content_col:
            if (i not in SHEET.columns):
                print(i, "column does not exist, please check again")
                return False
        return True
    else:
        print("Invalid mail column, please check again. ")
        return False
    