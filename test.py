# -*- coding:utf-8 -*-
import json
dicts={"log_id": 4849472856538915803, "direction": 0, "words_result_num": 5, "words_result": [{"words": "目前世界上有多少人登上月"}, {"words": "球?"}, {"words": "11人"}, {"words": "12人"}, {"words": "14人"}]}
d1=json.dumps(dicts)
dict2=json.loads(d1)
def get_words(dicts):
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

question,A,B,C=get_words(dict2)
print question
print A
print B
print C
