import sys

import RPi.GPIO as GPIO


###
# 控制继电器
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
    # 控制继电器
    while True:
        onOrOffOrExit = input('请输入参数控制继电器开关：')
        if onOrOffOrExit == str(0):
            r.off()
        elif onOrOffOrExit == str(1):
            r.on()
        else:
            r.release()
            sys.exit(0)
