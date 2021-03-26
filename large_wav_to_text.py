import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import key_word_extraction as kwe

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
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    audio_filename = "output_wave2.wav"
    
    os.system(f'cmd /c " ffmpeg -i {path} -vn {audio_filename}"')
    path=audio_filename
    # open the audio file using pydub

    sound = AudioSegment.from_wav(path)  

   
    # split audio sound where silence is 700 miliseconds or more and get chunks
    start_end_time,chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        #by this we can adjust the size of each sentance length
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-11,
        # keep the silence for 1 second, adjustable as well
        keep_silence=1000,
    )
    #chunks=chunks_with_time[0]
    #print(start_end_time)
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    j=0  #for time from start_end_list


    #**          ............           **#
    
     ## start_end_subtile store the start and and time stamp and sentece related to that##
    
    ##**          .....................   **#



    start_end_subtitle=[]
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        #save the each audio chunk at chink_filename file
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                pass
                #print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                #print(chunk_filename, ":", text,end=" ")
                #print(start_end_time[j])
                text=text.strip()
                if(len(text)>0):
                    start_end_time[j].append(text)
                    start_end_subtitle.append(start_end_time[j])
                whole_text += text
        j=j+1
    # return the text for all chunks detected
    ################################################################################
    # now we have transcript and subtitle its time to filter out important key word ##
    #################################################################################
    final_start_end_subtitle=[]
    obj=kwe.key_word_find(whole_text)    ##by importing code of key_word_extraction
    final_keyword=obj.get_top_n(4)      ## get top x key_word
   
    ## select only thos subtitle that have keyword 
    for l in start_end_subtitle:         
        for word in final_keyword:
            if word in l[2]:
                final_start_end_subtitle.append(l)
                break
    return final_start_end_subtitle
    
    return "done_lodu"

if __name__=='__main__':
    path = 'static/vd3.mp4'
    print("\nFull text:", get_large_audio_transcription(path))
