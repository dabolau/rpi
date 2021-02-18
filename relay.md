# 继电器控制程序

### 硬件线路连接方式


1.  树莓派选择（BOARD）模式
*  （2）引脚5V，电源，选择（红色）线连接
*  （6）引脚GND，接地，选择（黑色）线连接
*  （40）引脚GPIO，控制，选择（白色）线连接

2.  继电器接入（高电平时常开闭合，常闭断开，低电平时常开断开，常闭闭合，注意是什么电平触发）
*   (VCC)引脚，电源，连接红色线
*   (GND)引脚，接地，连接黑色线
*   (IN)引脚，控制，连接白色线

3.  继电器接出
*   (NO)引脚，常开，连接黑色线
*   (COM)引脚，公共端，连接灰色线
*   (NC)引脚，常闭，连接白色线

4.  电源（电池盒）
*   正极，连接继电器(COM)公共端灰色线
*   负极，连接发光二极管一引脚，另一引脚连接继电器(NO)常开黑色线，注意二极管的引脚正反

### 演示代码

```python
import sys

import RPi.GPIO as GPIO


###
# 继电器控制程序
###
class Relay():
    ###
    # 初始化
    ###
    def __init__(self, pinValue: int = 40):
        # 设置针脚
        self.pin = pinValue

    ###
    # 自定义初始化
    ###
    def init(self):
        # 设置针脚模式为（BOARD）
        GPIO.setmode(GPIO.BOARD)
        # 禁用警告
        GPIO.setwarnings(False)
        # 设置针脚为输出模式
        GPIO.setup(self.pin, GPIO.OUT)

    ###
    # 关闭
    ###
    def off(self):
        # 低电平输出
        GPIO.output(self.pin, GPIO.LOW)

    ###
    # 打开
    ###
    def on(self):
        # 高电平输出
        GPIO.output(self.pin, GPIO.HIGH)

    ###
    # 释放
    ###
    def release(self):
        # 释放针脚
        GPIO.cleanup()


###
# 主函数入口
###
if __name__ == '__main__':
    # 实例化并设置针脚
    r = Relay(pinValue=40)
    # 初始化
    r.init()
    # 继电器控制
    while True:
        onOrOffOrExit = input('请输入参数控制继电器开关：')
        if onOrOffOrExit == str(0):
            r.off()
        elif onOrOffOrExit == str(1):
            r.on()
        else:
            r.release()
            sys.exit(0)
```