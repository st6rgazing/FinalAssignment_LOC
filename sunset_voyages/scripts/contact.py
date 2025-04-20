#!/usr/bin/env python3

print("Content-Type: text/html")
print()

import cgi

form = cgi.FieldStorage()

print(f'''
<html>
<head><title>Contact Form Submission</title></head>
<body>
  <h2>Contact Form Submission</h2>
  <ul>
    <li><strong>name:</strong> {form.getvalue('name', '')}</li>
    <li><strong>email:</strong> {form.getvalue('email', '')}</li>
    <li><strong>subject:</strong> {form.getvalue('subject', '')}</li>
    <li><strong>message:</strong> {form.getvalue('message', '')}</li>
  </ul>
</body>
</html>
''')
