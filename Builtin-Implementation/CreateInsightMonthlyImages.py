import numpy as np
import os
import cv2
from datetime import datetime
import glob


class VideoCreatorImplement:
    def __init__(self):
        self.video_type = {
            'avi': cv2.VideoWriter_fourcc(*'XVID'),
            'mp4': cv2.VideoWriter_fourcc(*'XVID'),
        }
        self.std_dimension = {
            "480p": (640, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080),
            "4k": (3840, 2160),
        }
        self.date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        self.filename = self.date_time + '.avi'
        self.frames_per_second = 24.0
        self.res = '480p'


    def write_video_from_cam(self):
        pass

    def write_video_from_files(self, path):
        file_names = glob.glob(path + '*.jpg')
        print()
        for file in file_names:
            print(os.path.basename(file).split("_")[1])
            # self.video_writer = cv2.VideoWriter(file, self.video_type['avi'], 25, self.std_dimension['720p'])
            # image = cv2.imread(file)
            # image = cv2.putText(
            #     image,  # numpy array on which text is written
            #     self.date_time,  # text
            #     (10, 15),  # position at which writing has to start
            #     cv2.FONT_HERSHEY_SIMPLEX,  # font family
            #     0.5,  # font size
            #     (0, 250, 0, 255),  # font color
            #     1)  # font stroke
            # out.write(image)


if __name__ == "__main__":
    video_creator = VideoCreatorImplement()
    video_creator.write_video_from_files("E:/2020 - Images/")