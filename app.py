from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "🔥 Hello this is vishvendar bhai from my second Flask Docker app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
