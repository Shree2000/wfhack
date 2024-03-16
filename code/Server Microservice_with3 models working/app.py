from flask import Flask, render_template, request,redirect
from speec2emotion import predict
from noiseIntensityDetection import findIntensity
from deepfakeDetection import predictDeepFake


import tempfile
import os

   

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  return redirect("/voice/analyze")


@app.route("/ping", methods=["GET"])
def ping():
  return "pong", 200

@app.route("/voice/analyze", methods=["GET", "POST"])
def voice_analyze():
  if request.method == "GET":
    return render_template("voice_form.html")
  elif request.method == "POST":
    audio_file = request.files.get("audio_file")
    print(audio_file)
    if audio_file:
      

      app_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Save the uploaded file to the same directory as app.py
      file_path = os.path.join(app_dir, audio_file.filename)
      audio_file.save(file_path)
      audio_data=audio_file.read()
      
 
      intensity=findIntensity(file_path)
      emotion=predict(file_path)
      ans=predictDeepFake(file_path)
      # audio_data = audio_file.read()
      # Export the audio to WAV format
      
      if os.path.exists(file_path):
        print("file removed")
        os.remove(file_path)

      return {"status": "okay",
              "deepFakeStatus":ans,
              "emotion":emotion,
               "backgroundsound": intensity
              }
    else:
      return "No audio file uploaded.", 400

if __name__ == "__main__":
  app.run(debug=True)