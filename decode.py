# import urllib3.request
from urllib import request
import re

url=r"http://www.baidu.com/" #前面加r防止转义字符

#发送请求.获取响应信息
reponse=request.urlopen(url).read().decode() #解码---（编码 encode）

# print(reponse)
# print(type(reponse))

# 通过正则表达式简单的数据清洗
pat = r"<title>(.*?)</title>"
data = re.findall(pat, reponse)

print(data)