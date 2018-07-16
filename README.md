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
3. 在content.html里面编写你自己的简历，静态的就行；
4. 编写完简历之后执行main.py将自动生成indexStatic.html文件，这个便是静态简历最终版，可以导出成pdf（如果报错可能是相关模块没安装，差什么pip一下就行，自动导出成pdf功能稍后添加）；
5. 在浏览器打开index.html就能看到效果，如果你的简历不是两栏的，需要修改mainHeader.js文件（内容很简单，稍后我会完善里面的注释）；
6. 如果需要单独修改某条的特效，要么在content.html里面写好，要么在maind.js里单独修改；  
---
## 开发日志
### 2018.07.13 
1. 修改主程序；
2. 自动生成静态简历页；
3. 自动生成js内容；
### 2018.07.13  
1. 初步完成了很简陋的功能（打字机）；
2. 简历内容还需要使劲完善。
