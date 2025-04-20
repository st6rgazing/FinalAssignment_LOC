#!/usr/bin/env python3

print("Content-Type: text/html")
print()

import cgi

form = cgi.FieldStorage()

print(f'''
<html>
<head><title>Login Form Submission</title></head>
<body>
  <h2>Login Form Submission</h2>
  <ul>
    <li><strong>email:</strong> {form.getvalue('email', '')}</li>
    <li><strong>password:</strong> {form.getvalue('password', '')}</li>
  </ul>
</body>
</html>
''')
