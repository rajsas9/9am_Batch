import cx_Oracle
#pip install cx_Oracle
#XE or ORCL
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='xe') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'system', password='system', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute('select * from user4.emp') # use triple quotes if you want to spread your query across multiple lines
result = c.fetchall()
result = c.fetchone()
print(result)

#####################SQL STATEMENTS############################
#c.execute("CREATE DATABASE aaa")

c.execute('SELECT * FROM user4.emp WHERE ROWNUM <= 5')
for row in c: print(row)

c.execute("SELECT * FROM user4.emp WHERE ename ='SCOTT'")
result = c.fetchall()
print(result)

c.execute("SELECT * FROM user4.emp WHERE ename LIKE '%S%'")
result = c.fetchall()
print(result)

c.execute("DELETE FROM user4.emp WHERE ename='SCOTT'")
result = c.fetchall()
print(result)
#conn.commit()

c.execute("UPDATE user3.emp SET ename ='ADAM' WHERE ename ='SCOTT'")
result = c.fetchall()
print(result)


c.execute("select * from user4.emp order by ename")
result = c.fetchall()
print(result)

#To remove the , in the output use count,    
c.execute("select count(*) from user4.emp")
#The fetchone() method will return the first row of the result:
count, = c.fetchone()
print(count)


c.execute("create table abc1 as select * from user4.emp")
c.execute("drop table abc1")

c.execute("select * from tab")
c1= c.fetchall()
print(c1)

c.execute("select * from abc1")
c1= c.fetchall()
print(c1)


c.execute("CREATE TABLE cust1 (name VARCHAR(255), address VARCHAR(255))")

c.execute("""insert into cust1 values ('ABC', 'tesName')""")
c.execute("""insert into cust1 values ('XYZ', 'tesName1')""")
c.execute("select * from cust1")
c1= c.fetchall()
print(c1)
###########How many records inserted###############
print(c.rowcount, "record inserted.")
#print("1 record inserted, ID:", c.lastrowid)
##########To close the connection###############
#conn.close()
#####################################################
c = conn.cursor()
c.execute('select * from user4.emp') 
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()
   
##################################################
c.execute("SELECT * FROM user4.emp")
print(c.description)

c.execute("select * from ALL_TAB_COLUMNS where table_name = 'DUAL'")
print(c.fetchall())

#c.execute("SELECT COLUMN_NAME, DATA_TYPE FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='table_name' and OWNER='schema name'")
c.execute("SELECT COLUMN_NAME, DATA_TYPE FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='emp' and OWNER='user4'")
result = c.fetchall()
print(result)
#################################################
    
# print some details about the connection and the library
print("Database version:", conn.version)
print("Oracle Python version:", cx_Oracle.version)
    
#####################SQL JOINS############################
c.execute("SELECT * FROM user4.emp")
c.execute("SELECT * FROM user4.dept")
result = c.fetchall()
print(result)
#columns description then just use cursor.description
print(c.description)

c.execute("SELECT * FROM user4.emp")
result = c.fetchall()
print(result)


c.execute("SELECT emp.ename AS enm, dept.deptno AS dno FROM user4.emp \
          INNER JOIN user4.dept ON emp.empno = dept.deptno")
result = c.fetchall()
print(result)

c.execute("SELECT emp.ename AS enm, dept.deptno AS dno FROM user4.emp \
          LEFT JOIN user4.dept ON emp.empno = dept.deptno")
result = c.fetchall()
print(result)
#########################################################

