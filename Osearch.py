# -*- encoding:utf-8 -*-
from aip import AipOcr
APP_ID='10686924'
API_KEY='GshQGrsllArrfpFWFcFEFDLc'
API_SECRET='vZfA5ilznK9mBauhGf7Mne3GGM9kIiPO '
aipOcr=AipOcr(APP_ID,API_KEY,API_SECRET)
options = {
  'detect_direction': 'true',
  'language_type': 'CHN_ENG',
}
path='image/crop.png'
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_words(dicts):#得到题干和选项
    alls=dicts['words_result']
    result=[]
    for i in alls:
        result.append(i['words'])
    A=result[-1]
    B=result[-2]
    C=result[-3]
    question=''
    lens=len(result)
    for i in range(lens-3):
        question=question.join(result[i])
    return question,A,B,C

result=aipOcr.basicGeneral(get_file_content(path),options)#字典类型
print result
question,A,B,C=get_words(result)
print question
print A
print B
print C



