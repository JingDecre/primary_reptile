# import urllib3.request
from urllib import request
import re

url=r"http://www.baidu.com/" #前面加r防止转义字符

# 创建自定义请求对象
req = request.Request(url)

#发送请求.获取响应信息， 通过自定义请求对象获取信息，相比单纯url可扩展性更强
reponse=request.urlopen(req).read().decode() #解码---（编码 encode）


# 通过正则表达式简单的数据清洗
pat = r"<title>(.*?)</title>"
data = re.findall(pat, reponse)

print(data[0])