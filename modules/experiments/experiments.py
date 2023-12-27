from models.database import get_connection , end_transaction

class Experiment:
    def __init__(self):
        pass
    
    def get_reactions2(self):
        conn , c = get_connection()
        c.execute("SELECT distinct id, reaction FROM experiments")
        res = c.fetchall()
        
        reactions = {}
        #loop through the result and append the indicators to the list
        for indicator in res:
            #indicators.append(str(indicator[0]))
            reactions[str(indicator[0])] = str(indicator[1])
        end_transaction(conn, c)
        print(reactions)
        return reactions
    

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



    def get_indicators(self, reaction):
        conn , c = get_connection()
        c.execute("SELECT indicator FROM experiments where reaction = %s", (reaction,))
        res = c.fetchall()
        
        indicators = []
        #loop through the result and append the indicators to the list
        for indicator in res:
            indicators.append(str(indicator[0]))
        end_transaction(conn, c)
        print(indicators)
        return indicators
    
    def get_analyte(self, reaction , indicator):
        conn , c = get_connection()
        c.execute("SELECT analyte FROM experiments where reaction = %s and indicator =%s", (reaction,indicator))
        res = c.fetchall()
        
        analytes = []
        
        for analyte in res:
            analytes.append(str(analyte[0]))
        end_transaction(conn, c)
        print(analytes)
        return analytes
    

