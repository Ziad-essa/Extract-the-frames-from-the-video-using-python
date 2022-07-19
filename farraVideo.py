from moviepy.editor import VideoFileClip
import numpy as np
import os

SAVING_FRAMES_PER_SECOND = 10

def format_timedelta(td):
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def main(video_file,folderName):
    video_clip = VideoFileClip(video_file)
    os.mkdir(f'{folderName}')
    saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second
    i = 0
    for current_duration in np.arange(0, video_clip.duration, step):
        i=i +1
        frame_filename = os.path.join(folderName, f"frame{i}.jpg")
        video_clip.save_frame(frame_filename, current_duration)

main("assets/WhatsApp Video 2022-07-14 at 2.06.10 AM.mp4","ziad")