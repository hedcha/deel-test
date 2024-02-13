from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    reversed_ip = '.'.join(reversed(ip.split('.')))
    return f"Origin public IP of the request in reverse: {reversed_ip}"

if __name__ == '__main__':
    app.run(debug=True)