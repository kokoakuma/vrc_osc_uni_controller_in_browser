import argparse

from pythonosc import udp_client

from . import constant, udpClientGenerator

class MoveController:
    def __init__(self):
        self.client = udpClientGenerator.UDPClientGenerator()
        self.lastTop = 0
        self.lastLeft = 0

    def shouldSkipCall(self, top, left) -> bool:
        # 送信回数を減らすため、小さい変更はスキップさせる
        print(self.lastTop)
        print(top)
        print(abs(self.lastTop - top))
        print(constant.IGNORE_LEVEL)
        if abs(self.lastTop - top) < constant.IGNORE_LEVEL and abs(self.lastLeft - left) < constant.IGNORE_LEVEL:
            return True
        else:
            self.lastTop = top
            self.lastLeft = left
            return False

    def moveVertical(self, top) -> None:
        # スティック画像分のpxを足した後、座標をパラメータ用に変換（小さい数字を前進、大きい数字を後退）
        roundedTop = constant.AREA_SIZE - (top + constant.HALF_STICK_SIZE)
        # 範囲外の数字が来たら、丸める
        if top < constant.FLOAT_ZERO:
            roundedTop = constant.FLOAT_ZERO
        if top > constant.AREA_SIZE:
            roundedTop = constant.AREA_SIZE

        # 座標をfloat(-1.0 < x < 1.0)に変換
        verticalOffsetToCenter = roundedTop - constant.HALF_AREA_SIZE
        velocity = verticalOffsetToCenter / constant.HALF_AREA_SIZE

        self.client.send_message(constant.INPUT_VERTICAL, velocity)
    
    def moveHorizontal(self, left) -> None:
        # スティック画像分のpxを足した後、座標をパラメータ用に変換
        roundedLeft = left + constant.HALF_STICK_SIZE
        # 範囲外の数字が来たら、丸める
        if left < constant.FLOAT_ZERO:
            roundedLeft = constant.FLOAT_ZERO
        if left > constant.AREA_SIZE:
            roundedLeft = constant.AREA_SIZE

        # 座標をfloat(-1.0 < x < 1.0)に変換
        horizontalOffsetToCenter = roundedLeft - constant.HALF_AREA_SIZE
        velocity = horizontalOffsetToCenter / constant.HALF_AREA_SIZE

        self.client.send_message(constant.INPUT_HORIZONTAL, velocity)
    
    def stop(self) -> None:
        # 前後左右移動のパラメータを0にリセットする
        self.client.send_message(constant.INPUT_VERTICAL, constant.FLOAT_ZERO)
        self.client.send_message(constant.INPUT_HORIZONTAL, constant.FLOAT_ZERO)
