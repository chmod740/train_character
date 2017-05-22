from random import choice
import os
from PIL import Image
import matplotlib.pyplot as plt

# 读取训练文件
rootdir  = "d:\\COCO-Text-words-trainval\\train_words"
mapping_file = "D:\\COCO-Text-words-trainval\\train_words_gt.txt"

max_result_length = 20

img_list = []
def gen_img_list():
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
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

def gen_text_and_image():
    text = choice(img_list)
    # 读取文件夹中每一张图片
    captcha_image = Image.open(rootdir + "\\" + text + ".jpg")
    # 重新设置每张图片的大小，个人建议 需要改改
    captcha_image = captcha_image.resize((160, 60))
    try:
        text = img_map[text]
    except:
        # 递归的读取文件中的每张图片
        gen_text_and_image()

    if len(text) > max_result_length:
        return gen_text_and_image()
    else:
        return text, captcha_image


# 主函数
if __name__ == '__main__':
    text, image = gen_text_and_image()

    f = plt.figure()
    ax = f.add_subplot(111)
    ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
    plt.imshow(image)
    plt.show()

