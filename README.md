# respberrypi_log
记录自己玩树莓派的日志

规格：4B，8G

## TODO list
- [x] 烧录系统
- [x] 安装 Docker
- [ ] 学习面包版和接线，点亮小灯
- [ ] 学习接线，编写一个智能风扇
- [x] 学习摄像头，小功能待定
- [ ] 申请域名，接入公网
- [ ] 里程碑：Welcome Page，通过摄像头，实时记录一张图片到 Http 服务器中，可以通过公网访问这个主页，并定时更新 Readme 内容到主页中？（目的是让访问者可以观察到我的计划）
- [ ] 将此网站和公众号进行联动（联动内容暂未定）
- [ ] 学习 motor 相关驱动，步进电机？FOC控制板？Think More
- [ ] 学习 Python 的 OpenCV 库，学习人脸识别
- [ ] 学习 距离传感器
- [ ] 里程碑：制作一个遥控小车
- [ ] 里程碑：制作一个自动驾驶小车
 
## 库
- [ ] python 邮件模块
- [ ] python OpenCV

## 烧录系统 LOG
直接通过 TF 卡烧录了 64bit 的操作系统，在 BOOT 目录中。整个过程非常方便，让人很惊艳。

## 64bit OS 的缺陷
* 今晚花了点时间组装摄像头，后来发现 64bit 的 respberry OS 是不支持 raspistill 工具的。 https://forums.raspberrypi.com/viewtopic.php?p=1729089#p1729089
* 鉴于考虑到 32bit 才是稳定的版本，故重刷 32bit 的系统到 TF 卡里。（重新下单了一个 64 GB的 TF 卡，以后长期用于树莓派，128G 的后面继续用于 64bit 的OS，毕竟 Docker 还是有用的），刷系统的时候，需要考虑 ssh 开启和 wifi 的自动连接。因为我没有显示器，故需要参考：https://shumeipai.nxez.com/2018/08/31/raspberry-pi-vnc-viewer-configuration-tutorial.html
* 32bit 一开始遇到 VNC 连接桌面失败问题，参考了一下博客，调整一下显示器的像素就可以。https://www.tomshardware.com/how-to/fix-cannot-currently-show-desktop-error-raspberry-pi
* 后面还会花一点时间去了解 OpenCV。python 库安装的时候最好使用国内的源，就像这样： `pip3 install package -i https://pypi.tuna.tsinghua.edu.cn/simple/` https://zhuanlan.zhihu.com/p/124311177
* 最后摄像头的模块在 32bit OS 上测试通过，期待后面的功能
* 树莓派实验室，是最近几天看到的比较好的树莓派中文网站 https://shumeipai.nxez.com/
