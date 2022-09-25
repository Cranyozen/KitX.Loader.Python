import sys, socket, threading, importlib.util
from json import dumps as js_dumps
from time import sleep as tm_sleep

class KitX():
    def __init__(self, host: str, port: int, receiveFunc, BUFSIZE=1024*1000) -> None:
        self.host = host
        self.port = port
        self.BUFSIZE = BUFSIZE
        self.receiveRun = True
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        self.__receiveThread = threading.Thread(target=self.ReceiveMessage, args=(receiveFunc,))
        self.__receiveThread.start()

    def SendMessage(self, message):
        if isinstance(message, str):
            self.client.sendall(message.encode("utf-8"))
        elif isinstance(message, bytes):
            self.client.sendall(message)
        else:
            self.client.sendall(js_dumps(message).encode("utf-8"))

    def ReceiveMessage(self, func):
        while self.receiveRun:
            data = self.client.recv(self.BUFSIZE)
            if data:
                func(self, data.decode("utf-8"))

    def __del__(self):
        self.receiveRun = False
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()
        print("KitX socket closed.")
        while self.__receiveThread.is_alive():
            tm_sleep(2)

class Plugin():
    def __init__(self, host: str, port: int, path: str, name:str) -> None:
        self.path = path
        self.name = name
        self.__load_module()
        self.KitX = KitX(host, port, self.module.OnReceiveMessage)
        self.OnLoad()
    
    def __load_module(self) -> None:
        if self.name is None:
            self.name = self.path.replace('/', '_').replace('\\', '_').replace('.', '_')
        spec = importlib.util.spec_from_file_location(self.name, self.path)
        self.module = importlib.util.module_from_spec(spec)  # type: ignore
        sys.modules[self.name] = self.module
        spec.loader.exec_module(self.module)
    
    def OnLoad(self) -> None:
        self.Register()
        self.module.OnLoad(self.KitX)

    def OnUnload(self) -> None:
        self.module.OnUnload(self.KitX)

    def Register(self) -> None:
        data = self.module.PluginData
        data["RootStartupFileName"] = self.name
        self.KitX.SendMessage(data)

    def __del__(self) -> None:
        self.OnUnload()