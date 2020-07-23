from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from blog.models import *
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib import messages
# Create your views here.

# homepage function
def index(request):
    return render(request,"mysite/try.html")

# Cosultancy
def consultation(request):
    # getting user information via POSt
    if request.method == "POST":
        name = request.POST.get("company_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        topic = request.POST.get("topic")
        # Adding information to a DB
        #x = questions(name=name, age=age ,email=email, phone=phone, highest_education=education,
            #question= question)
        message = MIMEMultipart("alternative")
        message["Subject"] = "Consultacny Request"
        message["From"] = "MyWebSite"

        # Create the plain-text and HTML version of your message
        text = """\
        Subject: Hi there


        """
        html = """\
            <html>
                <body>
                    Hello Omar

                      <p> %s Has Just Submitted A Consultancy Request
                      <p> Topic: %s
                      <p> Email: %s
                      <p> Phone: %s

                    </p>
                </body>
            </html>
        """ %(name,topic,email,phone,)
        # Turn these into plain/html MIMEText objects
        p1 = MIMEText(text,"plain")
        p2 = MIMEText(html,"html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(p1)
        message.attach(p2)
        x = sending_mail(message)
        messages.success(request,"Request Submitted Successfully")
        return HttpResponseRedirect(reverse(index))
    else:
        return render(request, "mysite/consultation.html",)


# Asking for Mentorship
def mentorship(request):
    # getting user information via POSt
    if request.method == "POST":
        name = request.POST.get("usnm")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        education = request.POST.get("education")
        level = request.POST.get("level")
        track = request.POST.get("mytrack")
        if not track:
            track = request.POST.get("other_track")
        describtion = request.POST.get("describtion")
        # Adding information to a DB
        save_info = info(name=name, age=age ,email=email, phone=phone, highest_education=education,
         level=level, track=track ,describtion=describtion)
        save_info.save()

        message = MIMEMultipart("alternative")
        message["Subject"] = "Mentoring Request"
        message["From"] = "MyWebSite"


        # Create the plain-text and HTML version of your message
        text = """\
        Subject: Hi there

        This message is sent from Python."""
        html = """\
            <html>
                <body>
                    Hello Omar

                      <p> %s has just submitted a mentoring request </p>
                      <p> Age: %s
                      <p> Email: %s </p>
                      <p> Phone: %s
                      <p> Education: %s
                      <p> Track: %s
                      <p> Level: %s
                      <p> Describtion: %s
                    </p>
                </body>
            </html>
        """ %(name,age,email,phone,education,track,level,describtion)
        # Turn these into plain/html MIMEText objects
        p1 = MIMEText(text,"plain")
        p2 = MIMEText(html,"html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(p1)
        message.attach(p2)
        # Create a secure SSL context
        try:
            x = sending_mail(message)
        except:
            return HttpResponse("Error during sending message")
        messages.success(request,"Your Request Submitted Successfully")
        return HttpResponseRedirect(reverse(index))
    else:
        education = [
                    "Architecture","Art & Culture","Biology & Life Sciences","Business & Management",
                    "Chemistry","Communication","Computer Science","Data Analysis & Statistics",
                    "Economics & Finance","Education & Teacher Training",
                    "Electronics","Energy & Earth Sciences","Engineering","Language","Law",
                      "Literature",  "Math","Medicine",  "Physics","Science",]
        context = {
        "form": NameForm(),
        "education": education
        }
        return render(request, "mysite/mentorship.html" , context)


def sending_mail(message):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "shehabeldeen2019@gmail.com"
    receiver_email = "shehababbas2019@gmail.com"
    password = "shiko3bbas"

    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
