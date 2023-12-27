from models.database import get_connection , end_transaction

class Titration:
    def __init__(self):
        pass
        self.colors = ['Blue', 'Pink', 'Red', 'Yellow']
        
    def add(self, titration_dic):
        conn , c = get_connection()
        start_pred_class = self.colors[titration_dic['start_pred_class']]
        changed_pred_class = self.colors[titration_dic['changed_pred_class']]

        c.execute("INSERT INTO titration (reaction, indicator, analyte, start_time, end_time, start_pred_class, changed_pred_class, username, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (titration_dic['reaction'],titration_dic['indicator'],titration_dic['analyte'],titration_dic['start_time'],titration_dic['end_time'],start_pred_class,changed_pred_class, titration_dic['user_name'], titration_dic['volume']))
        print("inserted")
        end_transaction(conn, c)

    def get_titrations(self, username):
        conn , c = get_connection()
        c.execute("SELECT reaction, indicator, analyte, start_pred_class, changed_pred_class, volume FROM titration WHERE username = %s", (username,))
        res = c.fetchall()
        end_transaction(conn, c)
        return res


    def get_reactions(self):
        conn , c = get_connection()
        c.execute("SELECT distinct reaction FROM experiments")
        res = c.fetchall()
        
        reactions = []
        #loop through the result and append the indicators to the list
        for indicator in res:
            reactions.append(str(indicator[0]))
         
        end_transaction(conn, c)
        print(reactions)
        return reactions
