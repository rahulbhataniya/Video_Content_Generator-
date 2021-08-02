from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import subtitle_with_threading as swt
import Question_finder_with_threading as Qwt
app = Flask(__name__, static_folder='static')
  
@app.route("/")
def success():
    path='APJ.mp4'
    #path='que_ans_video.mp4'
    #time_subtitle=[]
    #keyword_algo='tf_idf'
    keyword_algo='yake'
    code_for='subtitle'
    code_for='Questions'
    if(code_for=='subtitle'):
        time_subtitle = swt.get_large_audio_transcription('static'+'/'+path,keyword_algo)
    else:
        time_subtitle = Qwt.get_large_audio_transcription('static'+'/'+path,keyword_algo)
    time_subtitle.append(path)
    return render_template("success.html", len = len(time_subtitle),time_subtitle=time_subtitle)

if __name__ == '__main__':
   app.run(debug = True)

#


