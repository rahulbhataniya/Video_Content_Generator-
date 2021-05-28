from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import large_wav_to_text as lwt
app = Flask(__name__, static_folder='static')
  

@app.route("/")
def success():
    path='static\\vd_1.mp4'
    time_subtitle = lwt.get_large_audio_transcription(path)
    #time_subtitle=[[5.45,1,'hii'],[2,3,'baby'],[4,5,'bhi bhi ']]
    return render_template("success.html", len = len(time_subtitle),time_subtitle=time_subtitle)
		
if __name__ == '__main__':
   app.run(debug = True)