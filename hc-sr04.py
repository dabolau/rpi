import time

import RPi.GPIO as GPIO


###
# 超声波传感器程序
###
class HcSr04:
    ###
    # 初始化
    ###
    def __init__(self, trig: int = 38, echo: int = 40):
        # 设置针脚
        self.TRIG = trig
        self.ECHO = echo
        # 初始化传感器
        self.init()

    ###
    # 初始化距离传感器
    ###
    def init(self):
        print("Distance Measurement In Progress")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

    ###
    # 获取距离信息
    ###
    def getDistance(self):
        # 向Trig引脚发送10us的脉冲信号
        GPIO.output(self.TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, GPIO.LOW)

        # 开始发送超声波的时刻
        while GPIO.input(self.ECHO) == 0:
            pass
        startTime = time.time()

        # 收到返回超声波的时刻
        while GPIO.input(self.ECHO) == 1:
            pass
        endTime = time.time()

        # 计算距离 距离=(声波的往返时间*声速)/2
        timeDelta = endTime - startTime
        distance = (timeDelta * 34300) / 2

        # 返回距离
        return distance


###
# 程序入口
###
if __name__ == "__main__":
    try:
        # 实例化超声波传感器并设置针脚
        h = HcSr04(trig=38, echo=40)
        while True:
            # 获取距离信息
            distance = h.getDistance()
            print(f"Distance = {distance} cm")
            # 每间隔1秒测量一次
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped")
        GPIO.cleanup()