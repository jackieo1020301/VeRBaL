from pathlib import Path
import sqlite3
import json
#this code saves list of TEXT entry to TEXT DB

def DBToJson(SQLCommand):
    dbconn = sqlite3.connect("../document.db")
    cursor = dbconn.cursor()
    res = cursor.execute(SQLCommand)
    outputList = res.fetchall()
    ret = json.dumps(outputList,ensure_ascii=False)
    return ret

def JsonToDB(filename):
    file = open(filename,'r',encoding='utf-8')
    data = file.readlines()
    print(data)

#this code inputs raw text (str) , outputs a list of document entry
def StrToDoc(str,ifTesting):
    result=[]
    
    if(ifTesting):
        filename = 'documents-none.txt'
        str = Path(filename).read_text('utf-8')
    jsonStr = json.loads(str)
    try:
        recordLen = len(jsonStr['datas']['records'])
    except:
        print("fatalError")
        return
    for i in range(0,recordLen):

        rawTitle = jsonStr['datas']['records'][i]['title']
        rawTitle = ''.join(rawTitle.split("<em>"))
        cleanTitle = ''.join(rawTitle.split("</em>"))

        element={
        'publish_year' :        jsonStr['datas']['records'][i]['publish_year'],
        'id' :                  jsonStr['datas']['records'][i]['dataId'],
        'policy_type' :         jsonStr['datas']['records'][i]['policy_type'],
        'publishDate' :         jsonStr['datas']['records'][i]['publishDate'],
        'datasourceshow' :      jsonStr['datas']['records'][i]['datasourceshow'],
        'source_organization' : jsonStr['datas']['records'][i]['source_organization'],
        'title' :               cleanTitle,
        'content' :           jsonStr['datas']['records'][i]['_abstract'],
        'detail_url' :          jsonStr['datas']['records'][i]['detail_url'],
        'file_number' :         jsonStr['datas']['records'][i]['file_number'],
        }
        result.append(element)
    return result

if __name__ == '__main__':
    SQLCommand = """
    SELECT  ID,sourceOrganization,title , content FROM DOCTEXT 
    WHERE datasourceshow == "交通运输部" AND policyType == "政策文件"
    GROUP BY sourceOrganization
    ORDER BY COUNT(sourceOrganization) DESC
    """
    
    filename = "Transport.json"
    Formatted_File = DBToJson(SQLCommand)
    JsonToDB("Transport.json")

    file = open(filename,'w',encoding='utf-8')
    file.write(Formatted_File)
