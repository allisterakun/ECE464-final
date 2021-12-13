import os
def setup():
    print("Enter password:")
    password = input()
    os.system("mysql -u root -p"+ password +" < .\\b.sql ")
    os.system("mysql -u root -p" + password + " < .\\schema.sql")
    os.system("mysql -u root -p" + password + " < .\\insert.sql")
    return "success"

if __name__ == "__main__":
    setup();