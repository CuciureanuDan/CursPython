
import smtplib 
from smtplib import SMTPAuthenticationError, SMTPException
import ssl
from email.message import EmailMessage
from configparser import ConfigParser

# Fisierul 'EmailData.ini' contine informatii referitoare la adresa de email utilizata pentru trimiterea mesajelor
# Contine sectiunea credentials cu cheile email si password

def send_email(email_receiver, product, price):

    config = ConfigParser()

    # Fiindca fisierul trebuie EmailData.ini trebuie generat de utilizator incercam sa gasim toate erorile posibile 
    try:
         
        config.read('EmailData.ini') 

        if 'credentials' not in config:
            raise ValueError("Sectiunea 'credentials' nu exista in fisierul .ini.")

        if 'email' not in config['credentials']:
            raise ValueError("Cheia 'email' nu exista in sectiunea 'credentials'.")

        if 'password' not in config['credentials']:
            raise ValueError("Cheia 'password' nu exista in sectiunea 'credentials'.")


        email_sender = config['credentials']['email']
        email_password = config['credentials']['password']

        if not email_sender or not email_password:
            raise ValueError("Adresa de email sau parola nu sunt populate.")
    
    except Exception as e:
        print(f"Eroare: {e}")
        raise SystemExit()
        #sys.exit(1)

    subject = "Email de mare importanta! "
    body = f"Atentie! A scazut pretul la {product} sub limita {price} lei. Acest email a fost generat automat, nu raspundeti."
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:

            smtp.login(email_sender,email_password)
        
            smtp.sendmail(email_sender,email_receiver,em.as_string())

    except SMTPAuthenticationError:
        print("Eroare de autentificare SMTP. Email-ul sau parola sunt gresite")
    except SMTPException as e:
        print(f"Eroare SMTP: {e}")
    except Exception as e:
        print(f"Alta eroare: {e}")


send_email('xdan181@yahoo.com', 'asd ', 'sss ')