# app.py
from flask import Flask, request, render_template
import datetime
import requests
from pathlib import Path
import ujson
import logging

app = Flask(__name__)


parent_directory = Path.cwd().parent

# helper to get client IP
def get_client_ip():
    xff = request.headers.get('X-Forwarded-For') or request.headers.get('x-forwarded-for')
    if xff:
        return xff.split(',')[0].strip()
    return request.remote_addr or 'unknown'

def fetch_ip_info(ip):
    if not ip or ip == 'unknown':
        return {}
    try:
        resp = requests.get(f"https://ipinfo.io/{ip}/json", timeout=3)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return {}

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = get_client_ip()
    ip_info = fetch_ip_info(ip)

    context = {
        "ID": None,
        "IP": ip,
        "Timestamp": timestamp,
        "UserAgent": user_agent,
        "Info": ip_info
    }

    context_data = f"ID: {str(id)}, IP: {ip}, Timestamp: {timestamp}, UserAgent: {user_agent}, Info: {ip_info}"
    print(context_data)    
    logging.INFO(context_data)
    return render_template('index.html', ID=str(id), IP=ip)

@app.route('/<id>')
def tracking_pixel_id(id):
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = get_client_ip()
    ip_info = fetch_ip_info(ip)

    context = {
        "ID": id,
        "IP": ip,
        "Timestamp": timestamp,
        "UserAgent": user_agent,
        "Info": ip_info
    }

    context_data = f"ID: {str(id)}, IP: {ip}, Timestamp: {timestamp}, UserAgent: {user_agent}, Info: {ip_info}"

    print(context_data)
    logging.INFO(context_data)
    return render_template('index.html', ID=str(id), IP=ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
