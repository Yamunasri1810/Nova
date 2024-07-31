import imaplib
import smtplib
from email.mime.text import MIMEText
import face_recognition
import cv2
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os


def main():
    imap_server = "imap.gmail.com"
    imap_username = "your_email@gmail.com"
    imap_password = "your_email_password"
    read_email(imap_server, imap_username, imap_password)

    smtp_server = "smtp.gmail.com"
    smtp_username = "your_email@gmail.com"
    smtp_password = "your_email_password"
    recipient = "recipient@example.com"
    subject = "Test Email"
    body = "This is a test email sent using Python."
    send_email(smtp_server, smtp_username, smtp_password, recipient, subject, body)

    # Load the known faces and face recognition model
    known_faces = []
    known_names = []
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Capture a frame from the camera
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    recognize_face(frame)

    # Run the speech recognition and command execution function
    run_nova()

if __name__ == "__main__":
    main()
