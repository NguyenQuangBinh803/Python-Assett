import numpy as np
import matplotlib.pyplot as plt
from IPython import display
import time

t = np.linspace(0, 10, num=601)
headerx = np.cos(2 * np.pi * t)
headery = np.sin(2 * np.pi * t)
count = 0

A = 1
B = 1

a = [1, 2, 3, 5]
b = [1, 2, 3, 5]
d = 0.5
D = -0

oldx = np.zeros((1, 16))
oldy = np.zeros((1, 16))

for i in t:
    count += 1
    tempx = []
    tempy = []

    f, axs = plt.subplots(nrows=5, ncols=5)
    f.set_size_inches(10, 10.5)

    for rows in range(4):
        for cols in range(4):
            x = np.exp(D * i) * np.sin(2 * np.pi * a[cols] * i / 10 + d * np.pi)
            y = np.exp(D * i) * np.sin(2 * np.pi * b[rows] * i / 10)

            scattery = -np.cos(2 * np.pi * a[cols] * i / 10 + d * np.pi)
            scatterx = np.cos(2 * np.pi * b[rows] * i / 10)

            tempx.append(x)
            tempy.append(y)

            linex = [-1, 1]
            liney = [-1, 1]

            if rows == 0:
                axs[rows, cols + 1].plot(headerx, headery, 'k-', lw=1);
                axs[rows, cols + 1].plot([x, x], [scattery, -1], 'r-', alpha=0.5);
                axs[rows, cols + 1].scatter(x, scattery, c='red', s=50);
                axs[rows, cols + 1].set_xticks([])
                axs[rows, cols + 1].set_yticks([])
                axs[rows, cols + 1].spines['top'].set_visible(False)
                axs[rows, cols + 1].spines['right'].set_visible(False)
                axs[rows, cols + 1].spines['bottom'].set_visible(False)
                axs[rows, cols + 1].spines['left'].set_visible(False)
                axs[rows, cols + 1].annotate('$%d$' % a[cols], xy=(0, 0),
                                             ha='center', va='center', fontsize=15)

            if cols == 0:
                axs[rows + 1, cols].plot(headerx, headery, 'k-', lw=1);
                axs[rows + 1, cols].plot([scatterx, 1], [y, y], 'r-', alpha=0.5);
                axs[rows + 1, cols].scatter(scatterx, y, c='red', s=50);
                axs[rows + 1, cols].set_xticks([])
                axs[rows + 1, cols].set_yticks([])
                axs[rows + 1, cols].spines['top'].set_visible(False)
                axs[rows + 1, cols].spines['right'].set_visible(False)
                axs[rows + 1, cols].spines['bottom'].set_visible(False)
                axs[rows + 1, cols].spines['left'].set_visible(False)
                axs[rows + 1, cols].annotate('$%d$' % b[rows], xy=(0, 0),
                                             ha='center', va='center', rotation='vertical',
                                             fontsize=15)

            if rows == 0 and cols == 0:
                axs[rows, cols].axis('off')
                axs[rows, cols].set_xlim([-1, 1])
                axs[rows, cols].set_ylim([-1, 1])
                axs[rows, cols].annotate('x0.1 Hz', xy=(0, 0),
                                         ha='center', va='center', fontsize=15)

            if count > 1:
                axs[rows + 1, cols + 1].plot(oldx[:, rows * 4 + cols], oldy[:, rows * 4 + cols], 'b-');

            axs[rows + 1, cols + 1].plot(linex, [y, y], 'r-', alpha=0.5)
            axs[rows + 1, cols + 1].plot([x, x], liney, 'r-', alpha=0.5)
            axs[rows + 1, cols + 1].scatter(x, y, c='red', s=50);
            axs[rows + 1, cols + 1].set_xlim((-1.1, 1.1));
            axs[rows + 1, cols + 1].set_ylim((-1.1, 1.1));
            axs[rows + 1, cols + 1].set_xticks([]);
            axs[rows + 1, cols + 1].set_yticks([]);

    # plt.suptitle('$ t = %.3f $s' %i)
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    plt.show()

    oldx = np.vstack((oldx, tempx))
    oldy = np.vstack((oldy, tempy))

    if count == 1:
        oldx = np.delete(oldx, (0), axis=0)
        oldy = np.delete(oldy, (0), axis=0)

    filename = 'images/' + str(count).zfill(4) + '.png'
    print(filename)

    f.savefig(filename, bbox_inches='tight', dpi=150)
    display.clear_output(wait=True);
    display.display(f);
    time.sleep(0.01)

i = 1
x = 1
y = 0
count = 601

linex = [-1, 1]
liney = [-1, 1]

for j in range(180):

    count += 1

    f, axs = plt.subplots(nrows=5, ncols=5);
    f.set_size_inches(10, 10.5);

    for rows in range(4):
        for cols in range(4):

            if j > 90:
                alpha = 0
            else:
                alpha = 1 - j / 90

            if rows == 0:
                axs[rows, cols + 1].plot(headerx, headery, 'k-', lw=1);
                axs[rows, cols + 1].plot([x, x], [y, -1], 'r-', alpha=0.5 * alpha);
                axs[rows, cols + 1].scatter(x, y, c='red', s=50, alpha=alpha);
                axs[rows, cols + 1].set_xticks([])
                axs[rows, cols + 1].set_yticks([])
                axs[rows, cols + 1].spines['top'].set_visible(False)
                axs[rows, cols + 1].spines['right'].set_visible(False)
                axs[rows, cols + 1].spines['bottom'].set_visible(False)
                axs[rows, cols + 1].spines['left'].set_visible(False)
                axs[rows, cols + 1].annotate('$%d$' % a[cols], xy=(0, 0),
                                             ha='center', va='center', fontsize=15)

            if cols == 0:
                axs[rows + 1, cols].plot(headerx, headery, 'k-', lw=1);
                axs[rows + 1, cols].plot([x, 1], [y, y], 'r-', alpha=0.5 * alpha);
                axs[rows + 1, cols].scatter(x, y, c='red', s=50, alpha=alpha);
                axs[rows + 1, cols].set_xticks([])
                axs[rows + 1, cols].set_yticks([])
                axs[rows + 1, cols].spines['top'].set_visible(False)
                axs[rows + 1, cols].spines['right'].set_visible(False)
                axs[rows + 1, cols].spines['bottom'].set_visible(False)
                axs[rows + 1, cols].spines['left'].set_visible(False)
                axs[rows + 1, cols].annotate('$%d$' % b[rows], xy=(0, 0),
                                             ha='center', va='center', rotation='vertical',
                                             fontsize=15)

            if rows == 0 and cols == 0:
                axs[rows, cols].axis('off')
                axs[rows, cols].set_xlim([-1, 1])
                axs[rows, cols].set_ylim([-1, 1])
                axs[rows, cols].annotate('x0.1 Hz', xy=(0, 0),
                                         ha='center', va='center', fontsize=15)

            if count > 1:
                axs[rows + 1, cols + 1].plot(oldx[:, rows * 4 + cols], oldy[:, rows * 4 + cols], 'b-');

            axs[rows + 1, cols + 1].plot(linex, [y, y], 'r-', alpha=0.5 * alpha)
            axs[rows + 1, cols + 1].plot([x, x], liney, 'r-', alpha=0.5 * alpha)
            axs[rows + 1, cols + 1].scatter(x, y, c='red', s=50, alpha=alpha);
            axs[rows + 1, cols + 1].set_xlim((-1.1, 1.1));
            axs[rows + 1, cols + 1].set_ylim((-1.1, 1.1));
            axs[rows + 1, cols + 1].set_xticks([]);
            axs[rows + 1, cols + 1].set_yticks([]);

    # plt.suptitle('$ t = %.3f $s' %i)
    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    plt.show()
    filename = 'images/' + str(count).zfill(4) + '.png'
    print(filename)

    f.savefig(filename, bbox_inches='tight', dpi=150)
    display.clear_output(wait=True);
    display.display(f);
    time.sleep(0.01)

import cv2
import numpy as np
import glob
from moviepy.editor import *

img_array = []
for i in range(781):
    filename = 'images/' + str(i + 1).zfill(4) + '.png'
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 60, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
