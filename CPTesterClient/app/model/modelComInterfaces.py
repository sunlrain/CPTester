# Model of Com(UART) Interfaces
from modelBase import modelBase


class modelComInterfaces(modelBase):
    def __init__(self):
        print("Com Interfaces init")
        self.keys = ["ipAddr","port"]
