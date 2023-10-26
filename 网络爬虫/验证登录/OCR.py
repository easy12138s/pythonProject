# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: OCR.py
    @time: 2023/10/23 15:27
"""
from PIL import Image
import pytesseract
import ddddocr

def image_ocr(path):
    # 普通版ocr，识别准确率较低

    # 打开图片
    image = Image.open(path)

    # 识别图片中的文字
    text = pytesseract.image_to_string(image)
    return  "识别结果：" + text

def image_ddocr(path):
    # 进阶版 识别率高
    with open(path, 'rb') as f:
        image = f.read()
        ocr = ddddocr.DdddOcr()
        text = ocr.classification(image)
    return text

if __name__ == '__main__':
    identify_data = image_ddocr('./images/topcheer.png')
    print(identify_data)