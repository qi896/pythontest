import base64
import rsa
from Crypto.PublicKey import RSA
import requests
import json



class login:

    #获取公钥、token
    def __init__(self):
        geturl = 'http://52.83.104.90:8081/api/public/security/encrypt/info'
        re = requests.get(geturl)
        a=json.loads(re.text)#转json 字典
        self.public = a['data']['publicKey']
        self.token = a['data']['accessToken']


    # 公钥加密
    def addpasswod(self,password):
        # 1、base64解码
        publicKeyBytes = base64.b64decode(self.public.encode())
        # 2、生成publicKey对象
        key = RSA.import_key(publicKeyBytes)
        # 3、对原密码加密
        encryptPassword = rsa.encrypt(password.encode(), key)
        self.run = base64.b64encode(encryptPassword).decode()
        print(self.run)


    #发送登录请求
    def loginhttp(self,username,password,random):
        self.addpasswod(password)
        posturl = 'http://52.83.104.90:8081/api/public/security/login'
        header ={'Content-Type':'application/json;charset=UTF-8;','accessToken':self.token}
        data = {"username":username,"authKey":self.run,"randomCode":random}
        res = requests.post(posturl,data=json.dumps(data),headers=header)#转json的字符串
        print(res.text)


if __name__ == '__main__':
    lo = login()
    lo.loginhttp("qishi","qishi333","0")


