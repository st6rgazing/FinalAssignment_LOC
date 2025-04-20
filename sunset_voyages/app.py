#!/usr/bin/env python3
import cgi
import cgitb
import os
from urllib.parse import parse_qs

cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
query = os.environ.get("QUERY_STRING", "")
params = parse_qs(query)

def print_header(title):
    print(f"""
    <html>
    <head><title>{title}</title></head>
    <body>
    <h2>{title}</h2>
    """)

def print_footer():
    print("</body></html>")

form_type = params.get("form", [""])[0]

if form_type == "signup":
    email = form.getvalue("email", "")
    password = form.getvalue("password", "")
    print_header("Signup Submitted")
    print(f"<p>Email: {email}</p>")
    print(f"<p>Password: {'*' * len(password)}</p>")
    print_footer()

elif form_type == "login":
    email = form.getvalue("email", "")
    password = form.getvalue("password", "")
    print_header("Login Attempt")
    print(f"<p>Email: {email}</p>")
    print(f"<p>Password: {'*' * len(password)}</p>")
    print_footer()

elif form_type == "contact":
    name = form.getvalue("name", "")
    email = form.getvalue("email", "")
    subject = form.getvalue("subject", "")
    message = form.getvalue("message", "")
    print_header("Contact Message Received")
    print(f"<p>Name: {name}</p>")
    print(f"<p>Email: {email}</p>")
    print(f"<p>Subject: {subject}</p>")
    print(f"<p>Message: {message}</p>")
    print_footer()

elif form_type == "book":
    destination = form.getvalue("destination", "")
    departure = form.getvalue("departure", "")
    people = form.getvalue("people", "")
    notes = form.getvalue("notes", "")
    print_header("Booking Received")
    print(f"<p>Destination: {destination}</p>")
    print(f"<p>Departure Date: {departure}</p>")
    print(f"<p>People: {people}</p>")
    print(f"<p>Notes: {notes}</p>")
    print_footer()

else:
    print_header("Invalid Form Submission")
    print("<p>No valid form type provided.</p>")
    print_footer()
