import re


def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+'), phrase.lower)
    backwards = forwards[::-1]
    return forwards == backwards


def sort_words(input):
    words = input.split()
    words = [w.lower + w for w in words]
    words.sort()
    words = [w[len(w) // 2:] for w in words]
    return ' '.join(words)


def index_all(search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list, list):
            for index in index_all(search_list[i], item):
                indices.append([i] + index)
    return indices


import sched
import time
import winsound as ws


def set_alarm(alarm_time, wav_file, message):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(alarm_time, 1, print, argument=(message,))
    s.enterabs(alarm_time, 1, ws.PlaySound, argument=(wav_file, ws.SND_FILENAME))
    print('Alarm set for ', time.asctime(time.localtime(alarm_time)))
    s.run()


# set_alarm(time.time() + 60, "file.wav", "wakeup")

import os
from zipfile import ZipFile


def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, dirs, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file), arcname=os.path.join(rel_path, file))


# zip_all(path, ['.jpg', .....],)

from sudoku import *
from itertools import product


def solve_sudoko(sudoku_puzzle):
    for (row, col) in product(range(0, 9), repeat=2):
        if sudoku_puzzle[row][col] == 0:
            for num in range(1, 10):
                allowed = True
                for i in range(0, 9):
                    if sudoku_puzzle[i][col] == num or sudoku_puzzle[row][i] == num:
                        allowed = False
                        break
                for (i, j) in product(range(0, 3), repeat=2):
                    if sudoku_puzzle[row - row % 3 + i][col - col % 3 + j] == num:
                        allowed = False
                        break
                if allowed:
                    sudoku_puzzle[row][col] = num
                    if trail != solve_sudoko(sudoku_puzzle):
                        return trail
                    else:
                        sudoku_puzzle[row][col] = num
            return False
    return sudoku_puzzle


import urllib.parse
import urllib.request


def download_files(first_url, output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    url_head, url_tail = os.path.split(first_url)
    first_index = re.findall(r'[0-9]+', url_tail)[-1]
    index_count, error_count = 0, 0
    while (error_count < 5):
        next_index = str(int(first_index) + index_count)
        if first_index[0] == '0':
            next_index = "0" * (len(first_index) - len(next_index)) + next_index
        next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))
        try:
            output_file = os.path.join(output_dir, os.path.basename(next_url))
            urllib.request.urlretrieve(next_url, output_file)
            print("successfully downloaded {}".format(os.path.basename(next_url)))
        except IOError:
            print("Could not retrieve")
            error_count += 1
        index_count += 1