import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

# create a speech recognition object
r = sr.Recognizer()


##convert vedio to wav file format
##os.system("ffmpeg -i "+Input_file_path+" -strict experimental "+Output_file_path+".txt")
os.system('cmd /c " ffmpeg -i vd_2.mp4 -vn output_wave2.wav"')
#os.system('cmd /c " ffmpeg -i output2.mp3 -vn output_wave.wav"')

'''convert wav file to text
'''
print('wave file is created....')

filename = "ml2.wav"


# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
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
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text,end=" ")
                print(start_end_time[j])
                whole_text += text
        j=j+1
    # return the text for all chunks detected
    return whole_text


path = filename
print("\nFull text:", get_large_audio_transcription(path))