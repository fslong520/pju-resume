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
            message=i.split('--')[1]
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
    message = 'i+=1; setTimeout(() => {$("#contentbh3").text("%s");}, i*100);' % message
    htmlstr = htmlstr.replace('\"', '\'')

    return message+'i+=1; setTimeout(() => {$("#contentDiv").html("%s");}, i*100);' % htmlstr


with open('content.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    htmlList = []
    htmlstr = ''
    jsCode = ''
    for line in lines:
        htmlstr += line.strip()
        htmlList.append(htmlstr)
    for htmlstr in htmlList:
        jsCode += createJScode(htmlstr)
jsCode = '\n$(function () { let i=40;'+jsCode + \
    'i+=1; setTimeout(() => {$("#contentbh3").text("简历暂时写完了，谢谢大家！");}, i*100);i+=10; setTimeout(() => {$("#contentb").fadeOut("slow");}, i*100);});'
with open('js/main.js', 'a', encoding='utf-8') as f:
    f.write(jsCode)
