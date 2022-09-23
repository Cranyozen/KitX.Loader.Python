import time, base64


with open("icon.jpg","rb") as f:
    base64_data = base64.b64encode(f.read())

PluginData = {
	"Name": "来自PythonLoader的测试插件",
	"Version": "来自PythonLoader的测试插件",
	"DisplayName": {
        "zh-cn": "来自PythonLoader的测试插件"
    },
	"AuthorName": "LYF511",
	"PublisherName": "LYF511",
	"AuthorLink": "https://github.com/LYF511",
	"PublisherLink": "https://github.com/LYF511",
	"SimpleDescription": {
        "zh-cn": "来自PythonLoader的测试插件"
    },
	"ComplexDescription": {
        "zh-cn": "来自PythonLoader的测试插件"
    },
	"TotalDescriptionInMarkdown": {
        "zh-cn": "来自PythonLoader的测试插件"
    },
	"IconInBase64": base64_data.decode(),
	"PublishDate": "2022-09-23T19:40:00",
	"LastUpdateDate": "2022-09-23T19:40:00",
	"IsMarketVersion": False,
	"Tags": {},
	"Functions": None,
	"RootStartupFileName": ""
}

def OnLoad(KitX):
    print(f"From plugin!\nHost:{KitX.host} Port:{KitX.port}")
    time.sleep(30)
