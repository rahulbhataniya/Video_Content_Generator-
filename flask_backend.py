from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import large_wav_to_text as lwt
import subtitle_with_threading as swt
app = Flask(__name__, static_folder='static')
  
@app.route("/")
def success():
    path='vanesha.mp4'
    #time_subtitle=[]
    time_subtitle = swt.get_large_audio_transcription('static'+'/'+path)
    time_subtitle.append(path)
    return render_template("success.html", len = len(time_subtitle),time_subtitle=time_subtitle)
		
if __name__ == '__main__':
   app.run(debug = True)




