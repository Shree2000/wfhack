from flask import Flask, render_template, request,redirect

app = Flask(__name__,static_folder='static')

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
    audio_file = request.files['audio']
    filename = audio_file.filename
    if audio_file:
      audio_data = audio_file.read()
      return {"status": "okay","deepFakeStatus":"true","emotion":"Happy","backgroundsound":63,"fileName":filename}
    else:
      return "No audio file uploaded.", 400

if __name__ == "__main__":
  app.run(debug=True)