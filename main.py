#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 生成个人简历js代码的主程序 '

__author__ = 'fslong'


import os
import re
import pdfkit


def createJScode(htmlstr):
    elementsList = re.findall(r'<.*?>', htmlstr)
    elementsListLeft = []
    elementsListRight = []
    message = ''
    for i in elementsList:
        if re.match(r'</.*?>', i):
            elementsListRight.append(i)
        else:
            elementsListLeft.append(i)
    for i in elementsListLeft:
        if i.startswith('<!--'):
            message = i.split('--')[1]
    elementsListLeft = elementsListLeft[::-1]
    if len(elementsListLeft) > len(elementsListRight):
        i = len(elementsListRight)
        while i < len(elementsListLeft):
            j = elementsListLeft[i]
            if j.startswith('<img')or j.startswith('<input') or j.startswith('<br') or j.startswith('<hr') or j.startswith('<!--'):
                pass
            else:
                if re.match(r'(.*?)(\s)', elementsListLeft[i]):
                    htmlstr += '</' + \
                        elementsListLeft[i].split(' ')[0][1:]+'>'
                else:
                    htmlstr += '</' + \
                        elementsListLeft[i].split(' ')[0][1:]
            i += 1
    message = 'i+=1; setTimeout(() => {$("#contentbh3").text("%s");}, i*100);\n' % message
    htmlstr = htmlstr.replace('\"', '\'')

    return message+'i+=1; setTimeout(() => {$("#contentDiv").html("%s");}, i*100);\n' % htmlstr


if __name__ == '__main__':
    with open('content.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        htmlList = []
        htmlstr = ''
        jsCode = ''
        for line in lines:
            htmlstr += line.strip()
            htmlList.append(htmlstr)
        # 生成静态的简历页面：
        with open('indexHeader.html', 'r', encoding='utf-8') as f:
            indexHeader = f.read()
        with open('indexFooter.html', 'r', encoding='utf-8') as f:
            indexFooter = f.read()
        with open('indexStatic.html', 'w', encoding='utf-8') as f:
            f.write(indexHeader+htmlstr+indexFooter)
        for htmlstr in htmlList:
            jsCode += createJScode(htmlstr)
    jsCode = '\n$(function () { \nlet i=40;'+jsCode + \
        'i+=1; setTimeout(() => {$("#contentbh3").text("简历暂时写完了，谢谢大家！");}, i*100);i+=10; setTimeout(() => {$("#contentb").fadeOut("slow");}, i*100);});'
    with open('js/mainHeader.js', 'r', encoding='utf-8') as f:
        jsHeader = f.read()
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(jsHeader+jsCode)
    a = input('是否同时生成pdf文件？\n目前还是有些bug，如果你的简历分两栏，会变成一栏，感觉是一些css样式的问题，尚未解决。y/n?\n')
    if a == 'y':
        # 转换静态html文件到pdf：
        # 安装位置，需要修改为你的设备wkhtmltopdf软件安装位置
        path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wk)
        options = {
            'page-size': 'A4',  # Letter
            'minimum-font-size': 25,
            # 'image-dpi':1500, ###
            'orientation': 'landscape',### 横向，注释掉就是纵向，详情请看：https://blog.csdn.net/u014644418/article/details/51584553

            'margin-top': '0.1in',  # 0.75in
            'margin-right': '0.1in',
            'margin-bottom': '0.1in',
            'margin-left': '0.1in',
            'encoding': 'UTF-8',  # 支持中文
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }
        try:
            path = os.path.join(os.path.abspath('.'), 'indexStatic.html')
            print(path)
            pdfkit.from_file(path, 'indexStatic.pdf',
                             configuration=config, options=options)
        except:
            print('转换失败，请查看相关代码问题。')
    else:
        print('转换完毕！')
