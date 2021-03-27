import os
##os.system("ffmpeg -i "+Input_file_path+" -strict experimental "+Output_file_path+".txt")
#os.system('cmd /c " ffmpeg -i vd_2.mp4 -vn -ab 25 output_wave2.wav"')
os.system('cmd /c " ffmpeg -i static/oops.mp4 -codec:a libmp3lame -qscale:a 2 output.wav"')

#os.system('cmd /c " ffmpeg -i output_wave2.wav -codec:a libmp3lame -qscale:a 2 output.wav"')
#os.system('cmd /c " ffmpeg -i output2.mp3 -vn output_wave.wav"')
print('done')
