import requests
import base64
import rsa
from Crypto.PublicKey import RSA
import requests
import json
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5

class sum:
    # 获取公钥、token
    def __init__(self):
        geturl = 'http://52.83.104.90:8081/api/public/security/encrypt/info'
        re = requests.get(geturl)
        a = json.loads(re.text)  # 转json 字典
        self.public = a['data']['publicKey']
        self.token = a['data']['accessToken']
        self.header = {'Content-Type': 'application/json;charset=UTF-8;', 'accessToken': self.token}


    # 公钥加密
    def addpassword(self,posturl,username,password,random):
        # 1、base64解码
        publicKeyBytes = base64.b64decode(self.public.encode())
        # 2、生成publicKey对象
        key = RSA.import_key(publicKeyBytes)
        # 3、对原密码加密
        encryptPassword = rsa.encrypt(password.encode(), key)
        self.run = base64.b64encode(encryptPassword).decode()
        header = {'Content-Type':'application/json;charset=UTF-8;','accessToken':self.token}
        data = {"username":username,"authKey":self.run,"randomCode":random}
        res = requests.post(posturl,data=json.dumps(data),headers=header)  # 转json的字符串
        return res

    #修改密码
    def updatapassword(self,user,psword,random,posturl,pass1,pass2):
        loginurl = 'http://52.83.104.90:8081/api/public/security/login'
        self.addpassword(loginurl,user,psword,random)
        publicKeyBytes = base64.b64decode(self.public.encode())
        key = RSA.import_key(publicKeyBytes)
        Password1 = rsa.encrypt(pass1.encode(), key)
        Password2 = rsa.encrypt(pass2.encode(), key)
        self.ps1 = base64.b64encode(Password1).decode()
        self.ps2 = base64.b64encode(Password2).decode()
        data = {"currentAuthKey":self.ps1,"newAuthKey":self.ps2}
        res = requests.post(posturl, data=json.dumps(data), headers=self.header)  # 转json的字符串
        return res


    #get无参
    def gettest(self,url):
        self.addpassword("http://52.83.104.90:8081/api/public/security/login","liao","7MK49R","00")
        res = requests.get(url,headers=self.header)
        return res

    #get有参
    def getdata(self,url,data):
        self.addpassword("http://52.83.104.90:8081/api/public/security/login", "liao", "7MK49R", "00")
        res = requests.get(url,data,headers=self.header)
        return res


    def posttest(self,url,data):
        self.addpassword("http://52.83.104.90:8081/api/public/security/login", "liao", "7MK49R", "00")
        res = requests.post(url,data,headers=self.header)
        return res


    #AWS账户加密
    def AWSname(self,url,ID,s3name,acckey,scckey,country):
        self.addpassword("http://52.83.104.90:8081/api/public/security/login", "liao", "7MK49R", "00")
        publicKeyBytes = base64.b64decode(self.public.encode())
        key = RSA.import_key(publicKeyBytes)
        ackey = rsa.encrypt(acckey.encode(), key)
        sskey = rsa.encrypt(scckey.encode(),key)
        ack = base64.b64encode(ackey).decode()
        scy = base64.b64encode(sskey).decode()
        header = {'Content-Type': 'application/json;charset=UTF-8;', 'accessToken': self.token}
        data = {"awsAccId":ID,"awsBillBucket":s3name,"awsAccessKey":ack,"awsSecretKey":scy,"belongCountryCode":country}
        res = requests.post(url, data=json.dumps(data), headers=header)  # 转json的字符串
        return res

