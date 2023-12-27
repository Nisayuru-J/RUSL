from models.database import get_connection , end_transaction

class UserAccount:
    def __init__(self):
        pass
        
    def add(self, username, password):
        conn , c = get_connection()
        c.execute("INSERT INTO user_account (username, password) VALUES (%s, %s)", (username, password))
        end_transaction(conn, c)

    #a function to update the user's password
    def update_password(self, username, password):
        conn , c = get_connection()
        c.execute("UPDATE user_account SET password = %s WHERE username = %s", (password, username))
        end_transaction(conn, c)

    def get_usernames(self):
        conn , c = get_connection()
        c.execute("SELECT username FROM user_account")
        res = c.fetchall()
        
        usernames = []
        #loop through the result and append the usernames to the list
        for username in res:
            usernames.append(str(username[0]))
        end_transaction(conn, c)
        print(usernames)
        return usernames
    
    def get_password(self, username):
        conn , c = get_connection()
        # c.execute("SELECT password FROM user_account WHERE username=:username", {"username": username})
        c.execute("SELECT password FROM user_account WHERE username = %s", (username,))

        res = c.fetchall()
        end_transaction(conn, c)
        return res
    
