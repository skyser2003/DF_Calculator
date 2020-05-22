import cv2
import numpy as np
import os
from PIL import Image
from PIL import ImageTk
from PIL import ImageEnhance
import time

def img_gif(item_code,value):
    imgtk=[]
    if value==0: ## 신화
        len_gif=12
    elif value==1: ## 시로코
        len_gif=22
    for i in range(0,len_gif):
        effect = cv2.imread('image_effect/'+str(value)+str(i)+'.PNG')

        if value==1:
            effect=effect[1:27,1:27]

        item = cv2.imread('image/'+str(item_code)+'n.PNG')
        item_cut=item[1:27,1:27]

        temp_img = cv2.addWeighted(effect, 40/100, item_cut, 60/100, 0)
        item[1:27,1:27]=temp_img
        item = cv2.cvtColor(item, cv2.COLOR_BGR2RGB)
        temp_img2 = Image.fromarray(item)
        enhancer=ImageEnhance.Brightness(temp_img2).enhance(1.5)
        imgtk.append(ImageTk.PhotoImage(image=enhancer))

    return imgtk

def make_skill_tag(fillname):
    try:
        img = Image.open('skillDB/skill_img/'+str(fillname))
    except:
        img = Image.open('skillDB/skill_talisman/'+str(fillname))
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] > 245 and item[1] > 245 and item[2] > 245:
            newData.append((item[0], item[1], item[2], 0))
        else:
            newData.append(item)
    img.putdata(newData)
    print(type(img))
    img.save('skillDB/skill_img/'+str(fillname))

def make_skill_bling(fillname,value):
    print(fillname)
    # ff = np.fromfile(imagePath, np.uint8)
    # img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
    if value=="normal":
        file_path='skillDB/skill_img/'+str(fillname)
        ff = np.fromfile(file_path, np.uint8)
        item = cv2.imdecode(ff, 1)
        effect = cv2.imread('skillDB/skill_normal.png', 1)
        save_path='skillDB/skill_img/'
    elif value=="talisman":
        file_path='skillDB/skill_talisman/'+str(fillname)
        ff = np.fromfile(file_path, np.uint8)
        item = cv2.imdecode(ff, 1)
        effect = cv2.imread('skillDB/skill_talisman.png', 1)
        save_path='skillDB/skill_talisman/'
    for i in range(1,27):
        for j in range(1,27):
            effect[i,j]=item[i,j]

    imwrite(file_path,effect)

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)
        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
                return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def auto_run():
    path = "skillDB/skill_img"
    file_list = os.listdir(path)

    for now in file_list:
        make_skill_tag(now)

    path = "skillDB/skill_talisman"
    file_list = os.listdir(path)

    for now in file_list:
        make_skill_tag(now)

def auto_run2():
    path = "skillDB/skill_img"
    file_list = os.listdir(path)

    for now in file_list:
        make_skill_bling(now,'normal')

    path = "skillDB/skill_talisman"
    file_list = os.listdir(path)

    for now in file_list:
        make_skill_bling(now,'talisman')


if __name__ == "__main__":
    auto_run2()
    auto_run()
    
