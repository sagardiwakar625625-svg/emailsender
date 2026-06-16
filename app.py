from flask import Flask, render_template, request
import smtplib
import re
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():

    sender_name = request.form['name']
    gmail_user = request.form['email']
    gmail_password = request.form['app_password']
    emails = request.form['emails']
    subject = request.form['subject']
    message = request.form['message']

    receiver_list = [
        email.strip()
        for email in re.split(r'[\n,]+', emails)
        if email.strip()
    ]

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_user, gmail_password)

        for receiver in receiver_list:

            body = f"""
Name: {sender_name}

Message:
{message}
"""

            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = gmail_user
            msg["To"] = receiver

            server.sendmail(
                gmail_user,
                receiver,
                msg.as_string()
            )

        server.quit()

        return f"✅ Email Sent To {len(receiver_list)} People"

    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)