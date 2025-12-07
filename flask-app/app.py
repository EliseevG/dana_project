from flask import Flask, request, render_template, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from dos_protection import DOSProtection

app = Flask(__name__)
metrics = PrometheusMetrics(app)
protection = DOSProtection()

@app.route('/')
def index():
    return render_template('index.html')


@app.before_request
def check_dos():
    client_ip = request.remote_addr
    if not protection.is_allowed(client_ip):
        return "Превышен лимит запросов", 429

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)