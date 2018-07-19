#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 生成个人简历js代码的主程序 '

__author__ = 'fslong'


import os
import re
import pdfkit


class Resume(object):
    def __init__(self):
        self.messageCode = ''
        self.htmlstrCode = ''

    def createJScode(self, htmlstr):
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
        messageCode = 'i+=1;showElementsByLine($("#contentbh3"),"%s",i) \n' % message
        htmlstr = htmlstr.replace('\"', '\'')
        htmlstr = 'i+=1;showElementsByLine($("#contentDiv"),"%s",i) \n' % htmlstr
        self.htmlstrCode = htmlstr
        # 如果message跟以前一样，那就不生成了，减少js的代码量；
        if self.messageCode == messageCode:
            return self.htmlstrCode
        else:
            self.messageCode = messageCode
            return self.messageCode+self.htmlstrCode

    def writeJScode(self):
        with open('content.html', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            htmlList = []
            htmlstr = ''
            jsCode = ''
            for line in lines:
                htmlstr += line.strip()
                if line.startswith('<!--'):
                    htmlList.append(htmlstr)
                else:
                    try:
                        line.split('>')[1]
                        htmlList.append(htmlstr)
                    except:
                        pass

            # 生成静态的简历页面：
            with open('indexHeader.html', 'r', encoding='utf-8') as f:
                indexHeader = f.read()
            with open('indexFooter.html', 'r', encoding='utf-8') as f:
                indexFooter = f.read()
            with open('indexStatic.html', 'w', encoding='utf-8') as f:
                f.write(indexHeader+htmlstr+indexFooter)
            for htmlstr in htmlList:
                jsCode += self.createJScode(htmlstr)
        jsCode = '\n$(function () { \nlet i=40;'+jsCode + \
            'i+=1; setTimeout(() => {$("#contentbh3").text("简历暂时写完了，谢谢大家！");}, i*100);i+=10; setTimeout(() => {$("#contentb").fadeOut("slow");}, i*100);});'
        with open('js/mainHeader.js', 'r', encoding='utf-8') as f:
            jsHeader = f.read()
        with open('js/main.js', 'w', encoding='utf-8') as f:
            f.write(jsHeader+jsCode)

    def createPDFfile(self):
        # 转换静态html文件到pdf：
        # 安装位置，需要修改为你的设备wkhtmltopdf软件安装位置
        pathWk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        pathFile = os.path.abspath('.')
        if os.path.isfile(os.path.join(pathFile, 'indexStatic.html')):
            self.writeJScode()
        config = pdfkit.configuration(wkhtmltopdf=pathWk)
        options = {
            'page-size': 'A4',  # Letter
            'minimum-font-size': 25,
            # 'image-dpi':1500, ###
            # 横向，注释掉就是纵向，详情请看：https://blog.csdn.net/u014644418/article/details/51584553
            'orientation': 'landscape',

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
            pdfkit.from_file(os.path.join(pathFile, 'indexStatic.html'), 'indexStatic.pdf',
                             configuration=config, options=options)
        except:
            if os.path.isfile(os.path.join(pathFile, 'indexStatic.html')):
                print('不好意思转换失败了。')
            else:
                print('咦？你把生成的静态网页删了呀，重新生成下！')


if __name__ == '__main__':
    myResume = Resume()
    myResume.writeJScode()
