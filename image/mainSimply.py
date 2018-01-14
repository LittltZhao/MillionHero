# -*- encoding:utf-8 -*-
import sys
import analyze
import search
reload(sys)
sys.setdefaultencoding('utf8')

def main():
    img = analyze.tell_and_get_image()
    question,option_arr = analyze.image_to_str(img)  # 图片转文字
    question, is_negative = analyze.get_question(question)  # 得到题目、选项及题目正反
    result_list = search.search(question)  # 搜索结果
    print
    print question
    print "选项:",','.join(option_arr)
    best_result = analyze.get_result(result_list, option_arr, question, is_negative)  # 分析结果
    if best_result is None:
        print('\n没有答案')
    else:
        print('最佳答案是： \033[1;31m{}\033[0m'.format(best_result))

if __name__ == '__main__':
        main()
