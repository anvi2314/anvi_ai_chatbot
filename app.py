from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__, static_folder='static', template_folder='templates')

OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:11434')
MODEL = os.environ.get('MODEL', 'llama2')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    message = data.get('message', '').strip()
    if not message:
        return jsonify({'error': 'Empty message'}), 400

    try:
        url = f"{OLLAMA_URL}/api/chat"
        payload = {"model": MODEL, "messages": [{"role": "user", "content": message}], "stream": False}
        resp = requests.post(url, json=payload, timeout=120)
        # Try parse JSON, fallback to raw text
        try:
            j = resp.json()
            if isinstance(j, dict):
                if 'message' in j and 'content' in j['message']:
                    reply = j['message']['content']
                elif 'response' in j:
                    reply = j['response']
                else:
                    reply = str(j)
            else:
                reply = str(j)
        except ValueError:
            reply = resp.text

        return jsonify({'reply': reply})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Upstream request failed: {e}'}), 502


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
