from query import Query
import pyodbc
import schedule
import time
from datetime import datetime
import query
period=5*3600
print(query.x)
def DB_Connection():
  server = 'localhost' 
  database = 'YourDB' 
  username = 'SA' 
  password = 'Sriraj@21' 
  return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  

connection=DB_Connection() #DB connection

def Get_Date_String(date):
      return date.strftime('%Y-%m-%d')

def Get_MasterOrders():
  cursor=connection.cursor()
  query="""SELECT WorkOrderNo,Company,Shipment_Date from Order_Acceptance_Main where Company LIKE '%PARADIGM%'"""
  cursor.execute(query)
  masterOrders=[]
  for i in cursor:
        order={}
        order['id']=i[0]
        order['title']=i[1]
        order['endDate']=Get_Date_String(i[2])
        masterOrders.append(order)
  for i in masterOrders:
    print(i)   

def Force_Fetch_Data():
  print("-----------------------------------------------------------------------")
  Get_MasterOrders()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print("Current Time =", current_time)  
    

Force_Fetch_Data()
while True:
  schedule.run_pending()
  time.sleep(1)
