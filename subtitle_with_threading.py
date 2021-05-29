import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import key_word_extraction as kwe
import time
import shutil
import requests
import concurrent.futures
from itertools import repeat
import silence_copy

# create a speech recognition object
r = sr.Recognizer()

##convert vedio to wav file format
##os.system("ffmpeg -i "+Input_file_path+" -strict experimental "+Output_file_path+".txt")
'''audio_filename = "output_wave2.wav"
vedio_filename="vd_2.mp4"
os.system(f'cmd /c " ffmpeg -i {vedio_filename} -vn {filename}"')
#os.system('cmd /c " ffmpeg -i output2.mp3 -vn output_wave.wav"')
'''

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path_target):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    audio_filename = path_target.split('.')[0]+"."+"wav"
    print("file name : ",audio_filename)
    #time.sleep(2)
    os.system(f'cmd /c " ffmpeg -i {path_target} -codec:a libmp3lame -qscale:a 2 {audio_filename}"')
    #os.system(f'cmd /c " ffmpeg -i {path} -vn -ab 70 {audio_filename}"')

    print('audio file is created...........')
    path=audio_filename

    # open the audio file using pydub -ab 256

    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    start_end_time,chunks = silence_copy.split_on_silence(sound,
        # experiment with this value for your target audio file
        #by this we can adjust the size of each sentance length
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-11,
        # keep the silence for 1 second, adjustable as well
        keep_silence=1000,
    )

    start_end_chunk = [[t , ch] for t, ch in zip(start_end_time,chunks)]
    start_end_chunk_index=list(enumerate(start_end_chunk))
    # value are in the form [( index,[ [start_time,end_time] ,chunk ])]
    
    folder_name = path_target.split('.')[0]
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    time.sleep(3)
    start_end_subtitle=[] #final answer will store in that list [start ,end ,end subtitles]
    whole_text=""
    def process_chunk(folder_name,chunk_data):
        nonlocal whole_text
        print(folder_name,chunk_data)
        audio_chunk=chunk_data[1][1]
        chunk_filename = os.path.join(folder_name, f"chunk{chunk_data[0]}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                pass
            else:
                text = f"{text.capitalize()}. "
                text=text.strip()
                if(len(text)>0):
                    start_end_time=chunk_data[1][0]
                    start_end_time.append(text)
                    start_end_subtitle.append(start_end_time)
                    print(text)
                whole_text+=text

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_chunk,repeat(folder_name),start_end_chunk_index)    
   
    final_start_end_subtitle=[]
    obj=kwe.key_word_find(whole_text)    ##by importing code of key_word_extraction
    final_keyword=obj.get_top_n(10)      ## get top x key_word
   
    ## select only thos subtitle that have keyword 
    for l in start_end_subtitle:         
        for word in final_keyword:
            if word in l[2]:
                print(word)
                final_start_end_subtitle.append(l)
                break 
    final_start_end_subtitle.sort()
    delete_files_folder(audio_filename, folder_name)
    return final_start_end_subtitle

def delete_files_folder(audio_filename, folder_name):
    shutil.rmtree(folder_name)
    os.remove(audio_filename)
    #delete folder after work is completedos.remove(audio_filename)  #delete audio files that are genrated

if __name__=='__main__':
    begin = time.time()
    path = 'vd_2.mp4'
    print("\nFull text:", get_large_audio_transcription(path))
    end = time.time()
    print(f'total time {end-begin}')
