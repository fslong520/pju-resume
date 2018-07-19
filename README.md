# pju-resume
An online resume frame by Pyrhon+jQuery+UIkit.  
这是本人写的一个简历框架（开的新坑），主要是一个动态的类似打字机效果的简历（后续可能会放更多的特效）。  

---  
## 运行效果 
![简历效果图初步.gif](https://i.loli.net/2018/07/16/5b4bf047f2e55.gif)<!--删除连接：https://sm.ms/delete/DokAaLfv28dP5VJ-->    

---  
## 使用说明
1. 克隆仓库到本地；
2. 修改index.html、indexHeader.html里的title标签为自己的简历；
3. 在content.html里面编写你自己的简历，静态的就行(**注意：因为解析网页数据的时候是逐行解析的，所以只需要把想在同一时间显示的代码放在同一行即可。**)；
4. 编写完简历之后执行main.py将自动生成indexStatic.html文件，这个便是静态简历最终版，同时也导出同名pdf文件（如果报错可能是相关模块没安装，差什么pip一下就行；如果提示导出pdf失败，那就是没有安装pdfkit或者wkhtmltox软件，检查下哪个没安装，如果是pdfkit没安装，用pip安装一下即可，如果是wkhtmltox没安装请访问其官网（ [wkhtmltox官网](https://wkhtmltopdf.org/downloads.html)）安装，如果是在Linux环境下运行或wkhtmltopdf没安装在默认目录，需要进入main.py修改`path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'`为你的设备中wkhtmltopdf的安装位置。）；
5. 在浏览器打开index.html就能看到效果，如果你的简历不是两栏的，需要修改mainHeader.js文件（内容很简单，稍后我会完善里面的注释）；
6. 如果需要单独修改某条的特效，要么在content.html里面写好，要么在maind.js里单独修改；   

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
