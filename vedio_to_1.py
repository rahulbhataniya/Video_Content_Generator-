import os
import speech_recognition as sr

Input_file_path = 'audio.mp3'
Output_file_path = 'result'
##os.system("ffmpeg -i "+Input_file_path+" -strict experimental "+Output_file_path+".txt")
os.system('cmd /c " ffmpeg -i vd_1.mp4 -vn output_wave.wav"')
#os.system('cmd /c " ffmpeg -i output2.mp3 -vn output_wave.wav"')

'''convert wav file to text
'''
print('wave file is created....')
filename = "output_wave.wav"
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

print('done')