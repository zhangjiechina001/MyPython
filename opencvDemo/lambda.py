class MyClass(object):
    def __init__(self):
        self._para=None

    def getParam(self):
        print("get param:%s"%self._para)
        return self._para
    def setParam(self,value):
        print('set param:%s'%self._para)
        self._para=value

    def delParam(self):
        print('del param:%s'%self._para)
        del self._para

if __name__=='__main__':
    cls=MyClass('zhangjie')
    cls.add(9,10)
