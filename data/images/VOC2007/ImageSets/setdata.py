import os
import shutil 

xml_dir = '/home/numen/code/yolox-pytorch/data/images/VOC2007/Annotations/'
train_txt_path = '/home/numen/code/yolox-pytorch/data/images/VOC2007/ImageSets/train.txt'
val_txt_path = '/home/numen/code/yolox-pytorch/data/images/VOC2007/ImageSets/val.txt'
test_txt_path = '/home/numen/code/yolox-pytorch/data/images/VOC2007/ImageSets/test.txt'
save_path = '/home/numen/code/yolox-pytorch/data/images/VOC2007/'
img_path = '/home/numen/code/yolox-pytorch/data/images/VOC2007/JPEGImages/'

ftrain = open(test_txt_path)
lines = ftrain.readlines()
for line in lines:
    line = line.strip('\n')
    path_xml = xml_dir + line + '.xml'
    path_img = img_path + line + '.jpg'
    save_train = save_path + 'test2007/'
    shutil.move(path_xml,save_train)
    shutil.move(path_img,save_train)
    print(line)

ftrain.close()
