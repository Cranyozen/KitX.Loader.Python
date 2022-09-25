import time, base64

def OnLoad(KitX):
    print(f"From plugin! Host:{KitX.host} Port:{KitX.port}")
    #time.sleep(30)

def OnUnload(KitX):
	print("From plugin! Unload.")

def OnReceiveMessage(Kit, msg):
	print(f"From plugin! ReceiveMessage {msg}")

#region 插件信息

with open("icon.jpg","rb") as f:
    base64_data = base64.b64encode(f.read())

PluginData = {
	"Name": "PyLoader测试插件",
	"Version": "PyLoader测试插件",
	"DisplayName": {
        "zh-cn": "PyLoader测试插件"
    },
	"AuthorName": "LYF511",
	"PublisherName": "LYF511",
	"AuthorLink": "https://github.com/LYF511",
	"PublisherLink": "https://github.com/LYF511",
	"SimpleDescription": {
        "zh-cn": "PyLoader测试插件"
    },
	"ComplexDescription": {
        "zh-cn": "PyLoader测试插件"
    },
	"TotalDescriptionInMarkdown": {
        "zh-cn": "PyLoader测试插件"
    },
	"IconInBase64": base64_data.decode(),
	"PublishDate": "2022-09-23T19:40:00",
	"LastUpdateDate": "2022-09-23T19:40:00",
	"IsMarketVersion": False,
	"Tags": {},
	"Functions": None,
	"RootStartupFileName": ""
}

#endregion
