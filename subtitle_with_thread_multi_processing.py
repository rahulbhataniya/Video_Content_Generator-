# importing the multiprocessing module
import multiprocessing
import os
import time
import subtitle_with_threading

def worker1(path,algo):
    print("\nFull text from worker 1:",subtitle_with_threading.get_large_audio_transcription(path,algo))

def worker2(path,algo):
    print("\nFull text from worker 2:",subtitle_with_threading.get_large_audio_transcription(path,algo))
	
def worker3(path,algo):
    print("\nFull text from worker 3:",subtitle_with_threading.get_large_audio_transcription(path,algo))
	


if __name__ == "__main__":
    begin=time.time()
    os.system("ffmpeg -i vd_2.mp4 -t 00:01:00 -c copy part1.mp4 -ss 00:01:00 -codec copy part2.mp4")
    os.system("ffmpeg -i part2.mp4 -t 00:01:00 -c copy part21.mp4 -ss 00:01:00 -codec copy part22.mp4")
   # os.system("ffmpeg -i part22.mp4 -t 00:00:49 -c copy part31.mp4 -ss 00:00:49 -codec copy part32.mp4")
    print("ID of main process: {}".format(os.getpid()))
    p1 = multiprocessing.Process(target=worker1,args=("part1.mp4","tf_idf",))
    p2 = multiprocessing.Process(target=worker2,args=("part21.mp4","tf_idf",))
    p3 = multiprocessing.Process(target=worker3,args=("part22.mp4","tf_idf",))
	# starting processes
    p1.start()
    p2.start()
    p3.start()
	# wait until processes are finished
    p1.join()
    p2.join()
    p3.join()
    os.remove("part1.mp4")
    os.remove("part2.mp4")
    os.remove("part21.mp4")
    os.remove("part22.mp4")
    end=time.time()

    print(f'total time {end-begin}')
