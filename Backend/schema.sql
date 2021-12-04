USE ece464;
create table if not exists Stores(
    store_id INT NOT NULL AUTO_INCREMENT,
    store_name CHAR(100) NOT NULL,
    PRIMARY KEY ( store_id )
);
create table if not exists Employees(
    employee_id INT NOT NULL AUTO_INCREMENT,
    employee_name CHAR(100) NOT NULL,
    store_id INT,
    position CHAR(40) NOT NULL,
    salary INT NOT NULL,
    PRIMARY KEY ( employee_id ),
    FOREIGN KEY (store_id) REFERENCES Stores( store_id ) ON DELETE CASCADE
);
create table if not exists Login_(
    employee_id INT,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    PRIMARY KEY ( employee_id ),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) ON DELETE CASCADE
);
create table if not exists Timesheet(
    employee_id INT,
    work_date DATE,
    clock_in_time TIME,
    clock_out_time TIME,
    items_sold INT NOT NULL,
    PRIMARY KEY ( employee_id ),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) ON DELETE CASCADE
);
create table if not exists ItemTypes(
    item_type_id INT NOT NULL,
    item_type VARCHAR(100) NOT NULL,
    PRIMARY KEY ( item_type_id )
);
create table if not exists Products(
    product_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    sell_price FLOAT(5, 2) NOT NULL,
    item_type_id INT,
    PRIMARY KEY ( product_id ),
    FOREIGN KEY (item_type_id) REFERENCES ItemTypes(item_type_id) ON DELETE CASCADE
);
create table if not exists Inventory(
    product_id INT,
    store_id INT,
    quantity INT NOT NULL,
    PRIMARY KEY ( store_id, product_id ),
    FOREIGN KEY (product_id) REFERENCES Products( product_id ),
    FOREIGN KEY (store_id) REFERENCES Stores( store_id )
);
create table if not exists Purchases(
    product_id INT,
    employee_id INT,
    purchase_date DATE NOT NULL,
    price_sold_at FLOAT(5,2),
    quantity INT NOT NULL,
    PRIMARY KEY (purchase_date, product_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) ON DELETE CASCADE
);