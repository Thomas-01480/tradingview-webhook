from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    with open("signal.json", "w") as f:
        json.dump(data, f)
    return "Signal reçu", 200

if __name__ == '__main__':
    app.run()
