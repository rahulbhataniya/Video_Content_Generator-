
#please read note from time analysis text file about the problem with multitreading
import multiprocessing
import os
import time
import sbtitle_without_threading
import subprocess
final_start_end_subtitle=list()
def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)

def worker(path,st):
    global final_start_end_subtitle
    res=sbtitle_without_threading.get_large_audio_transcription(path)
    print(res)
    for data in res:
        final_start_end_subtitle.append(data)
def worker(path,st):
    global final_start_end_subtitle
    res=sbtitle_without_threading.get_large_audio_transcription(path)
    print(res)
    for data in res:
        final_start_end_subtitle.append(data)


        
	
def get_time(t):
    hr=int(t//(60*60))#hr
    t=t-hr*60*60
    min=int(t//(60)) #sec
    t=t-min*60
    sec=int(t)
    return hr,min,sec


if __name__ == "__main__":
    begin=time.time()
    length_video=get_length("vd_2.mp4")
    print(length_video)
    part_length=length_video/4
    start_time=[]
    start=0
    for i in range(4):
        start_time.append(start)
        start+=part_length 
    
    lhr,lmin,lsec=get_time(part_length)
    
    video_list=[]
    file_path="vd_1.mp4"
    for i in range(0,4):
        sHr,smin,ssec=get_time(start_time[i])
        os.system(f"ffmpeg -ss {sHr}:{smin}:{ssec} -i {file_path}  -t {lhr}:{lmin}:{lsec} -c:v copy -c:a copy trim_copy{i}.mp4" )
        #ffmpeg -ss 00:00:03 -i inputVideo.mp4 -to 00:00:08 -c:v copy -c:a copy trim_ipseek_copy.mp4
        video_list.append(f"trim_copy{i}.mp4")
    processes=[]
    for i in range(4):
        p=multiprocessing.Process(target=worker,args=(video_list[i],start_time[i],))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

    for i in range(4):
        try:
            os.remove(f"trim_copy{i}.mp4")
        except:
            pass

    final_start_end_subtitle.sort()
    print(final_start_end_subtitle)
    end=time.time()

    print(f'total time {end-begin}')
    print('final ans :')
    print(final_start_end_subtitle)