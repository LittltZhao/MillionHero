# 百万英雄助手说明
HQ类答题游戏辅助（python）

如百万英雄、冲顶大会、芝士超人等HQ类答题游戏辅助。原理同前一阵大火的[跳一跳辅助](https://github.com/wangshub/wechat_jump_game)类似，将答题页面截图，然后使用图片识别功能转成文字，再放到百度去搜索。

截图使用的是adb,所以目前仅支持android。图片识别使用的是Baidu-OCR之前用的是Tesseract，但是中文识别正确率太低，导致搜索结果很差
# 步骤
##1.安装adb驱动
##2.安装百度ocr(`pip install baidu-aip`)
##3.安装相应的库(PIL等)
##4.运行main.py


