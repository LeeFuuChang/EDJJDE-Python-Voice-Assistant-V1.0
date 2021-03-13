import smtplib
import email

myGmail = "Your Gmail Account"
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
        try:
            server.login(myGmail, "Your Gmail Password")
        except:
            raise BaseException("Invalid Gmail Account Or Password, Did you forget to change it to your own?")
print("Gmail login Successful")
server.sendmail(myGmail, SendTo, TheMessage)
print("Gmail Sent:\n"+TheMessage)
server.quit()