import requests
import json
import base64
import rsa
from Crypto.PublicKey import RSA




geturl = 'http://52.83.104.90:8081/api/public/security/encrypt/info'
re = requests.get(geturl)
a = json.loads(re.text)  # 转json 字典
public = a['data']['publicKey']
token = a['data']['accessToken']
header = {'Content-Type': 'application/json;charset=UTF-8;', 'accessToken': token}



url = 'http://52.83.104.90:8081/api/public/security/login'
data = {"username":"liao","authKey":"08xoCD3PKgj4zt0htXs03If15Lr4MYEuHNINcPRc1ce1ExfAPBE8WMgdHX3VXSv5NWJoPHeA4/ta/VsY9Ek7UjOERZGHDRP8SxbmKgIAEjJ7rz70xlfsPdyB4sLEe850XRyrCqfIR31XfSSDIHE/VMl919HQzwOkfxtM/z6zGLA=","randomCode":"ucyt"}
res = requests.post(url, data=json.dumps(data), headers=header)  # 转json的字符串




pivekey = 'MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAITew3p41Pgwr5t+abaFTkOuC7RAlmK6xXKnKvMIsBQzOLx8G1lgUlb1yKN0ch82PXP6h3tq9gmp+OJ6wadZIoQxR1wQ0xFn81LJavoNYEWpEXQas9N6I1LL8seDLsFNHAc1Sfe0odYpj68qB8M3KGvKyskkPP6YzTVD/4lUjKL3AgMBAAECgYAsSvJRJmygW+J+bFKjNKcVarSeHxXCzc46XT21DMVdxoF4W8rmLXTlZkO/MXdFrlgoDHETlGF2cUH1hcR+m/kkKyv/za4PhV43ISQOTZD1r5Rfuuj5GVQhnO6klbwR/comvEJm82q74z4yWRO7VJd5dTLuOgMIXrhw0NbdVmcdWQJBALrYRI9nl4R4MgpQdSOZ+NA8/dQkbTQuQ2hAPEyIADC8qtpijxNooMqhNafFcuF6fqVpAgLBxh/tGYXPJalWrysCQQC2DFiCHN7SOUGKZP4ginFCgDf97LVsgZ3RuaCGGjytYRm++QqnmgeQ5T7qlQl/F7Pueq9eHkIkbVNgQy7FcRVlAkEAjYl4Xh1+BKY8Wd3a7m4bsjsRmNtDMiz9eQJ36w12/3RcBHR2p6AxdW2rRHzo6m8tcsXZ9Rauq86i798cS2vT4wJAcm5iOC9DlKsu2npPD09WkDGegHuJMtJqzIi9MW5Ok8FEeLl8jAuTE+411Sinln7kuFPf5e5pLxKVZR31yWAizQJAIjUe+F40xLeBz0mghBLMKuyePo1M/68hupb0hLa4PILaFzke0y7pejSCgTBwN3ynmgjBR50VvgRTyM2t++vuag=='
acckey = 'NqcMFh3Oz02kIquUEae8P+mgtQpcNMrS8FkNdHE2MfAHt1tYGYniraDBdVRdmVkz6h+ydFZvHmN07Jub9DZY5PQNkiSX4dazeHOCwXhNsoRCqOmQvUQ+bBqWBXlnNeeKmme0Bt/6nbqEScr9c9FYshBPjhFZ24pjMe2jGjtg9ac='
scckey = 'exL7RqwsimrItBEGXWJJMq4WP6jTFdtY9DHdWTgAUQtvVbJfDUlSTWEVLD4u7DY9IIgLOzgwxfvpuC6KHbHOYEYs/gm+RJYmaJR2HcaRqjvzBlq7VKQVmDQYObAbZ7C50l3T6JQzm2lu2z2xAmxtboJKCJfefAIWHOsE8K1wQ9A='
publicKeyBytes = base64.b64decode(pivekey)
key = RSA.import_key(publicKeyBytes)
print(key)
ackey = rsa.decrypt(acckey.encode(), key)
sskey = rsa.decrypt(scckey.encode(), key)
ack = base64.b64decode(ackey).encode()
scy = base64.b64decode(sskey).encode()
print(ack)
print(scy)
header = {'Content-Type': 'application/json;charset=UTF-8;', 'accessToken': token}
data = {"awsAccId":"246269375324","awsBillBucket":"","awsAccessKey":acckey,"awsSecretKey":scckey,"belongCountryCode":"cn"}
re = requests.post(url, data=json.dumps(data), headers=header)  # 转json的字符串
print(re.text)


