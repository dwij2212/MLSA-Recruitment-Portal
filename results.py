import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mspsite.settings")
# import smtplib
# from email.message import EmailMessage
import django
django.setup()

from test_portal.models import Candidate, ResponseMCQ
import pandas as pd

def get_all_candidates():
    return Candidate.objects.all()

def get_all_responses(candidate):
    # retrieves all responses marked by the candidate
    return ResponseMCQ.objects.filter(user=candidate)

def get_empty_df():
    df = pd.DataFrame(columns=['Name', 'Email', 'Marks'])
    return df

main_df = get_empty_df()

def to_excel_sheet(df):
    candidates = get_all_candidates()

    for i, candidate in enumerate(candidates):
        responses = get_all_responses(candidate)

        marks = 0
        for response in responses:
            marks += response.marks

        if i%10 == 0:
            print("Marks for {num} th Candidate calculated".format(num=i))

        df = df.append({'Name': candidate.firstName + " " + candidate.lastName, 'Email':candidate.email[7:], 'Marks':marks}, ignore_index=True)
        # msg = EmailMessage()
        # body = "Greetings from MLSA! \n Thank you for showing your interest in the club and attending the test. We have validated your responses and your scores have been generated.\nYour Score : <<Marks>>\n\nYou will be contacted soon if you are selected for further rounds."
        # msg.set_content(body)
        # msg['subject']= "MLSA Recruitment Test Results" 
        # msg['to']= candidate.email[7:]
        
        # user = "supreeth.mksupreeth@gmail.com"
        # msg['from'] = user
        # password='eqinpbunocxuxqta'

        # server = smtplib.SMTP("smtp.gmail.com",587)
        # server.starttls()
        # server.login(user,password)
        # server.send_message(msg)
        # server.quit()

    df.to_csv("Results.csv")

