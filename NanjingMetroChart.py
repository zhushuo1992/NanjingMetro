#-*-coding:utf8-*-
import sqlite3
import os
import time, datetime
import pandas as pd
from pyecharts import Bar
from pyecharts.chart import Chart
from pyecharts import Pie

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

def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

if __name__ == "__main__":

    i=0
    bar = Bar("南京地铁", "总图",title_pos='left',width=1400, height=700)
    conn = get_conn(DB_FILE_PATH)
    cu = get_cursor(conn)
    fetchall_sql = '''SELECT LineALL FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnt0 = cu.fetchall()
    cntl0=[]
    for l0 in cnt0:
        cntl0.append(l0[0])

    

    fetchall_sql = '''SELECT DATE FROM NajingMetro'''
    cu.execute(fetchall_sql)
    date1 = cu.fetchall()
    datel1=[]
    for d1 in date1:
        datel1.append(d1[0])

    fetchall_sql = '''SELECT Line1 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnt1 = cu.fetchall()
    cntl1=[]
    for l1 in cnt1:
        cntl1.append(l1[0])

    fetchall_sql = '''SELECT Line2 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnt2 = cu.fetchall()
    cntl2=[]
    for l2 in cnt2:
        cntl2.append(l2[0])

    fetchall_sql = '''SELECT Line3 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnt3 = cu.fetchall()
    cntl3=[]
    for l3 in cnt3:
        cntl3.append(l3[0])

    fetchall_sql = '''SELECT Line4 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnt4 = cu.fetchall()
    cntl4=[]
    for l4 in cnt4:
        cntl4.append(l4[0])

    fetchall_sql = '''SELECT Line10 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnt10 = cu.fetchall()
    cntl10=[]
    for l10 in cnt10:
        cntl10.append(l10[0])

    fetchall_sql = '''SELECT LineS1 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnts1 = cu.fetchall()
    cntls1=[]
    for ls1 in cnts1:
        cntls1.append(ls1[0])

    fetchall_sql = '''SELECT LineS3 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnts3 = cu.fetchall()
    cntls3=[]
    for ls3 in cnts3:
        cntls3.append(ls3[0])

    fetchall_sql = '''SELECT LineS7 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnts7 = cu.fetchall()
    cntls7=[]
    for ls7 in cnts7:
        cntls7.append(ls7[0])

    fetchall_sql = '''SELECT LineS8 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnts8 = cu.fetchall()
    cntls8=[]
    for ls8 in cnts8:
        cntls8.append(ls8[0])

    fetchall_sql = '''SELECT LineS9 FROM NajingMetro'''
    cu.execute(fetchall_sql)
    cnts9 = cu.fetchall()
    cntls9=[]
    for ls9 in cnts9:
        cntls9.append(ls9[0])


    cntl0.reverse()
    cntl1.reverse()
    cntl2.reverse()
    cntl3.reverse()
    cntl4.reverse()
    cntl10.reverse()
    cntls1.reverse()
    cntls3.reverse()
    cntls7.reverse()
    cntls8.reverse()
    cntls9.reverse()


    bar.add('全线网客运量',date1,cntl0,mark_point=["max","min"],mark_line=["average"],is_more_utils=True)
    bar.add('1号线', date1, cntl1,is_datazoom_show=True)
    bar.add('2号线', date1, cntl2,is_datazoom_show=True)
    bar.add('3号线', date1, cntl3,is_datazoom_show=True)
    bar.add('4号线', date1, cntl4,is_datazoom_show=True)
    bar.add('10号线', date1, cntl10,is_datazoom_show=True)
    bar.add('S1机场线', date1, cntls1,is_datazoom_show=True)
    bar.add('S3宁和线', date1, cntls3,is_datazoom_show=True)
    bar.add('S7宁溧线', date1, cntls7,is_datazoom_show=True)
    bar.add('S8宁天线', date1, cntls8,is_datazoom_show=True)
    bar.add('S9宁高线', date1, cntls9,is_datazoom_show=True)

    #bar.show_config()
    bar.render('南京地铁.html')

    cntl0.reverse()
    cntl1.reverse()
    cntl2.reverse()
    cntl3.reverse()
    cntl4.reverse()
    cntl10.reverse()
    cntls1.reverse()
    cntls3.reverse()
    cntls7.reverse()
    cntls8.reverse()
    cntls9.reverse()

    print(cntls9[0:30])
    print(averagenum(cntls9[0:30]))
    attr = ["1号线", "2号线", "3号线", "4号线", "10号线", "S1机场线", "S3宁和线", "S7宁溧线", "S8宁天线", "S9宁高线"]
    v1 = [averagenum(cntl1[0:30]), averagenum(cntl2[0:30]), averagenum(cntl3[0:30]), averagenum(cntl4[0:30]), averagenum(cntl10[0:30]), averagenum(cntls1[0:30]),averagenum(cntls3[0:30]),averagenum(cntls7[0:30]),
    averagenum(cntls8[0:30]),averagenum(cntls9[0:30])]
    pie = Pie("南京地铁","各线路占比",title_pos='left',width=1400, height=700)#新建饼图示例pie

    pie.add("", attr, v1, is_label_show=True)
    #pie.show_config()#是否在命令行中显示config，此行可省略
    pie.render("南京地铁饼图.html")