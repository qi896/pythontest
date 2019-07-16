import xlrd,logging,time,datetime


class tool:
    def read(self,index=0):
        ren = xlrd.open_workbook('D:\hh.xlsx')
        sheet = ren.sheets()[index]
        return sheet


    def logelf(self,wo,level,msg):
        name = 'date'
        timea = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        #imea = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        qu = 'pass'
        if level == 0:
            qu = "pass"
        else:
            qu = "fail"
        bye = timea + " - " + wo + " - " +  qu + " : " + msg + "\n"
        eq = open(name,'a+',encoding='utf-8')
        eq.write(bye)
        eq.close()


    def wen(self,r,s,temp):
         sum = True
         if r in s:
             self.logelf(temp,0,"成功")
             return sum
         else:
             sum = False
             self.logelf(temp,1,"失败")
             return sum
