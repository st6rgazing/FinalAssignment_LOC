#!/usr/bin/env python3

print("Content-Type: text/html")
print()

import cgi

form = cgi.FieldStorage()

print(f'''
<html>
<head><title>Signup Form Submission</title></head>
<body>
  <h2>Signup Form Submission</h2>
  <ul>
    <li><strong>first_name:</strong> {form.getvalue('first_name', '')}</li>
    <li><strong>last_name:</strong> {form.getvalue('last_name', '')}</li>
    <li><strong>email:</strong> {form.getvalue('email', '')}</li>
    <li><strong>password:</strong> {form.getvalue('password', '')}</li>
  </ul>
</body>
</html>
''')
