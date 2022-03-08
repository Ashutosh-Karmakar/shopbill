from lib2to3.pgen2.token import CIRCUMFLEX
import mysql.connector
import sys

from baseIntialization import UiFields

mysqlDB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234',
    database = 'Shop'
)
cursor = mysqlDB.cursor()

def saveCustomerData(name,mobile,addhar_number, address, bill_location = "LOCATION"):
    data = []
    if(mobile!=''):
        try:
            comd = ("Select * from customer where phone_no = "+str(mobile)+ ";")
            print(comd)
            cursor.execute(comd)
            data = cursor.fetchall()
        except Exception:
            print("There is a exception in find if customer exists ?")
        if(len(data) > 0):
            return
        
        if(name!='' and mobile!=''):
            try:
                if(addhar_number!='' and address!=''):
                    comd = ("INSERT INTO customer(cust_name, phone_no, address, addhar_number, bill_location) VALUES("+"'" +name+ "'," +mobile+ ",'" +address+ "'," +addhar_number+ ", '" +bill_location+ "');")
                    print(comd)
                    cursor.execute(comd)
                    mysqlDB.commit()
                elif(addhar_number!=''):
                    comd = ("INSERT INTO customer(cust_name, phone_no, addhar_number, bill_location) VALUES("+"'" +name+ "'," +mobile+ "," +addhar_number+ ", '" +bill_location+ "');")
                    print(comd)
                    cursor.execute(comd)
                    mysqlDB.commit()
                else:
                    comd = ("INSERT INTO customer(cust_name, phone_no, address, bill_location) VALUES("+"'" +name+ "'," +mobile+ ",'" +address+ "', '" +bill_location+ "');")
                    print(comd)
                    cursor.execute(comd)
                    mysqlDB.commit()
            except Exception:
                print("There was a exception while entering into database CUSTOMER")
        
def saveGstData(weight,ornament,gold_rate,total_val,cgst,sgst,net_total):
    try:
        comd = ("INSERT INTO gst_table(ornament, weight,gold_rate, total_val, cgst, sgst, net_total) VALUES('" +ornament+ "'," +str(weight)+ "," +str(gold_rate)+ "," +str(total_val)+ "," +str(cgst)+ "," +str(sgst)+ "," +str(net_total)+ ");")
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception:
        print("There was a exception in save GST Data")
        
def findByNumber(number):
    try:
        comd = ("Select * from customer where phone_no = "+str(number)+ ";")
        print(comd)
        cursor.execute(comd)
        data = cursor.fetchall()
        if len(data) == 0:
            return 0
        cust_data = []
        for i in data:
            cust_data.append(i)
        return cust_data[0]
    except Exception:  
        print("there is a exception in findbynumber()")
    

def findBillNumber():
    try:
        comd = ("select id from customer order by id desc limit 1;")
        cursor.execute(comd)
        result = 0
        for i in cursor:
            result = i
            break
        return int(result[0])+1    
    except Exception:
        print("there is a error in findbillnumber")

# def saveBillLocation(u:UiFields,folderName):
#     comd = "UPDATE customer SET bill_location = '" + folderName + "' WHERE id = " +u.bill_txt.get()+ ";"
#     print(comd)
#     cursor.execute(comd)
        