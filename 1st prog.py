import sqlite3 as lite


# funcality gose here


class Databasemanage(object):

    def __init__(self):
        global con 
        try:
            con = lite.connect('course db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print('unable to create a db')

    # create data
    def insert_data(self,data):
        try:
            with con:
                
                cur = con.cursor()
                
                cur.execute(
                    "INSERT INTO course(name,description,price,is_private)VALUES (?,?,?,?)", data
                    )
                return True
        except Exception:
            return False

    # rade data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False
    # delete data
    def delete_data(self,id):
        try:
            with con:
                cur = con.cursor()
                sql="DELETE FROM course WHERE Id = ?"
                cur.execute(sql,[id])                
                return True
        except Exception:
            return False        


# provide interface to user

def main():
    print("*"*40)
    print("\n :: COURSE MANAGEMENT :: \n")
    print("*"*40)
    print("\n")

    db = Databasemanage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print("\nPRESS 1. insret a new coureses\n")
    print("PRESS 3. Delete a  courese(NEED ID OF COURSE)\n")
    print("PRESS 2. show all coureses\n")
    print("#"*40)
    print("\n")

    choice = input("\n enter a choice : ")

    if choice == "1":
        name = input("\n enter course name : ")
        description = input("\n enter course descriprion : ")
        price = input("\n enter course price : ")
        private = input("\n enter course (0/1) : ")

        if db.insert_data([name,description,price,private]):
            print("Course was inserted successfully")
        else:    
            print("OOPs something went wrong")

    elif choice =="2":
        print("\n:: Course list :: ")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index + 1))
            print("Course ID : " + str(item[0]))
            print("Course Name : " + str(item[1]))
            print("Course description : " + str(item[2]))
            print("Course price : " + str(item[3]))
            private = "Yes" if item[4] else "NO"
            print("Is Private : " + private)
            print("\n")

    elif choice =="3":
        record_id = input("Enter the course id : ")

        if db.delete_data(record_id):
            print("Course was delated successfully")
        else:
            print("OOPs some thing went wrong")

    else:
        print("\n BAD Choice") 

if __name__=='__main__':
    main()
