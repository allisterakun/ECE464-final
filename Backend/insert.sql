USE ece464;

insert into Stores values (1, "Key Food");
insert into Stores values (2, "Giant Food");
insert into Stores values (3, "Food Lion");

insert into Employees values (1, "Bully Maguire", 1, "Cashier", 20);
insert into Employees values (2, "Tom Cat", 1, "Manager", 30);
insert into Employees values (3, "Ben Simmons", 1, "Cashier", 10);
insert into Employees values (4, "Andrew Garfield", 2, "Cashier", 40);
insert into Employees values (5, "Peter Parker", 2, "Manager", 50);

insert into Login_ values (1, "two", "weeks");
insert into Login_ values (2, "Net", "Stat");
insert into Login_ values (3, "marco", "polo");
insert into Login_ values (4, "UGonnaCry", "BeatItChump");
insert into Login_ values (5, "noway", "home");

insert into ItemTypes values (1, "fruit");
insert into ItemTypes values (2, "meat");
insert into ItemTypes values (3, "drink");

insert into Products values (1, "Dr. Thunder", 1.0, 3);
insert into Products values (2, "Dr. Pepper", 2.0, 3);
insert into Products values (3, "Gatorade", 3.0, 3);
insert into Products values (4, "Powerade", 4.0, 3);

insert into Timesheet values (1, "2021-12-08", "17:00", "22:00", 12);
insert into Timesheet values (1, "2021-12-09", "17:00", "22:00", 15);
insert into Timesheet values (2, "2021-12-09", "15:00", "22:00", 10);
insert into Timesheet values (2, "2021-12-15", "15:00", "22:00", 16);
insert into Timesheet values (3, "2021-12-15", "21:00", "22:00", 16);
insert into Timesheet values (4, "2021-12-15", "15:00", "22:00", 16);

insert into Inventory values (1, 1, 15);
insert into Inventory values (2, 1, 12);
insert into Inventory values (3, 1, 11);
insert into Inventory values (4, 2, 2);

insert into Purchases values (1, 1, 1, "2021-12-08", 1.0, 12);
insert into Purchases values (1, 2, 1, "2021-12-10", 1.0, 10);
insert into Purchases values (1, 2, 2, "2021-12-09", 1.0, 11);