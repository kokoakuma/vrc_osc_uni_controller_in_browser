import argparse

from pythonosc import udp_client

from . import controller

moveController = controller.MoveController()

def moveAvater(top, left) -> None:
    moveController.moveVertical(top)
    print("vertical" + str(top))
    moveController.moveHorizontal(left)
    print("horizontal" + str(left))

def stopAvater() -> None:
    moveController.stop()

def judgeShouldSkip(top, left) -> bool:
    return moveController.shouldSkipCall(top, left)

