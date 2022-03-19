- third.py == this is mainly the ui part of the code
- baseInitialization.py == here all the initializations are done
- database.py == here all the database operations are done 
- billgenerator.py == here all the excel styling is done and printing standarda are set
- findBill.py == here the finding operatiuon of the code works
- goldrate.py == here changing of goldrate window work is done
- monhlygst.py == here gst finding widow code is written and we can add date to get the gst data
- printer.py == here printing operation is operation is done

# Running Program:

- first install mysql using [mysql/installer/8.0.28](https://dev.mysql.com/downloads/installer/).

- download the (mysql-installer-community-8.0.28.0.msi) file.

- install in developer mode.

- install the requirements step by step.

- Then product configuration is done.

- use legacy authentication method.

- set the password as 1234 if u set anything else it will create problems.

- complete all the steps and then u have installed mysql and also workbench.

- in workbench go into root : run the code one by one written in database section bellow.

- then run the setup.exe file that will install all the python requirements

- you need to install the correct version of the python that is : 

- you need to have excel installed in your system.



# BaseInitialization:

- mainly all the initializations are written in the baseInitialization.py file and all other files use this.\
- this helps us to call any funcion by just passing the object of that class

# Databases:
- There are three tables that is : gst_table, customer, billtable.

# table creation : 
## Database:
```
CREATE DATABASE shop;
```
```
USE shop;
```

#### Customer:
```
CREATE TABLE customer(
	id INT AUTO_INCREMENT,
	cust_name VARCHAR(50),
	phone_no VARCHAR(11),
	address VARCHAR(100),
	addhar_number VARCHAR(15),
	PRIMARY KEY(id)
);
```
#### GsT Table:
```
CREATE TABLE gst_table(
	id INT AUTO_INCREMENT,
	added_date DATETIME DEFAULT(CURRENT_DATE),
	ornament VARCHAR(50),
	qty INT,
	weight DECIMAL(10,2),
	gold_rate DECIMAL(10,2),
	total_val DECIMAL(10,2),
	cgst DECIMAL(10,2),
	sgst DECIMAL(10,2),
	net_total DECIMAL(10,2),
	PRIMARY KEY(id)
);
```

#### Bill Table:
```
CREATE TABLE billtable(
	id INT AUTO_INCREMENT,
	bill_location VARCHAR(100),
	billing_date DATETIME DEFAULT(curdate()),
	customer_id INT,
	PRIMARY KEY(id),
	FOREIGN KEY (customer_id) REFERENCES customer(id)
);
```

#### Gold Rate:
```
CREATE TABLE daily_gold_rate(
	id INT AUTO_INCREMENT,
	added_date DATETIME DEFAULT(curdate()),
	gold_rate DECIMAL(10,2),
	PRIMARY KEY(id)
);
```

```
pyinstaller --noconfirm --onedir --console --add-data "D:/Coding/exeshop/shopbill/FrontEnd/__init__.py;." --add-data "D:/Coding/exeshop/shopbill/FrontEnd/backend.py;." --add-data "D:/Coding/exeshop/shopbill/FrontEnd/baseIntialization.py;." --add-data "D:/Coding/exeshop/shopbill/FrontEnd/billgenerator.py;." --add-data "D:/Coding/exeshop/shopbill/FrontEnd/database.py;." --add-data "D:/Coding/exeshop/shopbill/FrontEnd/findBill.py;." --add-data "D:/Coding/exeshop/shopbill/FrontEnd/findGoldrate.py;." --add-data "D:/Coding/exeshop/shopbill/FrontEnd/goldrate.py;." --add-data "D:/Coding/exeshop/shopbill/FrontEnd/monthlyGST.py;." --add-data "D:/Coding/exeshop/shopbill/FrontEnd/printer.py;." --hidden-import "mysql" --hidden-import "mysql.connector" --hidden-import "win32api" --hidden-import "win32print" --hidden-import "tkinter" --hidden-import "tkcalendar" --hidden-import "datetime" --hidden-import "openpyxl" --hidden-import "sys" --hidden-import "pyautogui" --hidden-import "os" --hidden-import "threading" --hidden-import "tkcalendar.calendar_" --hidden-import "babel" --hidden-import "babel.numbers"  "D:/Coding/exeshop/shopbill/FrontEnd/third.py"
```
