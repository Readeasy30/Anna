import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AndroidNotifier:
    def __init__(self):
        # Configure your sending email (your SlotsfreeUSA account)
        self.smtp_server = "://gmail.com"
        self.smtp_port = 587
        self.sender_email = "SlotsfreeUSA@gmail.com"
        
        # 🔑 WINDOWS PASSWORD REQUIRED:
        # Generate an "App Password" inside your Google Account Security settings
        # and paste the 16-letter code here instead of your normal email password.
        self.sender_password = "YOUR_GOOGLE_APP_PASSWORD"
        
        # 📱 PHONE ROUTING CONFIGURATION:
        # Enter your cell phone number and select your mobile carrier's gateway domain.
        # Examples:
        # AT&T:     "yournumber@txt.att.net"
        # Verizon:  "yournumber@vtext.com"
        # T-Mobile: "yournumber@tmomail.net"
        self.recipient_phone_gateway = "YOUR_PHONE_NUMBER@vtext.com"

    def send_cell_alert(self, client_name, tier_selected):
        print(f"📡 Processing notification trigger for client: {client_name}...")
        
        subject = "✨ New Showroom Order!"
        body = f"Webmasters LLC Alert:\nClient {client_name} just requested a {tier_selected} deployment!\nCheck your dashboard queue."

        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.recipient_phone_gateway
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Secure connection link to Google Mail server layers
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.recipient_phone_gateway, msg.as_string())
            server.quit()
            print("🚀 Notification successfully pushed straight to your mobile cell phone screen!")
        except Exception as e:
            print(f"❌ Notification failed: {str(e)}")
            print("💡 Tip: Verify your Google App Password is correct and entered into the script.")

if __name__ == "__main__":
    notifier = AndroidNotifier()
    # Run a quick local test notification pulse
    notifier.send_cell_alert("Showroom Test Lead", "Level 4 Android")
