import speech_recognition as sr 
#import speech_recognizer as sr
import moviepy.editor as mp


print('start...processing')
clip = mp.VideoFileClip(r"vd_1.mp4") 

print('vedio is loded ....')
clip.audio.write_audiofile(r"converted_to_wav.wav")

print('time to recognize speech')
r = sr.Recognizer()

audio = sr.AudioFile("converted_to_wav.wav")

with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)

# exporting the result 
with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")
