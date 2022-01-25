import os
import cx_Oracle

def main():
    while True:

        connect = cx_Oracle.connect('system/root@localhost:1521/xe')
        cursor = connect.cursor()
        
        print("Main Menu ")
        print("")
        print("  1) Admin")
        print("  2) Member")
        print("  3) Exit")
        print("")
        selection = int(input("Selection: "))
        os.system('cls')
        print()

#ADMIN MENU *********************************************************
        #LOG IN
        if selection == 1:
            username = input("Username: ")
            password = input("Password: ")
            if username == 'admin' and password == 'root':
                print("")
                print("Access granted!")
                print("")
                
                print("Admin Menu ")
                print("")
                print("  1) Add new movie")
                print("  2) Add new member")
                print("  3) Search and update movie")
                print("  4) Search and delete movie")
                print("  5) Search and update member")
                print("  6) Search and delete member")
                print("  7) Back")
                print("")
                selection1 = int(input("Selection: "))
                print()
            else:
                print('')
                print('Username or password was incorrect')
                print('')
                return main()

            #ADD MOVIE
            if selection1 == 1:

                
                movieid = input("Enter the movie ID: ")
                movietitle = input("Enter the movie title: ")
                moviecatid = input("Enter the movie category ID: ")
                movievalue = input("Enter the movie value: ")
                movieqty = input("Enter the movie quantity: ")
                
                addmovie = "INSERT INTO MM_MOVIE (MOVIE_ID, MOVIE_TITLE, MOVIE_CAT_ID, MOVIE_VALUE, MOVIE_QTY) VALUES('{0}', '{1}', '{2}', '{3}', '{4}')".format(movieid, movietitle, moviecatid, movievalue, movieqty)
                cursor.execute(addmovie)
                connect.commit()
                
                print("")
                print("Movie successfully added!")
                print("")

            #ADD MEMBER
            elif selection1 == 2:

                memberid = input("Enter new member ID: ")
                last = input("Enter new member last name: ")
                first = input("Enter new member first name: ")
                licenseno = input("Enter new member license number: ")
                licensest = input("Enter new member license state: ")
                creditcard = input("Enter new member credit card number: ")
                suspension = input("Enter member suspension status (Y/N): ")
                mailinglist = input("Will they be in the mailing list? (Y/null): ")
                
                addmember = "INSERT INTO MM_MEMBER (MEMBER_ID, LAST, FIRST, LICENSE_NO, LICENSE_ST, CREDIT_CARD, SUSPENSION, MAILING_LIST) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(memberid, first, last, licenseno, licensest, creditcard, suspension, mailinglist)
                cursor.execute(addmember)
                connect.commit()
                
                print("")
                print("Member successfully added!")
                print("")

            #UPDATE MOVIE
            elif selection1 == 3:

                print("Here is the list of movies:")
                print("")
                cursor.execute('SELECT MOVIE_ID, MOVIE_TITLE FROM MM_MOVIE')
                rows3=cursor.fetchall()
                print(*['{} : {}'.format(k,v) for k,v in rows3], sep = "\n")
                print("")
                
                mo_id = input("Enter the movie ID you would like to update: ")

                value = input('Input the new movie value you would like to update to: ')
                
                updatemovie = "UPDATE MM_MOVIE SET MOVIE_VALUE=:value WHERE MOVIE_ID=:mo_id"
                cursor.execute(updatemovie, [value, mo_id])
                connect.commit()
                
                print("")
                print("Movie value successfully updated!")
                print("")

            #UPDATE MEMBER
            elif selection1 == 5:

                print("Here is the list of members:")
                print("")
                cursor.execute('SELECT MEMBER_ID, FIRST, LAST FROM MM_MEMBER')
                rows3=cursor.fetchall()
                print(*['{} : {} {}'.format(k,v,x) for k,v,x in rows3], sep = "\n")
                print("")
                
                m_id = input("Enter the member ID you would like to update: ")

                payment = input('Input the new credit card you would like to update to: ')
                
                updatemember = "UPDATE MM_MEMBER SET CREDIT_CARD=:payment WHERE MEMBER_ID=:m_id"
                cursor.execute(updatemember, [payment, m_id])
                connect.commit()
                
                print("")
                print("Member successfully updated!")
                print("")

            #DELETE MOVIE
            elif selection1 == 4:
                print("Here is our list of movies and their IDs:")
                print("")
                cursor.execute('SELECT MOVIE_ID, MOVIE_TITLE FROM MM_MOVIE')
                rows3=cursor.fetchall()
                print(*['{} : {}'.format(k,v) for k,v in rows3], sep = "\n")
                print("")
                
                m_id = input("Enter the movie ID you would like to remove: ")
                print("")
                titleq = "DELETE FROM MM_MOVIE WHERE MOVIE_ID=:m_id"
                cursor.execute(titleq,[m_id])
                connect.commit()
                print("Movie successfully removed from the system!")
                print("")

            #DELETE MEMBER
            elif selection1 == 6:
                print("Here is the list of members:")
                print("")
                cursor.execute('SELECT MEMBER_ID, FIRST, LAST FROM MM_MEMBER')
                rows3=cursor.fetchall()
                print(*['{} : {} {}'.format(k,v,x) for k,v,x in rows3], sep = "\n")
                print("")
                
                m_id = input("Enter the member ID you would like to remove: ")
                print("")
                titleq = "DELETE FROM MM_MEMBER WHERE MEMBER_ID=15"
                cursor.execute(titleq)
                connect.commit()
                print("Member successfully removed from the system!")
                print("")

            
            elif selection1 == 7:
                return main()
            else:
                break
            
#MEMBER MENU ********************************************************
            
        elif selection == 2:
            print("Member Menu ")
            print("")
            print("  1) Search movie")
            print("  2) Rent movie")
            print("  3) Return movie")
            print("  4) Back")
            print("")
            selection2 = int(input("Selection: "))
            print()

            #SEARCH MOVIE
            if selection2 == 1:
                
                print("Here is our list of movies and their IDs:")
                print("")
                cursor.execute('SELECT MOVIE_ID, MOVIE_TITLE FROM MM_MOVIE')
                rows2=cursor.fetchall()
                print(*['{} : {}'.format(k,v) for k,v in rows2], sep = "\n")
                print("")
                
                m_id = input("Enter the movie ID you would like to search: ")
                print("")
                titleq = "SELECT MOVIE_QTY, MOVIE_VALUE FROM MM_MOVIE WHERE MOVIE_ID=:m_id"
                cursor.execute(titleq,m_id)
                rows=cursor.fetchall()
                print(*['We have {} in stock and it costs ${}0 to rent'.format(k,v) for k,v in rows],)
                print("")
                cursor.close()

            #RENT MOVIE
            elif selection2 == 2:
                print("Here is our list of movies and their IDs:")
                print("")
                cursor.execute('SELECT MOVIE_ID, MOVIE_TITLE FROM MM_MOVIE')
                rows3=cursor.fetchall()
                print(*['{} : {}'.format(k,v) for k,v in rows3], sep = "\n")
                print("")
                
                m_id = input("Enter the movie ID you would like to rent: ")
                print("")
                updatemovie = "UPDATE MM_MOVIE SET MOVIE_QTY=MOVIE_QTY-1 WHERE MOVIE_ID=:m_id"
                cursor.execute(updatemovie,[m_id])
                connect.commit()
                print("Order submitted!")
                print("")

            #RETURN MOVIE
            elif selection2 == 3:
                print("Here is our list of movies and their IDs:")
                print("")
                cursor.execute('SELECT MOVIE_ID, MOVIE_TITLE FROM MM_MOVIE')
                rows3=cursor.fetchall()
                print(*['{} : {}'.format(k,v) for k,v in rows3], sep = "\n")
                print("")
                
                m_id = input("Enter the movie ID you would like to return: ")
                print("")
                updatemovie = "UPDATE MM_MOVIE SET MOVIE_QTY=MOVIE_QTY+1 WHERE MOVIE_ID=:m_id"
                cursor.execute(updatemovie,[m_id])
                connect.commit()
                print("Return submitted!")
                print("")
            
            elif selection2 == 4:
                return main()
            else:
                break

#EXIT **************************************************************
            
        elif selection == 3:
            print("Exiting the Movie Rental System...")
            print("-")
            print("-")
            print("Goodbye!")
            break
            
        else:
            break


if __name__ == '__main__':
    main()
