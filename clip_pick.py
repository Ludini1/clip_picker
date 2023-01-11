import tkinter as tk
from tkVideoPlayer import TkinterVideo

import glob
import random
import sys


def play_pause():
    """ pauses and plays """
    if videoplayer1.is_paused():
        videoplayer1.play()
        play_pause_btn["text"] = "Pause"

    else:
        videoplayer1.pause()
        play_pause_btn["text"] = "Play"

    if videoplayer2.is_paused():
        videoplayer2.play()
        play_pause_btn["text"] = "Pause"

    else:
        videoplayer2.pause()
        play_pause_btn["text"] = "Play"

def top_wins():

    global current_video1
    global current_video2
    global video_list
    global current_round
    global videoplayer1
    global videoplayer2
    global window

    videoplayer1.stop()
    videoplayer2.stop()

    print("top wins")

    video_list.remove(current_video1)
    video_list.remove(current_video2)

    winner_list.append(current_video1)
    loser_list.append(current_video2)

    print(len(video_list))
    print(len(winner_list))
    print(len(loser_list))

    if (len(video_list) <= 1): # Do lots of testing here
        if (len(winner_list) == 1):
            results_file.write("The winner is:\n")
            results_file.write('\n'.join(winner_list))
            results_file.write("!\n")
            results_file.close()
            videoplayer1.stop()
            videoplayer2.stop()
            window.destroy() 
            sys.exit("Found a Winner!")
        else:
            results_file.write("Round " + str(current_round) + ":\n")
            results_file.write('\n'.join(winner_list))
            results_file.write("\n")
            current_round += 1

            video_list = winner_list.copy()
            winner_list.clear()



    current_video1 = random.choice(video_list)
    current_video2 = random.choice(video_list)

    while (current_video1 == current_video2): # fix for accidentally choosing the same one, definitely a better way of doing this
        current_video2 = random.choice(video_list)

    videoplayer1.load(current_video1)
    videoplayer2.load(current_video2)

def bottom_wins():

    global current_video1
    global current_video2
    global video_list
    global current_round
    global videoplayer1
    global videoplayer2
    global window

    videoplayer1.stop()
    videoplayer2.stop()

    print("bottom wins")
    
    video_list.remove(current_video1)
    video_list.remove(current_video2)

    winner_list.append(current_video2)
    loser_list.append(current_video1)

    print(len(video_list))
    print(len(winner_list))
    print(len(loser_list))

    if (len(video_list) <= 1):
        if (len(winner_list) == 1):
            results_file.write("The winner is:\n")
            results_file.write('\n'.join(winner_list))
            results_file.write("!\n")
            results_file.close()
            videoplayer1.stop()
            videoplayer2.stop()
            window.destroy()          
            sys.exit("Found a Winner!")
        else:
            results_file.write("Round " + str(current_round) + ":\n")
            results_file.write('\n'.join(winner_list))
            results_file.write("\n")
            current_round += 1

            video_list = winner_list.copy()
            winner_list.clear()

    current_video1 = random.choice(video_list)
    current_video2 = random.choice(video_list)

    while (current_video1 == current_video2): # fix for accidentally choosing the same one, definitely a better way of doing this
        current_video2 = random.choice(video_list)

    videoplayer1.load(current_video1)
    videoplayer2.load(current_video2)

def pass_next():
    global current_video1
    global current_video2

    current_video1 = random.choice(video_list)
    current_video2 = random.choice(video_list)
    videoplayer1.load(current_video1)
    videoplayer2.load(current_video2)

def loop1(e):
    videoplayer1.play()

def loop2(e):
    videoplayer2.play()

video_list = glob.glob("*.mp4")

print(video_list)

winner_list = []
loser_list = []
current_round = 1

results_file = open("results.txt", "a")

current_video1 = random.choice(video_list)
current_video2 = random.choice(video_list)

window = tk.Tk()
window.title("Clip Pick")
window.geometry("720x720")


videoplayer1 = TkinterVideo(master=window, scaled=True)
videoplayer1.load(current_video1)
videoplayer1.pack(expand=True, fill="both")
videoplayer1.set_size([720, 360])


videoplayer2 = TkinterVideo(master=window, scaled=True)
videoplayer2.load(current_video2)
videoplayer2.pack(expand=True, fill="both")
videoplayer2.set_size([720, 360])


play_pause_btn = tk.Button(window, text="Pause", command=play_pause)
play_pause_btn.pack(side = "left")

top_btn = tk.Button(window, text="Top wins!", command=top_wins)
top_btn.pack()

bottom_btn = tk.Button(window, text="Bottom wins!", command=bottom_wins)
bottom_btn.pack()

pass_btn = tk.Button(window, text="Pass", command=pass_next)
pass_btn.pack(side = "right")


videoplayer1.play()
videoplayer2.play()


videoplayer1.bind("<<Ended>>", loop1)
videoplayer2.bind("<<Ended>>", loop2)

window.mainloop()