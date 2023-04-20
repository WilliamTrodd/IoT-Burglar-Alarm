import smtplib
import ssl
import RPi.GPIO as GPIO
import time
# import opencv-python

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
pir = 37  # Motion sensor - these pins should change depending on your GPIO setup
ldr = 35  # Light sensor - these pins should change depending on your GPIO setup
led = 16  # LED - these pins should change depending on your GPIO setup

GPIO.setup(pir, GPIO.IN)
GPIO.setup(ldr, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

port = 465
password = ""  # Enter your password
context = ssl.create_default_context()

sender_email = ""  # Enter your email address
receiver_email = ""  # Enter the receiver's email address
message = "motion detected"  # The message you want to send

# Set up the SMTP server
with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(sender_email, password)  # Login to your email
    while True:
        # If motion is detected and the light is low
        if GPIO.input(pir) and GPIO.input(ldr):
            GPIO.output(led, GPIO.HIGH)  # Turn on the LED
            server.sendmail(sender_email, receiver_email,
                            message)  # Send the email
            time.sleep(5)  # Wait 5 seconds
            GPIO.output(led, GPIO.LOW)  # Turn off the LED
            time.sleep(5)  # Wait 5 seconds
