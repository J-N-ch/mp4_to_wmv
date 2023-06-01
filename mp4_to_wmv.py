#!/usr/bin/python

# 20230601 Andrew Chen
# recommend using conda to create virtual-environment
# then install moviepy using pip in the virtual-environment
# please also refer to: https://pypi.org/project/moviepy/
# pip install moviepy==1.0.3

from moviepy.editor import *

# appoint input video
input__video = "./example.mp4"

# define output video
output_video = f"output_msmpeg4_qv1.wmv"

# read input video
video = VideoFileClip( input__video )

# define ffmpeg parameters to keep the video quality
ffmpeg_params_list=['-q:a', '4', '-q:v', '1', '-qmin', '1', '-qmax', '1']

# convert the video from mp4 to wmv 
video.write_videofile(
        f"output_msmpeg4_qv1.wmv",
        temp_audiofile = "temp-audio.m4a", 
        remove_temp = True, 
        codec = "msmpeg4", 
        audio_codec = "wmav2",
        ffmpeg_params = ffmpeg_params_list,
        )

