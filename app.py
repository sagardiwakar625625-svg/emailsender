from flask import Flask, render_template, request
import smtplib
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    sender_name = request.form["name"]
    gmail_user = request.form["gmail"]
    gmail_password = request.form["password"]
    emails = request.form["emails"]
    subject = request.form["subject"]
    message = request.form["message"]

    receiver_list = [
        email.strip()
        for email in re.split(r'[\n,]+', emails)
        if email.strip()
    ]

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=15)
        server.starttls()
        server.login(gmail_user, gmail_password)

        for receiver in receiver_list:
            body = f"""Subject: {subject}

{message}

----------------
Sent by: {sender_name}
Email: {gmail_user}
"""

            server.sendmail(gmail_user, receiver, body)

        server.quit()

        return f"""
        <h2>✅ Email Sent To {len(receiver_list)} People</h2>
        <br>
        <a href="/">Send More</a>
        """

    except Exception as e:
        return f"<h3>Error:</h3><pre>{str(e)}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)from flask import Flask, render_template, request
import smtplib
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    sender_name = request.form["name"]
    gmail_user = request.form["gmail"]
    gmail_password = request.form["password"]
    emails = request.form["emails"]
    subject = request.form["subject"]
    message = request.form["message"]

    receiver_list = [
        email.strip()
        for email in re.split(r'[\n,]+', emails)
        if email.strip()
    ]

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=15)
        server.starttls()
        server.login(gmail_user, gmail_password)

        for receiver in receiver_list:
            body = f"""Subject: {subject}

{message}

----------------
Sent by: {sender_name}
Email: {gmail_user}
"""

            server.sendmail(gmail_user, receiver, body)

        server.quit()

        return f"""
        <h2>✅ Email Sent To {len(receiver_list)} People</h2>
        <br>
        <a href="/">Send More</a>
        """

    except Exception as e:
        return f"<h3>Error:</h3><pre>{str(e)}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)