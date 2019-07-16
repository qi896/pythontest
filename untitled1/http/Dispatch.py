from http.implement import sum
from http.Tool import tool
import time
import threading

class testcase:
     def __init__(self):
          self.su = sum()
          self.to = tool()
          self.data = self.to.read()
          self.ps = 0
          self.fa = 0

     def run(self):
         for i in range(1,self.data.nrows):
             rowList = self.data.row_values(i)
             if rowList[2] == 'post':
                 if rowList[0] == '登录':
                     print("#####")
                     listone = rowList[3].split(',')
                     won = self.su.addpassword(rowList[1],listone[0],listone[1],listone[2])
                     xun = self.to.wen(rowList[4],won.text,"第"+str(i)+"条用例: "+rowList[0])
                     if xun == True:
                         self.ps += 1
                     else:
                         self.fa += 1
                 elif rowList[0] == '修改密码':
                     print("&&&&&&")
                     listone = rowList[3].split(',')
                     wo = self.su.updatapassword(listone[0],listone[1],listone[2],rowList[1],listone[3],listone[4])
                     too = self.to.wen(rowList[4], wo.text,"第"+str(i)+"条用例: "+rowList[0])
                     if too == True:
                         self.ps += 1
                     else:
                         self.fa += 1

                 elif rowList[0] == 'AWS账户':
                     print("AWS")
                     list= rowList[3].split(',')
                     ss = self.su.AWSname(rowList[1],list[0],list[1],list[2],list[3],list[4])
                     temp = self.to.wen(rowList[4], ss.text,"第"+str(i)+"条用例: "+rowList[0])
                     if temp == True:
                         self.ps += 1
                     else:
                         self.fa += 1


                 else:
                      res = self.su.posttest(rowList[1],rowList[3])
                      a = self.to.wen(rowList[4],res.text,"第"+str(i)+"条用例: "+rowList[0])
                      if a == True:
                          self.ps += 1
                      else:
                          self.fa += 1
             else:
                  if rowList[3] == '':
                      print("******")
                      re = self.su.gettest(rowList[1])
                      b= self.to.wen(rowList[4],re.text,"第"+str(i)+"条用例: "+rowList[0])
                      if b == True:
                          self.ps += 1
                      else:
                          self.fa += 1
                  else:
                      print("$$$$$$$$")
                      re = self.su.getdata(rowList[1],rowList[3])
                      b = self.to.wen(rowList[4],re.text,"第"+str(i)+"条用例: "+rowList[0])
                      if b == True:
                          self.ps += 1
                      else:
                          self.fa += 1


     def start(self):
          # 在执行过程之前和之后分别获取开始和结束时间
          begin = time.clock()
          self.run()
          end = time.clock()
          # 计算出运行时长
          self.runTime = int(end - begin)
          print('-------------------------------')
          print('运行时长：' + str(self.runTime) + "s, 成功数：" + str(self.ps) + ", 失败数：" + str(self.fa))
          print('-------------------------------')


    #定时执行脚本
     #def fun_timer(self):
      #   self.start()
        # global timer
         #timer = threading.Timer(5,self.fun_timer)  # 60秒调用一次函数
         #timer.start()




t = testcase()
t.start()
#t.fun_timer()











