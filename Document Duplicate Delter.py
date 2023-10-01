## Get Packages #################################################
import numpy as np
import cv2 as cv
import os
import pdf2image
from tqdm import tqdm
from send2trash import send2trash

## Deleting PDFs ###############################################
def delete_pdf(root):
    # Get Root Directory
    path_list = []
    for file in tqdm(os.listdir(root), desc='Getting Files'):
        if '.pdf' in file:
            path_list.append(r'{}\{}'.format(root, file))
        else:
            pass

    # Remove Problematic Files (Optional)
    path_list.remove('C:\\Users\\druid\\Downloads\\AHTW5s05bhJ8N0nI83AmJn7cMENVryUlxPTFgNVjpgv6NUWnre-DKdr6yNT6WXE_BcD_e3P1wTYq4fetsGj3YHwb2IOQ2lP7utRq225I-6SVDCh__HJQnANllp6h1pRyN3p3yg0jSPdV88z6x_KsZmcD2po4p5lIufpVsXNjYcoWFSNnmH8BRsg8Zs6CUP9BpdFv3HrIFWtG255JDEh5gGIQ1Gj2fER-6Rbykolvem8mJPM2rv8khat_Hro.pdf')

    # Convert to Images
    image_list = []
    for path in tqdm(path_list, desc="Converting to Images"):
        temp = []
        img = pdf2image.convert_from_path(path)
        for i in range(len(img)):
            temp.append(np.asarray(img[i]))
        image_list.append(temp)

    # Delete Items
    delete = {}
    for i in tqdm(range(len(image_list)), colour='red', desc='Finding Duplicates'):
        for k in range(len(image_list)):
            tik = 0  # Tick marks for number of duplicate pages
            flag = False  # Reset flag for breaking the loop
            for j in range(len(image_list[i])):
                if flag:
                    break
                if len(image_list[i]) != len(image_list[k]):
                    flag = True
                    break
                else:
                    if i == k:
                        continue
                    for m in range(len(image_list[k])):
                        if flag:
                            break
                        # Add number to duplicates
                        if np.array_equiv(image_list[i][j], image_list[k][m]):
                            tik = tik + 1
                        # Check if they're the same length
                        if tik == len(image_list[i]) and i > k:
                            delete.append(path_list[i])
                            flag = True
                        if flag:
                            break

    delete = [*set(delete)]
    for item in delete:
        send2trash(item)

## Deleting Images #############################################################

def delete_img(root):
    path_list = []
    for file in tqdm(os.listdir(root), desc='Getting Files', colour = 'white'):
        if ('.png' or '.jpg') in file:
            path_list.append(r'{}\{}'.format(root, file))
        else:
            pass

    # Convert to Array
    image_list = [np.asarray(cv.imread(path)) for path in tqdm(path_list, desc = 'Converting to Array', colour = 'red')]

    # Delete Items
    delete = []
    for i in tqdm(range(len(image_list)), colour='blue', desc='Finding Duplicates'):
        flag = False
        for j in range(len(image_list)):
            if flag:
                break
            if image_list[i].shape != image_list[j].shape:
                flag = True
                break
            else:
                if i == k:
                    continue
                # Add number to duplicates
                if np.array_equiv(image_list[i], image_list[j]) and i > j:
                    delete.append(path_list[i])
                    flag = True
                if flag:
                    break

    delete = [*set(delete)]
    for item in delete:
        send2trash(item)