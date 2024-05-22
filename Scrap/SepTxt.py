from pathlib import Path
import sqlite3
#this code saves list of TEXT entry to TEXT DB

def SepTxt():
    SQLCommand = """
    SELECT  * FROM DOCTEXT WHERE publishYear = ?  
    """

    dbconn = sqlite3.connect("document.db")
    cursor = dbconn.cursor()
    yearNums = cursor.execute(
        '''
            SELECT DISTINCT  publishYear FROM DOCTEXT 
        '''
    ).fetchall()

    for year in yearNums:
        print(year[0])
        query = (year[0],)
        cursor.execute(SQLCommand,query)
        f = open(f"./data/{year[0]}.txt",'a',encoding='utf-8')
        i=0
        for row in cursor:
            i+=1
            text = row[9]
            textpiece = text.split("。")
            metadata = "[metadata]" + row[3] + ";" + row[4] + ";" + row[5] + ";" + row[6] + "\n"
            f.write(metadata)
            #print(metadata)
            for sentence in textpiece:
                if(len(sentence)== 0):
                    continue
                f.write( sentence+"。"+"\n")
    cursor.close()
    f.close()
    return 0

if __name__ == '__main__':
    Formatted_File = SepTxt()

