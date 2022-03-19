from tkinter import messagebox
import mysql.connector
import sys
import openpyxl
from baseIntialization import UiFields


try:
    mysqlDB = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '1234',
        database = 'Shop',
        auth_plugin='mysql_native_password'
    )
    cursor = mysqlDB.cursor()
except Exception as e:
    messagebox.showerror("Error","Error in CONNECTING TO DATABASE : {0}".format(e))
    sys.exit()

def saveCustomerData(u:UiFields, name,mobile,addhar_number, address):
    data = []
    if(mobile!=''):
        try:
            comd = ("Select * from customer where phone_no = "+str(mobile)+ ";")
            print(comd)
            cursor.execute(comd)
            data = cursor.fetchall()
        except Exception:
            print("There is a exception in find if customer exists ?: {0}".format(e))
        if(len(data) > 0):
            return
        
        if(name!='' and mobile!=''):
            try:
                if(addhar_number == ''):
                    addhar_number = 1234
                if(address == ''):
                    address = 'BBSR'
                # if(addhar_number!='' and address!=''):
                comd = ("INSERT INTO customer(cust_name, phone_no, address, addhar_number) VALUES("+"'" +name+ "'," +mobile+ ",'" +address+ "'," +str(addhar_number)+ ");")
                print(comd)
                cursor.execute(comd)
                mysqlDB.commit()
                # elif(addhar_number!=''):
                #     comd = ("INSERT INTO customer(cust_name, phone_no, addhar_number) VALUES("+"'" +name+ "'," +mobile+ "," +addhar_number+ ");")
                #     print(comd)
                #     cursor.execute(comd)
                #     mysqlDB.commit()
                # else:
                #     comd = ("INSERT INTO customer(cust_name, phone_no, address) VALUES("+"'" +name+ "'," +mobile+ ",'" +address+ "');")
                #     print(comd)
                #     cursor.execute(comd)
                #     mysqlDB.commit()
            except Exception as e:
                print("There was a exception while entering into database CUSTOMER : {0}".format(e))
#important       
def saveGstData(weight,ornament,gold_rate,total_val,cgst,sgst,net_total):
    try:
        comd = ("INSERT INTO gst_table(ornament, qty,weight,gold_rate, total_val, cgst, sgst, net_total) VALUES('" +ornament+ "'," +str(1)+ ","+str(weight)+ "," +str(gold_rate)+ "," +str(total_val)+ "," +str(cgst)+ "," +str(sgst)+ "," +str(net_total)+ ");")
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception as e:
        messagebox.showerror("Error","Error in save GST Data : {0}".format(e))
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
    except Exception as e:  
        print("there is a exception in findbynumber : {0}".format(e))
    

def findBillNumber():
    try:
        comd = ("select id from BillTable order by id desc limit 1;")
        print(comd)
        cursor.execute(comd)
        # cursor.fetchall()
        result = cursor.fetchone()
        print(result)
        
        
        if(result == None):
            return 1
        
        return result[0]+1
    except Exception:
        print("there is a error in findbillnumber : {0}".format())


def saveBillLocation(u:UiFields):
    if(u.mobile_txt.get()!=''):
        try:
            cursor.execute('select id from customer where phone_no = ' +str(u.mobile_txt.get())+ ';')
            check = cursor.fetchone()
            if(check != None):
                u.customer_id = check[0]
            else:
                cursor.execute('select id from customer order by id desc Limit 1')
                u.customer_id = cursor.fetchone()[0]
        except Exception:
            u.customer_id = 1
            print("Error in saveBillLocation in finding customer_id")
    print(u.customer_id)
    try:     
        comd = ("INSERT INTO BILLTable(bill_location, customer_id) VALUES('" +u.saveLocation+ "'," +str(u.customer_id)+");")
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception as e:
        print("Error in saveBill in saving : {0}".format(e))
        
#important        
def findGst(u:UiFields):
    try:
        comd = "Select * from gst_table;"
        print(comd)
        cursor.execute(comd)
        # for gst in cursor.fetchall():
        #     print(gst)
        wb = openpyxl.Workbook()
        sh1 = wb.active
        sh1.title = 'gst'
        
        i = 0
        j = 1
        for gst in cursor.fetchall():
            for c in gst:
                location = chr(65+i)+''+str(j)
                if(i == 1):
                    sh1[location] = str(c)[0:10]
                # print(location)
                else:
                    sh1[location] = c
                i+=1
            j+=1
            i = 0
            
        wb.save(filename='gst.xlsx')
        
            
        
    except Exception as e:
        messagebox.showerror("Error","Error in save GST Data : {0}".format(e))
        print("There is an error in finding gst data")
        
        
def saveGoldRate(u:UiFields):
    try:
        comd = ("INSERT INTO daily_gold_rate(gold_rate) VALUES("+str(u.gold_rate)+");")
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception as e:
        print("Error in saving into gold rate : {0}".format(e))

#important
def findGoldRate(u:UiFields):
    try:
        comd = ("SELECT gold_rate from daily_gold_rate order by id desc limit 1")
        print(comd)
        cursor.execute(comd)
        result = cursor.fetchone()
        if(result == None):
            u.gold_rate = 4876
        else:
            u.gold_rate = int(result[0])
    except Exception as e:
        messagebox.showerror("Error","Error in save GST Data : {0}".format(e))
        print("Error in finding gold rate")


def findGRDate(u:UiFields):
    try:
        comd = ("SELECT gold_rate from daily_gold_rate WHERE added_date = '" +u.grFindDate+ "';")
        print(comd)
        cursor.execute(comd)
        result = cursor.fetchone()
        if(result == None):
            pass
        else:
            u.grRateOnDate = result[0]
    except Exception as e:
        print("There is a error in finding gold rate by date: {0}".format(e))
        
# def findBASEDIR(u:UiFields):
#     try:
#         comd = ('SELECT valuee FROM config WHERE keyy = "BASEDIR";')
#         cursor.execute(comd)
#         result = cursor.fetchone()
#         if result == None:
#             return "."
#         return result[0]
#     except Exception:
#         print("Error in finding base dir")
    
        