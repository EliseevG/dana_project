from flask import Flask, request

from dos_protection import DOSProtection

app = Flask(__name__)
protection = DOSProtection()

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.before_request
def check_dos():
    client_ip = request.remote_addr
    if not protection.is_allowed(client_ip):
        return "Превышен лимит запросов", 429

if __name__ == '__main__':
    app.run()