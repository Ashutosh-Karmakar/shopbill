import mysql.connector
mysqlDB = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234',
    database = 'Shop'
)
cursor = mysqlDB.cursor()

def saveCustomerData(name,mobile,addhar_number,address):
    try:
        comd = ("INSERT INTO customer(cust_name, phone_no, address, addhar_number) VALUES("+"'" +name+ "'," +mobile+ "," +addhar_number+ ",'" +address+ "');")
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception:
        print("There was a exception while entering into database CUSTOMER")
        
def saveGstData(qty,weight,ornament,gold_rate,total_val,cgst,sgst,net_total):
    try:
        comd = ("INSERT INTO gst_table(ornament, qty, weight,gold_rate, total_val, cgst, sgst, net_total) VALUES('" +ornament+ "'," +str(qty)+ "," +str(weight)+ "," +str(gold_rate)+ "," +str(total_val)+ "," +str(cgst)+ "," +str(sgst)+ "," +str(net_total)+ ");")
        print(comd)
        cursor.execute(comd)
        mysqlDB.commit()
    except Exception:
        print("There was a exception while entering into database GST")
