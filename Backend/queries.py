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
    

def get_all_timesheets(cursor, start_date, end_date):
    cursor.execute("SELECT employee_name, work_date, clock_in_time, clock_out_time, items_sold \
                    FROM Timesheet JOIN Employees ON Timesheet.employee_id = Employees.employee_id \
                    WHERE work_date BETWEEN '" + str(start_date) + "' AND '" + str(end_date) + "';")
    row_headers=[x[0] for x in cursor.description] # get row headers
    rows = cursor.fetchall()

    json_data = []
    for result in rows:
        json_data.append({
                            row_headers[0]: result[0], 
                            row_headers[1]: str(result[1]),
                            row_headers[2]: str(result[2]),
                            row_headers[3]: str(result[3]),
                            row_headers[4]: result[4]
                        })
    return json_data
    # join timesheets and employee on employee_id
    # return table (employee_name STRING, work_date DATE, clock_in_time TIME, clock_out_time TIME, items_sold INT)


def get_all_salary_info(cursor, start_date, end_date):
    # join timesheet and employee on employee_id
    # return table (employee_name STRING, work_date DATE, clock_out_time - clock_in_time TIME, salary INT)
    pass

def getSoldAmountTotal(cursor, store_id, start_date, end_date):
    # return table and do it in python (price_sold_at INT, quantity INT)
    pass

def get_inventory_general(cursor, store_id):
    # join products and inventory on product_id
    # return table (product_name, sell_price, quantity)
    pass

def get_inventory_specific_product(cursor, store_id, product_id):
    # join products and inventory on product_id
    # return table (product_name, sell_price, quantity)
    pass

def get_product_info(cursor, product_name):
    # return product_id INT
    pass

def get_quantity_specific_product(cursor, product_id, store_id):
    # return quantity INT
    pass

def add_purchases(cursor, employee_id, current_date, price_sold_at, product_id, quantity):
    # insert 
    # return None
    pass

def update_inventory(cursor, store_id, product_id, quantity):
    # update
    # return None
    pass

def product_exists(cursor, product_id):
    # return Bool
    pass

def add_inventory(cursor, store_id, product_id, quantity):
    # insert
    # return None
    pass