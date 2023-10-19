import smtplib
from email.message import EmailMessage
import os

def send_email():
    msg = EmailMessage()
    msg.set_content("Tests failed! There is an issue with the build and tests.")
    msg["Subject"] = "Build and Test Failure Notification"
    msg["From"] = "wincchesster@gmail.com"
    msg["To"] = "wincchesster@gmail.com"  # Replace with the recipient's email address

    # Set up the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Log in to your Gmail account
    gmail_user = "wincchesster@gmail.com"
    gmail_password = "GMAIL_PASSWORD"  # Use the GitHub Secret name for your Gmail password
    print("Username:", gmail_user)
    print("Password:", gmail_password)
    server.login(gmail_user, gmail_password)

    # Send the email
    server.send_message(msg)

    # Close the connection to the SMTP server
    server.quit()

if __name__ == "__main__":
    send_email()
