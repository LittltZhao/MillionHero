# -*- encoding:utf-8 -*-
import os
from PIL import Image
from aip import AipOcr
import pytesseract
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 720*1280分辨率坐标下题目及选项区域
body_width_720_start = 50
body_height_1280_start = 350
body_width_720_end = 1000
body_height_1280_end = 1200

# 720*1280分辨率下此区域是一片白色，以此判断是否是答题页面

default_width = 1080
default_height = 1280

negate_word = ['没有', '不是', '不会', '不包括', '不属于']

auxiliary_word = ['下列', '以下']

opt_aux_word = ['《', '》']

# 分辨答题页面,若是返回图片对象
def tell_and_get_image():
    os.system('adb shell screencap -p /sdcard/backup.png')
    os.system('adb pull /sdcard/backup.png image/backup.png')
    backup_img = Image.open('image/backup.png')
    return backup_img

def get_words(dicts):#得到题干和选项
    alls=dicts['words_result']
    lens=dicts['words_result_num']
    result=[]
    for i in alls:
        result.append(i['words'])
    # print result
    # print "*"*10
    A=result[-3]
    B=result[-2]
    C=result[-1]
    allOptions=[]
    for op in [A,B,C]:
        if op.startswith("《"):
            op=op[1:]
        if op.endswith("》"):
            op=op[:-1]
        allOptions.append(op)
    question=[]
    # print lens
    for i in range(lens-3):
        question.append(result[i])
    questions="".join(question)
    return questions,allOptions

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def image_to_str(image):
    # 2. 截取题目并文字识别
    crop_img = image.crop((body_width_720_start, body_height_1280_start, body_width_720_end, body_height_1280_end))
    crop_img.save('image/crop.png')
    APP_ID='10686924'
    API_KEY='GshQGrsllArrfpFWFcFEFDLc'
    API_SECRET='vZfA5ilznK9mBauhGf7Mne3GGM9kIiPO '
    aipOcr=AipOcr(APP_ID,API_KEY,API_SECRET)
    options = {
      'detect_direction': 'true',
      'language_type': 'CHN_ENG',
    }
    path='image/crop.png'
    ditcs=aipOcr.basicGeneral(get_file_content(path),options)
    # print ditcs
    question,optionArr=get_words(ditcs)
    return question,optionArr



def get_question(question):
    extra_word = negate_word + auxiliary_word
    is_negate = False
    for ele in extra_word:
        if ele in negate_word and ele in question:
            is_negate = True
        if ele in question:
            question = question.replace(ele, '')
    return question, is_negate


def get_result(result_list, option_arr, question, is_negate):
    answer_num = len(result_list)
    op_num = len(option_arr)
    source_arr = []  # 记录各选项得分
    for i in range(0, op_num):
        source_arr.append(0)
    for i in range(0, answer_num):
        result = result_list[i]
        for j in range(0, op_num):
            op = option_arr[j]
            if op in result:  # 选项在答案中出现一次，加10分
                source_arr[j] += 10
    if len(source_arr) == 0 or max(source_arr) == 0:
        return None
    if is_negate:
        best_index = min(source_arr)
    else:
        best_index = max(source_arr)
    best_result = option_arr[source_arr.index(best_index)]
    return best_result


if __name__ == '__main__':
    img=tell_and_get_image()
    question,optionArr=image_to_str(img)
    print question,','.join(optionArr)




