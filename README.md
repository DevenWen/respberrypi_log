# respberrypi_log
记录自己玩树莓派的日志

* 规格：4B，8G
* 官方[网站](https://www.raspberrypi.com/)

## TODO list
- [x] 烧录系统
- [x] 安装 Docker
- [x] 学习面包版和接线，点亮小灯
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
- [x] python OpenCV，[Google meidapipe](https://google.github.io/mediapipe/)

# 1. 烧录系统

1.1 直接通过 TF 卡烧录了 64bit 的操作系统，在 BOOT 目录中。整个过程非常方便，让人很惊艳。步骤也比较简单
1. 在官方网站下载镜像和写镜像工具
2. 写镜像
3. 在 /boot 目录添加 ssh、wifi 的配置（参考 Log 2.2）
4. 插入 rasp pi，通电，重启

> 官方文档为叫我们烧录系统，提供了一个[极其简单漂亮的 Video](https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager)。

1.2 Docker 的安装可以参考，过程比较顺利。docker 安装完成后并不能马上启用，但 reboot 后就可以了。[参考](https://phoenixnap.com/kb/docker-on-raspberry-pi)

# 2. 64bit OS 的缺陷与重装

2.1 今晚花了点时间组装摄像头，后来发现 64bit 的 respberry OS 是不支持 raspistill 工具的。参考：[官方 64bit-OS 反馈贴](https://forums.raspberrypi.com/viewtopic.php?p=1729089#p1729089) 

2.2 鉴于考虑到 32bit 才是稳定的版本，故重刷 32bit 的系统到 TF 卡里。（重新下单了一个 64 GB的 TF 卡，以后长期用于树莓派，128G 的后面继续用于 64bit 的OS，毕竟 Docker 还是有用的），刷系统的时候，需要考虑 ssh 开启和 wifi 的自动连接。因为我没有显示器，故需要[参考此贴](https://shumeipai.nxez.com/2018/08/31/raspberry-pi-vnc-viewer-configuration-tutorial.html
)

2.3 32bit 一开始遇到 VNC 连接桌面失败问题，参考了一下[博客](https://www.tomshardware.com/how-to/fix-cannot-currently-show-desktop-error-raspberry-pi)，调整一下显示器的分辨率就可以。

2.4 后面还会花一点时间去了解 OpenCV。

* python 库安装的时候最好使用国内的源，就像这样： `pip3 install package -i https://pypi.tuna.tsinghua.edu.cn/simple/` ，[参考](https://zhuanlan.zhihu.com/p/124311177)
* OpenCV 在 B 站有搜索到这个比较简单的[教程](https://www.bilibili.com/video/BV1qh411Y7ty)。

2.5 树莓派实验室，是最近几天看到的比较好的[树莓派中文网站](https://shumeipai.nxez.com/) 

2.6 最后摄像头的模块在 32bit OS 上测试通过，期待后面的功能

# 3. 点亮小灯
* Date：2021-10-15 晚上
* Subject: 学习面包板，阅读色环电阻，学习 GPIO 编程

3.1 面包板其实就是一个实验电路板，需要清楚里面的通电逻辑。在B站的[这个视频](https://www.bilibili.com/video/BV1gz4y1Z7N7)里，我认为是讲述面包板最好的。

3.2 电子电路的电阻也是值得关注的，电阻的知识已经忘记得差不多了，需要花一点时间回顾一下。色环电阻的数值阅读需要另外学习，[学习资料](https://www.bilibili.com/video/BV1X64y1U7rQ)在此。但后面还是需要一个万用表协助一下.

3.3 有了上面的储备，可以先看看一份[教程](https://www.ruanyifeng.com/blog/2017/06/raspberry-pi-tutorial.html)，由阮一峰写的，非常简单。但是他用的是 node js 写的。了解完代码后，需要读一下 raspberry 关于 gpio 在 python 上的文档，官方文档[在此](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)，也比较简单。

3.4 正式开始前，还可以选择使用 raspi-gpio 事先测试一下接口，需要 raspi-gpio help 一下就知道如何使用了。假如接线没问题，这个工具应该可以点亮 led 灯了。

3.5 最后编写一下 python 脚本如下：
```python
# test for GPIO

import RPi.GPIO as GPIO
from time import sleep

led = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

i = 10
while i > 0:
    GPIO.output(led, True) # 点亮 led
    sleep(0.5)
    GPIO.output(led, False) # 熄灭 led
    sleep(0.5)
    i -= 1

GPIO.cleanup() # 清理 GPIO
```

执行一下，小灯就会一闪一闪的了。nice，这是自己编写的代码第一次出现在自己眼前，有趣的事情即将发生。这些工程需要积累的东西还很多。期待

# 4. 电子水墨屏的调研
Date：2021-10-18 

4.1 今晚看了 B 站何同学的视频，他设计了一个桌面是带 LED 透明显示器。我想漂亮的电子硬件应该都有显示器，而显示器中，我觉得水墨屏是非常特点有意思的，所以花了一点时间调研。

4.2 发现 B 站的科技区还是挺多视频，符合需求的是[这个](https://www.bilibili.com/video/BV1bf4y1177M?from=search&seid=3348862390233158475&spm_id_from=333.337.0.0)，不过翻译是比较差。另外基于这个视频可以看到 [微雪电子](https://detail.tmall.com/item.htm?id=550688629935&skuId=3770460932966) 会供应这类的屏幕和驱动板。

# 5. OpenCV 的安装
Date: 2021-10-18

5.1 树莓派 apt-get 的安装速度很慢，可以考虑使用[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/)，树莓派拥有更好的社区，这下子显示出来了。棒！这个数据源的下载速度确实非常快，后面在墙内安装东西，还是考虑一些源，节省生命。

5.2 得益于 B 站的小哥介绍，我做了一下 OpenCV 工具的安装。
```shell
pip3 install opencv-python # 偶尔会失败，需要重试
pip3 install opencv-contrib-python==4.1.0.25 # 
apt-get install libatlas-base-dev
apt-get install libjasper-dev -y
apt-get install libqtgui4
apt-get install python3-pyqt5 -y
apt-get install libqt4-test
apt-get install libhdf5-dev -y
```

测试一下：
```python
Python 3.7.3 (default, Jan 22 2021, 20:04:44)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> cv2.__version__
'4.1.0'
>>>
```

# 6. SD 卡的使用技巧
Date: 2021-10-19

6.1 今天在休息的时候无意中发现，tf 卡在大量读写时，会很容易达到寿命的极限。对此树莓派提供了一些延长使用 tf 卡的技巧，就是让 tf 设置为 read only 模式，然后日常编写的文件都会存在内存中，和正常使用无二，但一旦断电后，就必定需要将数据先另外提交。

# 7. python opencv && raspberry pi camera
Date：2021-10-21

7.1 写代码还是需要 vscode，`apt update && apt install code` 就可以[安装 vscode](https://code.visualstudio.com/docs/setup/raspberry-pi)。方便！

7.2 简单地在[ 这个网站 ](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)过了一下 camera 的入门练习。

7.3 pi 在运行的时候突变变得比较慢，考虑到是温度问题，估通过命令 `/opt/vc/bin/vcgencmd measure_temp` 查看了温度，68°，接了风扇后降到 50°。

7.4 在[ B 站](https://www.bilibili.com/video/BV1qh411Y7ty)看到了关于一个 Google 开发的 mediapipe 框架，这是基于 OpenCV 上，构建的一个 AI，用于捕捉某些物件的。所以考虑尝试一下，刚好有 raspberry4 的库，安装方法在[这里](https://pypi.org/project/mediapipe-rpi4/)。（树莓派有大量的极客库都被实现了），但 mediapipe-rpi4 库在国内的源都没有，安装起来有点慢，大概 36MB，20min 左右。

7.5 试了一下上述的视频的《手部跟踪》章节，非常容易就能够在 pi4 上实现下图的效果，代码也写好了，非常简单，非常有意思，但深夜了，先去休息。






