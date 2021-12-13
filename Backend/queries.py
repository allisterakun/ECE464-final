from flask import json

def getPosition(cursor, _id):
    cursor.execute("SELECT position FROM Employees WHERE employee_id = '" + str(_id) + "';")
    position = cursor.fetchone()
    return position
    # return str(position)


def add_timesheet(cursor, _id, work_date, clock_in_time, clock_out_time, items_sold):
    cursor.execute("insert into Timesheet values (" + str(_id) + ", '" + str(work_date) + "', '" + str(clock_in_time) + "', '" + str(clock_out_time) + "', " + str(items_sold) + ");")
    return
    # return None


def get_timesheet(cursor, _id):
    cursor.execute("SELECT work_date, clock_in_time, clock_out_time, items_sold FROM Timesheet WHERE employee_id = " + str(_id) + ";")
    row_headers = [x[0] for x in cursor.description] # get row headers
    rows = cursor.fetchall()

    json_data = []
    for result in rows:
        json_data.append({
                            row_headers[0]: str(result[0]),
                            row_headers[1]: str(result[1]),
                            row_headers[2]: str(result[2]),
                            row_headers[3]: result[3]
                        })
    return json_data
    # return table (work_date DATE, clock_in_time TIME, clock_out_time TIME, items_sold INT)
    

def get_all_timesheets(cursor, store_id, start_date, end_date):
    cursor.execute("SELECT employee_name, work_date, clock_in_time, clock_out_time, items_sold, salary \
                    FROM Timesheet JOIN Employees ON Timesheet.employee_id = Employees.employee_id \
                    WHERE store_id = "+ str(store_id) + " AND work_date BETWEEN '" + str(start_date) + "' AND '" + str(end_date) + "';")
    row_headers = [x[0] for x in cursor.description] # get row headers
    rows = cursor.fetchall()

    json_data = []
    for result in rows:
        json_data.append({
                            row_headers[0]: result[0], 
                            row_headers[1]: str(result[1]),
                            row_headers[2]: str(result[2]),
                            row_headers[3]: str(result[3]),
                            row_headers[4]: result[4],
                            row_headers[5]: result[5]
                        })
    return json_data
    # join timesheets and employee on employee_id
    # return table (employee_name STRING, work_date DATE, clock_in_time TIME, clock_out_time TIME, items_sold INT)


def get_all_salary_info(cursor, store_id, start_date, end_date):
    cursor.execute("SELECT employee_name, work_date, ABS(TIMESTAMPDIFF(HOUR, clock_out_time, clock_in_time)) AS shift_hours, salary \
                    FROM Timesheet JOIN Employees ON Timesheet.employee_id = Employees.employee_id \
                    WHERE store_id = "+ str(store_id) + " AND work_date BETWEEN '" + str(start_date) + "' AND '" + str(end_date) + "';")
    row_headers = [x[0] for x in cursor.description]
    rows = cursor.fetchall()
    
    json_data = []
    for row in rows:
        json_data.append({
                            row_headers[0]: row[0], 
                            row_headers[1]: str(row[1]),
                            row_headers[2]: row[2],
                            row_headers[3]: row[3]
                        })

    salary_info = {}
    for row in json_data:
        if row["employee_name"] not in salary_info:
            salary_info[row["employee_name"]] = 0
        salary_info[row["employee_name"]] += row["shift_hours"] * row["salary"]        

    return salary_info

    # join timesheet and employees on employee_id
    # then use python logic to get the necessary values
    # return table (employee_name STRING, work_date DATE, clock_out_time - clock_in_time TIME, salary INT)


def getSoldAmountTotal(cursor, store_id, start_date, end_date):
    cursor.execute("SELECT price_sold_at, quantity \
                    FROM Purchases \
                    WHERE store_id = '" + str(store_id) + "' \
                        AND purchase_date BETWEEN '" + str(start_date) + "' and '" + str(end_date) + "';")
    
    data = cursor.fetchall()
    total = 0

    for row in data:
        total += row[0] * row[1]
    
    return total
    # return table and do it in python (price_sold_at INT, quantity INT)


def get_inventory_general(cursor, store_id):
    cursor.execute("SELECT product_name, sell_price, quantity \
                    FROM Products JOIN Inventory ON Products.product_id = Inventory.product_id \
                    WHERE Inventory.store_id = " + str(store_id) + ";")
    
    row_headers = [x[0] for x in cursor.description]
    rows = cursor.fetchall()
    
    json_data = []
    for row in rows:
        json_data.append({
                            row_headers[0]: row[0], 
                            row_headers[1]: row[1],
                            row_headers[2]: row[2]
                        })

    return json_data
    # join products and inventory on product_id
    # return table (product_name, sell_price, quantity)
    

def get_inventory_specific_type_products(cursor, store_id, product_ids):
    cursor.execute("SELECT Products.product_name, Products.sell_price, Inventory.quantity \
                    FROM Products JOIN Inventory ON Products.product_id = Inventory.product_id \
                    WHERE store_id = " + str(store_id) + " AND Inventory.product_id IN (" + str(product_ids)[1:-1] + ");")

    row_headers = [x[0] for x in cursor.description]
    rows = cursor.fetchall()

    json_data = []
    for row in rows:
        json_data.append({
                            row_headers[0]: row[0], 
                            row_headers[1]: row[1],
                            row_headers[2]: row[2]
                        })

    return json_data
    # join products and inventory on product_id
    # return table (product_name, sell_price, quantity)


def get_product_info(cursor, store_id, item_type_id):
    cursor.execute("SELECT Products.product_id FROM Products JOIN Inventory ON Products.product_id = Inventory.product_id JOIN ItemTypes ON ItemTypes.item_type_id = Products.item_type_id \
                    WHERE store_id = " + str(store_id) + " AND Products.item_type_id = " + str(item_type_id) + ";")

    product_ids = cursor.fetchall()
    product_ids = [product[0] for product in product_ids]
    return product_ids
    # return llist(product_id) INT


def get_specific_product_info(cursor, store_id, product_name):
    cursor.execute("SELECT Products.product_id, sell_price FROM Products JOIN Inventory ON Products.product_id = Inventory.product_id WHERE store_id = " + str(store_id) + " AND product_name = '" + product_name + "';")
    data = cursor.fetchone()
    return data
    # return product_id, sell_price INT
    

def get_quantity_specific_product(cursor, product_id, store_id):
    cursor.execute("SELECT quantity FROM Inventory WHERE store_id = " + str(store_id) + " AND product_id = " + str(product_id) + ";")
    quantity = cursor.fetchone()
    return quantity
    # return quantity INT


def add_purchases(cursor, employee_id, current_date, price_sold_at, product_id, store_id, quantity):
    cursor.execute("INSERT INTO Purchases values (" + str(product_id) + ", " + str(employee_id) + ", " + str(store_id) + ", " + str(current_date) + ", " + str(price_sold_at) + ", " + str(quantity) + ");")
    return
    # insert 
    # return None
    

def update_inventory(cursor, store_id, product_id, quantity):
    cursor.execute("UPDATE Inventory SET quantity = " + str(quantity) + " WHERE store_id = " + str(store_id) + " AND product_id = " + str(product_id) + ";")
    return
    # update
    # return None
    

def product_exists(cursor, product_id):
    cursor.execute("SELECT EXISTS (SELECT * FROM Inventory WHERE product_id = " + str(product_id) + ");")
    _exists = cursor.fetchone()
    return _exists
    # return Bool
    

def add_inventory(cursor, store_id, product_id, quantity):
    cursor.execute("INSERT INTO Inventory values (" + str(product_id) + ", " + str(store_id) + ", " + str(quantity) + ");")
    return
    # insert
    # return None

def get_all_purchases(cursor, store_id):
    cursor.execute("SELECT product_name, Employees.employee_name, purchase_date, price_sold_at, quantity FROM Purchases JOIN Employees ON Employees.employee_id = Purchases.employee_id AND Employees.store_id = Purchases.store_id JOIN Products ON Products.product_id = Purchases.product_id WHERE Employees.store_id = " + str(store_id) + " ORDER BY purchase_date DESC;")

    row_headers = [x[0] for x in cursor.description]
    rows = cursor.fetchall()

    json_data = []
    for row in rows:
        json_data.append({
                            row_headers[0]: row[0], 
                            row_headers[1]: row[1],
                            row_headers[2]: row[2],
                            row_headers[3]: row[3],
                            row_headers[4]: row[4]
                        })

    return json_data

    