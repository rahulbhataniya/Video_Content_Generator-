# importing the multiprocessing module
import multiprocessing
import os
import time
import large_wav_to_text

def worker1(path):
	# printing process id
    print("\nFull text from worker 1:",large_wav_to_text.get_large_audio_transcription(path))
    #print("ID of process running worker1: {}".format(os.getpid()))

def worker2(path):
	# printing process id
    print("\nFull text from worker 2:",large_wav_to_text.get_large_audio_transcription(path))
	#print("ID of process running worker2: {}".format(os.getpid()))
def worker3(path):
	# printing process id
    print("\nFull text from worker 3:",large_wav_to_text.get_large_audio_transcription(path))
	#print("ID of process running worker2: {}".format(os.getpid()))


if __name__ == "__main__":
	# printing main program process id
    begin=time.time()
    os.system("ffmpeg -i vd_1.mp4 -t 00:01:00 -c copy part1.mp4 -ss 00:01:00 -codec copy part2.mp4")
    os.system("ffmpeg -i part2.mp4 -t 00:01:00 -c copy part21.mp4 -ss 00:01:00 -codec copy part22.mp4")
   # os.system("ffmpeg -i part22.mp4 -t 00:00:49 -c copy part31.mp4 -ss 00:00:49 -codec copy part32.mp4")
    print("ID of main process: {}".format(os.getpid()))
    p1 = multiprocessing.Process(target=worker1,args=("part1.mp4",))
    p2 = multiprocessing.Process(target=worker2,args=("part21.mp4",))
    p3 = multiprocessing.Process(target=worker3,args=("part22.mp4",))
	# starting processes
    p1.start()
    p2.start()
    p3.start()

	# process IDs
    #print("ID of process p1: {}".format(p1.pid))
    #print("ID of process p2: {}".format(p2.pid))

	# wait until processes are finished
    p1.join()
    p2.join()
    p3.join()

	# both processes finished
    
    end=time.time()

    print(f'total time {end-begin}')

    