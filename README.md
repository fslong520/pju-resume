# pju-resume
An online resume frame by Pyrhon+jQuery+UIkit.  
这是本人写的一个简历框架（开的新坑），主要是一个动态的类似打字机效果的简历（后续可能会放更多的特效），使用说明详见[wiki页](https://github.com/fslong520/pju-resume/wiki/使用说明)。    
---  
## 运行效果 
![简历效果图初步.gif](https://i.loli.net/2018/07/16/5b4bf047f2e55.gif)<!--删除连接：https://sm.ms/delete/DokAaLfv28dP5VJ-->     
---  
## bug与后续计划
### bug与不友好的地方
1. 生成的pdf格式有问题，一些样式、分栏会很奇怪（有些js代码控制的样式没执行）；
2. 修改简历比较麻烦；
### 计划
1. 进一步封装各个方法、类；
2. 可以使用markdown编辑简历或者文章，然后再生成（感觉这种模式更加适合使用markdown写的文章）；
3. 未完待续...    
---
*参考文献：*  
> [1、wkhtmltopdf 中文参数详解](https://blog.csdn.net/u014644418/article/details/51584553)  
> [2、python--生成pdf](https://www.jianshu.com/p/91fa0420f621)   
---
## 开发日志
### 2018.07.19 
1. 科四过了，重新封装了一下大部分的方法和函数；
2. 优化逻辑，大幅减少js代码量；
### 2018.07.16 
1. 修改主程序；
2. 自动生成静态简历页；
3. 自动生成js内容；
4. 自动生成pdf文档（存在bug）；
### 2018.07.13  
1. 初步完成了很简陋的功能（打字机）；
2. 简历内容还需要使劲完善。
