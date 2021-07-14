from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import subtitle_with_threading as swt
app = Flask(__name__, static_folder='static')
  
@app.route("/")
def success():
    path='que_ans_video.mp4'
    path='videoplayback.mp4'
    #time_subtitle=[]
    time_subtitle = swt.get_large_audio_transcription('static'+'/'+path)
    time_subtitle.append(path)
    return render_template("success.html", len = len(time_subtitle),time_subtitle=time_subtitle)
		
if __name__ == '__main__':
   app.run(debug = True)




