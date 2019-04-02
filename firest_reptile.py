# import urllib3.request
from urllib import request
url=r"http://www.baidu.com/" #前面加r防止转义字符

#发送请求.获取响应信息
reponse=request.urlopen(url).read()


print(type(reponse))
