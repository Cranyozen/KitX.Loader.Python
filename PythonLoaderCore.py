import socket, json, importlib.util, sys

class KitX():
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def SendMessage(self, message):
        if isinstance(message, str):
            self.client.sendall(message.encode("utf-8"))
        else:
            self.client.sendall(json.dumps(message).encode("utf-8"))

    def __del__(self):
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()
        print("KitX socket closed.")

class Plugin():
    def __init__(self, host: str, port: int, path: str, name:str) -> None:
        self.path = path
        self.name = name
        self.KitX = KitX(host, port)
        self.__load_module()
    
    def __load_module(self):
        if self.name is None:
            self.name = self.path.replace('/', '_').replace('\\', '_').replace('.', '_')
        spec = importlib.util.spec_from_file_location(self.name, self.path)
        self.module = importlib.util.module_from_spec(spec)  # type: ignore
        sys.modules[self.name] = self.module
        spec.loader.exec_module(self.module)
        self.OnLoad()
    
    def OnLoad(self):
        self.Register()
        self.module.OnLoad(self.KitX)

    def OnUnLoad(self):
        pass

    def Register(self):
        data = self.module.PluginData
        data["RootStartupFileName"] = self.name
        self.KitX.SendMessage(data)
