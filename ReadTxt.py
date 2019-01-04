#-*-coding:utf8-*-
import sqlite3
import os
import time, datetime

year1=2018

#是否打印sql
SHOW_SQL = True
DB_FILE_PATH = 'NajingMetro.db'

def get_conn(path):
    '''获取到数据库的连接对象，参数为数据库文件的绝对路径
    如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
    路径下的数据库文件的连接对象；否则，返回内存中的数据接
    连接对象'''
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print('硬盘上面:[{}]'.format(path))
        return conn
    else:
        conn = None
        print('内存上面:[:memory:]')
        return sqlite3.connect(':memory:')

def get_cursor(conn):
    '''该方法是获取数据库的游标对象，参数为数据库的连接对象
    如果数据库的连接对象不为None，则返回数据库连接对象所创
    建的游标对象；否则返回一个游标对象，该对象是内存中数据
    库连接对象所创建的游标对象'''
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()

def create_table(conn, sql):
    '''创建数据库表'''
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu.execute(sql)
        conn.commit()
        print('创建数据库表[student]成功!')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def close_all(conn, cu):
    '''关闭数据库游标对象和数据库连接对象'''
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()

def save(conn, sql, data):
    '''插入数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                try:
                	cu.execute(sql, d)
                	try:
                		conn.commit()
                	except:
                		print("Unexpected error:")
                except:
                	print("Unexpected error:")
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def fetchall(conn, sql):
    '''查询所有数据'''
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu.execute(sql)
        r = cu.fetchall()
        if len(r) > 0:
            for e in range(len(r)):
                print(r[e])
    else:
        print('the [{}] is empty or equal None!'.format(sql)) 

def fetchone(conn, sql, data):
    '''查询一条数据'''
    if sql is not None and sql != '':
        if data is not None:
            #Do this instead
            d = (data,) 
            cu = get_cursor(conn)
            if SHOW_SQL:
                print('执行sql:[{}],参数:[{}]'.format(sql, data))
            cu.execute(sql, d)
            r = cu.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    print(r[e])
        else:
            print('the [{}] equal None!'.format(data))
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def update(conn, sql, data):
    '''更新数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def delete(conn, sql, data):
    '''删除数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))

def savedata(sql,data):
    '''保存数据测试...'''
    conn = get_conn(DB_FILE_PATH)
    save(conn, sql, data)

def getdate(date1):
	global year1
	if date1.find('月') != -1:
		date1=date1.replace('月',';')
		date1=date1.replace('日',';')
		list2=date1.split(';')
		if '1' == list2[0] and '2' ==  list2[1]:
			year1=year1-1
			date2=str(year1)+'-'+list2[0]+'-'+list2[1]
		else:
			date2=str(year1)+'-'+list2[0]+'-'+list2[1]
		date3 = datetime.datetime.strptime(date2,'%Y-%m-%d').date()
		return date3

if __name__=="__main__":
    create_table_sql = '''CREATE TABLE `NajingMetro` (
                          `DATE` varchar(20) NOT NULL,
                          `LineALL` REAL(20) DEFAULT NULL,
                          `Line1` REAL(20) DEFAULT NULL,
                          `Line2` REAL(20) DEFAULT NULL,
                          `Line3` REAL(20) DEFAULT NULL,
                          `Line4` REAL(20) DEFAULT NULL,
                          `Line10` REAL(20) DEFAULT NULL,
                          `LineS1` REAL(20) DEFAULT NULL,
                          `LineS3` REAL(20) DEFAULT NULL,
                          `LineS7` REAL(20) DEFAULT NULL,
                          `LineS8` REAL(20) DEFAULT NULL,
                          `LineS9` REAL(20) DEFAULT NULL,
                           PRIMARY KEY (`DATE`)
                        )'''
    conn = get_conn(DB_FILE_PATH)
    create_table(conn, create_table_sql)

    f = open('2638276292.txt','r', encoding='UTF-8')
    while True:
        line = f.readline()
    # 零长度指示 EOF
        if len(line) == 0:
            break
    # 每行（`line`）的末尾
    # 都已经有了换行符
    #因为它是从一个文件中进行读取的
        cnt0=0
        cnt1=0
        cnt2=0
        cnt3=0
        cnt4=0
        cnt10=0
        cnts1=0
        cnts3=0
        cnts7=0
        cnts8=0
        cnts9=0
        date5=''

        line=line.replace('，',',')
        line=line.replace('。',',')
        line=line.replace(' ','')
        line=line.replace(' ','')
        line=line.replace('南京地铁','')
        line=line.replace('万次','')
        line=line.replace('全线网客运量',',')
        line=line.replace('线网客运量',',')
        line=line.replace('全线网客运',',')
        line=line.replace('全线网客',',')
        line=line.replace('其中',',')
        line=line.replace('元月','1月')
        line=line.replace('（','(')
        ind0=line.find('(')
        if ind0 != -1:
            line = line[:ind0]
            ind0=line.find('(')
        ind0=line.find('.另')
        if ind0 != -1:
            line = line[:ind0]
        list1 = line.split(',')
        for str1 in list1:
            if str1.find('记录') != -1:
                continue
            elif str1.find('月') != -1:
                #print(getdate(str1))
                date5=getdate(str1)
            elif str1.find('1号线') != -1:
                #print(str1)
                ind1 = str1.find('1号线')
                cnt1=float(str1[ind1+3:])
                
            elif str1.find('2号线') != -1:
                ind1 = str1.find('2号线')
                cnt2=float(str1[ind1+3:])

            elif str1.find('3号线') != -1:
                ind1 = str1.find('3号线')
                cnt3 = float(str1[ind1+3:])

            elif str1.find('4号线') != -1:
                ind1 = str1.find('4号线')
                cnt4=float(str1[ind1+3:])

            elif str1.find('10号线') != -1:
                ind1 = str1.find('10号线')
                cnt10 = float(str1[ind1+4:])

            elif str1.find('S1机场线') != -1:
                ind1 = str1.find('S1机场线')
                cnts1 = float(str1[ind1+5:])

            elif str1.find('S3宁和线') != -1:
                ind1 = str1.find('S3宁和线')
                cnts3 = float(str1[ind1+5:])

            elif str1.find('S7宁溧线') != -1:
                ind1 = str1.find('S7宁溧线')
                cnts7 = float(str1[ind1+5:])

            elif str1.find('S8宁天线') != -1:
                ind1 = str1.find('S8宁天线')
                cnts8 = float(str1[ind1+5:])

            elif str1.find('S9宁高线') != -1:
                ind1 = str1.find('S9宁高线')
                cnts9 = float(str1[ind1+5:])
            
        cnt0=float(list1[1])
        savesql = '''INSERT INTO NajingMetro values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        data = [(date5, cnt0,cnt1,cnt2,cnt3,cnt4,cnt10,cnts1,cnts3,cnts7,cnts8,cnts9)]
        savedata(savesql,data)
    # 关闭文件
    f.close()

