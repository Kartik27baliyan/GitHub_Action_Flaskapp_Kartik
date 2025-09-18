from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to GitHub Actions Flask App!", "status": "success"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "flask-app"})

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({"greeting": f"Hello, {name}!", "timestamp": "2025-09-18"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
