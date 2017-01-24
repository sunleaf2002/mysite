#导入pymysql的包
import pymysql
try:
#获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
	conn=pymysql.connect(host='218.247.145.14',user='root',passwd='root99',db='project_manager',port=3306,charset='UTF8')
	cur=conn.cursor()#获取一个游标
	cur.execute('select * from employees')
	data=cur.fetchall()
	for d in data :
		#注意int类型需要使用str函数转义
	 print("ID: "+d[0])
	cur.close()#关闭游标
	conn.close()#释放数据库资源
except  Exception :print("发生异常")
