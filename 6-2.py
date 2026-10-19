import math
import turtle
import figure  # figure.py 모듈로 imfort

class Triangle(figure.Polygon):
    count = 0

    def __init__(self, sideLen=0):
        super().__init__(3)
        self.setSideLen(sideLen)
        Triangle.count += 1
        self.serialNumber = Triangle.count

    # 1. 정삼각형 넓이 계산
    def getArea(self):
        return (math.sqrt(3) / 4) * (self.sideLen**2)

    # 2. 몇 번째 인스턴스인지 반환
    def getSerial(self):
        return self.serialNumber

    # 3. draw() 메소드 -> turtle 모듈로 삼각형 그리기
    def draw(self):
        for step in range(self.sideNumber):
            turtle.forward(self.sideLen)
            turtle.right(360 / self.sideNumber)
        input("Press any key to stop")

if __name__ == "__main__":
    t = Triangle(300)
    print("삼각형의 면적 : {}".format(t.getArea()))
    print("생성된 인스턴스 번호 : {}".format(t.getSerial()))
    t.draw()