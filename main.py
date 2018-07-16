#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 生成个人简历js代码的主程序 '

__author__ = 'fslong'


import os
import re


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


with open('content.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    htmlList = []
    htmlstr = ''
    jsCode = ''
    for line in lines:
        htmlstr += line.strip()
        # 由于<progress标签的问题，会出现奇怪的事情，所以，progress标签不进行打字输出：
        if line.strip().startswith('<progress'):
            pass
        else:
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
