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
        self.date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.filename = self.date_time + '.avi'
        self.frames_per_second = 24.0
        self.res = '480p'
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv2.VideoWriter(self.filename, self.video_type['avi'], 2, self.std_dimension['720p'])

    def write_video_from_cam(self):
        pass

    def write_video_from_files(self, path):
        ''''
        There are 2 problems to perform this function,
        1: The size of the input images is vary and unmatch with the video writer
        2:
        '''
        file_names = glob.glob(path + '*.jpg')
        prev_month = 0
        print("[" + " " * 100 + "]")
        length_of_files = len(file_names)
        step = int(100 / length_of_files)
        print("[")
        progress = 0
        prev_shape = None
        for file in file_names:
            # print(os.path.basename(file).split("_")[1])
            file_date = os.path.basename(file).split("_")[1]
            year, month, date = file_date[0:4], file_date[4:6], file_date[6:]
            # print(year, month, date)
            time_string = str(date) + "/" + str(month) + "/" + str(year)
            image = cv2.imread(file)
            if not prev_shape or prev_shape != image.shape:
                prev_shape = image.shape
                print(image.shape)

            # image = cv2.resize(image, ((1280, 720)))

            image = cv2.putText(
                image,  # numpy array on which text is written
                time_string,  # text
                (10, 25),  # position at which writing has to start
                cv2.FONT_HERSHEY_SIMPLEX,  # font family
                1,  # font size
                (255, 0, 0, 255),  # font color
                2)  # font stroke
            self.video_writer.write(image)
            progress += 1
            if progress >= step:
                print("\\", end='')
                progress = 0
            # if int(month) > 1 :
            #     break

        print("]")
        print("Done")
        self.video_writer.release()

    def write_images_to_folder(self, path):
        '''
        2: Problem with
        :param path:
        :return:
        '''
        os.mkdir(self.date_time)
        file_names = glob.glob(path + '*.jpg')

        for file in file_names:
            # Setup output file
            image = cv2.imread(file)
            original_file = os.path.basename(file)
            output_file_path = self.date_time + "/" + original_file

            # Setup datetime string
            file_date, file_time = os.path.basename(file).split("_")[1:3]
            date_string = file_date[6:] + "/" + file_date[4:6] + "/" + file_date[0:4]
            time_string = file_time[0:2] + ":" + file_time[2:4] + ":" + file_time[4:]
            datetime_string = date_string + " - " + time_string

            image = cv2.putText(image, datetime_string, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255, 255), 4)
            print(output_file_path)
            cv2.imwrite(output_file_path, image)


if __name__ == "__main__":
    video_creator = VideoCreatorImplement()
    video_creator.write_images_to_folder("E:/2020 - Images/")
