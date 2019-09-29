import pymssql #引入pymssql模块
import snap7.server as server
ser=server;
txt=ser.Server.event_text();
print(txt);

def conn():
    connect = pymssql.connect(server='(local)',database='CATL_48VOCV') #服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    return connect


if __name__ == '__main__':
    conn = conn()