# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2382019442@qq.com
    @software: PyCharm
    @file: OCR.py
    @time: 2023/10/23 15:27
"""
from PIL import Image
import pytesseract

def image_identify(path):
    # 打开图片
    image = Image.open(path)

    # 识别图片中的文字
    text = pytesseract.image_to_string(image)
    return  "识别结果：" + text

if __name__ == '__main__':
    identify_data = image_identify('./images/img_1.png')
    print(identify_data)