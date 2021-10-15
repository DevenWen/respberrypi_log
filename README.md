# respberrypi_log
记录自己玩树莓派的日志

* 规格：4B，8G
* 官方[网站](https://www.raspberrypi.com/)

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

# 1. 烧录系统

1.1 直接通过 TF 卡烧录了 64bit 的操作系统，在 BOOT 目录中。整个过程非常方便，让人很惊艳。步骤也比较简单
1. 在官方网站下载镜像和写镜像工具
2. 写镜像
3. 在 /boot 目录添加 ssh、wifi 的配置（参考 Log 2.2）
4. 插入 rasp pi，通电，重启

> 官方文档提供了一个[极其简单漂亮的 Video](https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager)。

1.2 Docker 的安装可以参考，过程比较顺利。docker 安装完成后并不能马上启用，但 reboot 后就可以了。[参考](https://phoenixnap.com/kb/docker-on-raspberry-pi)

## 2. 64bit OS 的缺陷与重装

2.1 今晚花了点时间组装摄像头，后来发现 64bit 的 respberry OS 是不支持 raspistill 工具的。参考：[官方 64bit-OS 反馈贴](https://forums.raspberrypi.com/viewtopic.php?p=1729089#p1729089) 

2.2 鉴于考虑到 32bit 才是稳定的版本，故重刷 32bit 的系统到 TF 卡里。（重新下单了一个 64 GB的 TF 卡，以后长期用于树莓派，128G 的后面继续用于 64bit 的OS，毕竟 Docker 还是有用的），刷系统的时候，需要考虑 ssh 开启和 wifi 的自动连接。因为我没有显示器，故需要[参考此贴](https://shumeipai.nxez.com/2018/08/31/raspberry-pi-vnc-viewer-configuration-tutorial.html
)

2.3 32bit 一开始遇到 VNC 连接桌面失败问题，参考了一下[博客](https://www.tomshardware.com/how-to/fix-cannot-currently-show-desktop-error-raspberry-pi)，调整一下显示器的分辨率就可以。

2.4 后面还会花一点时间去了解 OpenCV。python 库安装的时候最好使用国内的源，就像这样： `pip3 install package -i https://pypi.tuna.tsinghua.edu.cn/simple/` ，[参考](https://zhuanlan.zhihu.com/p/124311177)

2.5 树莓派实验室，是最近几天看到的比较好的[树莓派中文网站](https://shumeipai.nxez.com/) 

2.6 最后摄像头的模块在 32bit OS 上测试通过，期待后面的功能
