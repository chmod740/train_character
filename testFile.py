from random import choice
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 读取测试文件
rootdir  = "D:\\COCO-Text-words-trainval\\val_words"
mapping_file = "D:\\COCO-Text-words-trainval\\val_words_gt.txt"

max_result_length = 20

img_list = []
def gen_img_list():
    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames: # 输出文件信息
            img_list.append(filename.replace(".jpg", ""))
    return img_list
gen_img_list()

img_map = {}
def gen_img_map():
    file = open(mapping_file, encoding='utf-8')
    for s in file:
        s = s.replace("\r\n", "\n").replace("\n", "")
        if s != "":
            img_map[s.split(",")[0]] = s.replace(s.split(",")[0] + ",", "")
gen_img_map()

# def gen_text_and_image():
#     text = choice(img_list)
#     # 读取文件夹中每一张图片
#     captcha_image = Image.open(rootdir + "\\" + text + ".jpg")
#     # 重新设置每张图片的大小，个人建议 需要改改
#     captcha_image = captcha_image.resize((160, 60))
#     try:
#         text = img_map[text]
#     except:
#         # 递归的读取文件中的每张图片
#         gen_text_and_image()
#
#     if len(text) > max_result_length:
#         return gen_text_and_image()
#     else:
#         return text, captcha_image
def get_test_length():
    return len(img_map)

def gen_test_text_and_image(i):
    if i >= len(img_list):
        return None, None
    text = img_list[i]
    i += 1
    if i >= len(img_list):
        return None,None
    captch_image = Image.open(rootdir + "\\" + text + ".jpg")
    captch_image = captch_image.resize((160, 60))
    captch_image = np.array(captch_image)
    try:
        text = img_map[text]
    except:
        return None, None
    if len(text) > max_result_length:
        return None, None
    else:
        return text, captch_image

# 主函数
if __name__ == '__main__':
    text, image = gen_text_and_image()
    f = plt.figure()
    ax = f.add_subplot(111)
    ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
    plt.imshow(image)
    plt.show()

