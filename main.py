from flask import Flask, request, render_template_string
import datetime
import os
# import logging

app = Flask(__name__)

# # Configure logging
# def log_to_file(log_path):
#     logging.basicConfig(
#         filename=log_path,
#         level=logging.INFO,
#         format='%(message)s'
#     )

# HTML template (replace or load from an external file if needed)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>IP Leak Test</title>
    <meta property="og:title" content="Website name" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://example.com/" />
    <meta property="og:description" content="Website description" />
</head>
<body>
    <h1>IP Leak PoC</h1>
    <p>Timestamp: {{ timestamp }}</p>
    <p>Your IP: {{ ip }}</p>
</body>
</html>
"""

@app.route('/')
def leak_ip():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ip = request.remote_addr
    request_dump = f"{request.method} {request.path}\nHeaders:\n{dict(request.headers)}\n\n{request.get_data(as_text=True)}"
    print(request_dump)
    return render_template_string(HTML_TEMPLATE, timestamp=timestamp, ip=ip)

@app.route('/<id>')
def leak_ip_id(id):
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ip = request.remote_addr
    request_dump = f"{request.method} {request.path}\nHeaders:\n{dict(request.headers)}\n\n{request.get_data(as_text=True)}"
    print(request_dump)
    return render_template_string(HTML_TEMPLATE, timestamp=timestamp, ip=ip)

@app.route('/favicon.ico')
def favicon():
    return "", 204

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
