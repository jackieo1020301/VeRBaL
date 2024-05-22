import sqlite3
#this code saves list of TEXT entry to TEXT DB

def write_to_DB_TEXT(Inputlist):
    if(type(Inputlist)=='NoneType'):
        print("fatalError!EmptyList")
        return
    dbconn = sqlite3.connect("document.db")
    cursor = dbconn.cursor()
    res = cursor.execute("SELECT * from sqlite_master where name = 'DOCTEXT'")
    if res.fetchone() is None:
        cursor.execute('''CREATE TABLE DOCTEXT(ID VARCHAR(40) PRIMARY KEY,
                                            publishYear INT, 
                                            policyType VARCHAR(255),
                                            publishDate VARCHAR(15),
                                            datasourceshow VARCHAR(63),
                                            sourceOrganization VARCHAR(63),
                                            title VARCHAR(255),
                                            detailUrl VARCHAR(255),    
                                            fileNumber VARCHAR(31), 
                                            content TEXT                                                                  
                                            )''')
    for element in Inputlist:
        try:
            cursor.execute(f'''INSERT OR IGNORE INTO DOCTEXT(ID,publishYear,policyType,publishDate,
                       datasourceshow,sourceOrganization,title,detailUrl,fileNumber,content)
                    VALUES("{element['id']}" , "{element['publish_year']}" , "{element['policy_type']}",
                      "{element['publishDate']}", "{element['datasourceshow']}", "{element['source_organization']}",
                      "{element['title']}", "{element['detail_url']}", "{element['file_number']}", "{element['content']}")
                    ''')
        except:
            continue
    cursor.execute("COMMIT")
    res = cursor.execute(f'''SELECT COUNT(*) FROM DOCTEXT
        ''')
    entireNum = res.fetchone()[0]
    print("currentLines:",entireNum)
    return entireNum

