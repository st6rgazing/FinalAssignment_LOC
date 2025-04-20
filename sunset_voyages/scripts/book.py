#!/usr/bin/env python3

print("Content-Type: text/html")
print()

import cgi

form = cgi.FieldStorage()

print(f'''
<html>
<head><title>Book Form Submission</title></head>
<body>
  <h2>Book Form Submission</h2>
  <ul>
    <li><strong>name:</strong> {form.getvalue('name', '')}</li>
    <li><strong>email:</strong> {form.getvalue('email', '')}</li>
    <li><strong>destination:</strong> {form.getvalue('destination', '')}</li>
    <li><strong>dates:</strong> {form.getvalue('dates', '')}</li>
    <li><strong>travelers:</strong> {form.getvalue('travelers', '')}</li>
  </ul>
</body>
</html>
''')
