from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import io
from TTS.utils.synthesizer import Synthesizer
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
allowed_origins = ["https://verbatone.netlify.app"]
CORS(app, resources={r"/*": {"origins": allowed_origins}})
app.config['CORS_HEADERS'] = 'Content-Type'

synthesizer = None

VOLUME_MOUNT_PATH = os.getenv('RAILWAY_VOLUME_MOUNT_PATH')

MODEL_PATH = os.path.join(VOLUME_MOUNT_PATH, 'best_model.pth')
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json') 

@app.route('/synthesize', methods=['POST'])
def synthesize():
    api_key = os.getenv('API_KEY')
    if request.headers.get('X-API-KEY') != api_key:
        return jsonify({"error": "Invalid API Key"}), 403

    try:
        data = request.json
        text = data.get('text', '')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        if len(text) > 1000:
            return jsonify({'error': 'Text is too long'}), 400

        global synthesizer
        if synthesizer is None:
            synthesizer = Synthesizer(MODEL_PATH, CONFIG_PATH, use_cuda=False)
            wav = synthesizer.tts(text)

            wav_bytes = io.BytesIO()
            synthesizer.save_wav(wav, wav_bytes)
            wav_bytes.seek(0)

            return send_file(wav_bytes, mimetype='audio/wav', as_attachment=True, download_name='output.wav')
    except FileNotFoundError:
        return jsonify({'error': 'Model or config file not found'}), 500
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)