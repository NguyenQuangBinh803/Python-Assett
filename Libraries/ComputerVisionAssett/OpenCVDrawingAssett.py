import cv2
import numpy as np
import os

def draw_rounded_rectangle(src, top_left, bottom_right, radius=1, color=255, thickness=1, line_type=cv2.LINE_AA,
                           complete=True):
    #  corners:
    #  p1 - p2
    #  |     |
    #  p4 - p3

    p1 = top_left
    p2 = (bottom_right[1], top_left[1])
    p3 = (bottom_right[1], bottom_right[0])
    p4 = (top_left[0], bottom_right[0])

    height = abs(bottom_right[0] - top_left[1])

    if radius > 1:
        radius = 1

    corner_radius = int(radius * (height / 2))

    if thickness < 0:
        # big rect
        top_left_main_rect = (int(p1[0] + corner_radius), int(p1[1]))
        bottom_right_main_rect = (int(p3[0] - corner_radius), int(p3[1]))

        top_left_rect_left = (p1[0], p1[1] + corner_radius)
        bottom_right_rect_left = (p4[0] + corner_radius, p4[1] - corner_radius)

        top_left_rect_right = (p2[0] - corner_radius, p2[1] + corner_radius)
        bottom_right_rect_right = (p3[0], p3[1] - corner_radius)

        all_rects = [
            [top_left_main_rect, bottom_right_main_rect],
            [top_left_rect_left, bottom_right_rect_left],
            [top_left_rect_right, bottom_right_rect_right]]

        [cv2.rectangle(src, rect[0], rect[1], color, thickness) for rect in all_rects]

    if complete:
        # draw straight lines
        cv2.line(src, (p1[0] + corner_radius, p1[1]), (p2[0] - corner_radius, p2[1]), color, abs(thickness), line_type)
        cv2.line(src, (p2[0], p2[1] + corner_radius), (p3[0], p3[1] - corner_radius), color, abs(thickness), line_type)
        cv2.line(src, (p3[0] - corner_radius, p4[1]), (p4[0] + corner_radius, p3[1]), color, abs(thickness), line_type)
        cv2.line(src, (p4[0], p4[1] - corner_radius), (p1[0], p1[1] + corner_radius), color, abs(thickness), line_type)

    # draw arcs
    cv2.ellipse(src, (p1[0] + corner_radius, p1[1] + corner_radius), (corner_radius, corner_radius), 180.0, 0, 90,
                color, thickness, line_type)
    cv2.ellipse(src, (p2[0] - corner_radius, p2[1] + corner_radius), (corner_radius, corner_radius), 270.0, 0, 90,
                color, thickness, line_type)
    cv2.ellipse(src, (p3[0] - corner_radius, p3[1] - corner_radius), (corner_radius, corner_radius), 0.0, 0, 90, color,
                thickness, line_type)
    cv2.ellipse(src, (p4[0] + corner_radius, p4[1] - corner_radius), (corner_radius, corner_radius), 90.0, 0, 90, color,
                thickness, line_type)

    return src


def draw_blur_region(image, top_left, bottom_right, shape):
    mask = np.zeros(image.shape)
    if shape == "RECTANGLE":
        cv2.rectangle(mask, top_left, bottom_right, (255, 255, 255), -1)
        mask = cv2.GaussianBlur(mask, (51, 51), 0)
    elif shape == "ELIPSE":
        pass
    return image*(mask/255)


def decorate_background_text(file_name):
    image = cv2.imread(file_name)
    file_name = os.path.basename(file_name)
    file_date, file_time = file_name.split("_")[1:3]
    date_string = file_date[6:] + "/" + file_date[4:6] + "/" + file_date[0:4]
    time_string = file_time[0:2] + ":" + file_time[2:4] + ":" + file_time[4:]
    datetime_string = date_string + " - " + time_string

    scale = 3
    mask = np.ones(image.shape, dtype=np.uint8)
    mask = mask * 255
    cv2.rectangle(mask, (2, 2), (420 * scale, 38 * scale), (0, 0, 0), -1)
    image = cv2.addWeighted(image, 1.0, mask, 0.15, 1)
    image = cv2.putText(image, datetime_string, (10 * scale, 30 * scale), cv2.FONT_HERSHEY_SIMPLEX, scale,
                        (255, 255, 255, 255), 3)
    return image


if __name__ == "__main__":
    top_left = (200, 200)
    bottom_right = (500, 500)
    color = (255, 255, 255)
    image_size = (800, 800, 3)
    img = np.zeros(image_size)
    img = draw_rounded_rectangle(img, top_left, bottom_right, color=color, radius=0.25, thickness=2, complete=False)

    cv2.imshow('rounded_rect', img)
    cv2.imshow('blur_region', draw_blur_region(img, top_left,bottom_right, "RECTANGLE"))
    cv2.waitKey(0)
