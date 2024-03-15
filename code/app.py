from flask import Flask, jsonify, request
from pydub import AudioSegment
import io
from ProcessAudio.NeuralNetwork import process


app = Flask(__name__)

# Ping API
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'success'}), 200
# Predict API
@app.route('/voice/analyze', methods=['POST'])
def voice_analyze():
   # Assuming audio data is sent in the POST request
    audio_data = request.data
    
    # Convert the audio data to an AudioSegment object
    audio = AudioSegment.from_mp3(io.BytesIO(audio_data))
    
    # Call the process function from neuralnetwork.py
    result = process(audio)

    # Return the result
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)