from Scrap.Formatting import StrToDoc
from Scrap.ConnToDB import write_to_DB_TEXT
import sqlite3
import time
import random
import traceback
import json
import requests

def requestRawDocs(updatedCookie,payload):
    baseurl="https://policy.ckcest.cn/data/es/search"
    payload = payload
    headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,eo;q=0.7',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json',
    'Cookie': updatedCookie,
    'Host':'policy.ckcest.cn',
    'Origin': 'https://policy.ckcest.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://policy.ckcest.cn/search.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
    response = requests.post(baseurl,data=json.dumps(payload),timeout=10,headers=headers)
    response.encoding = 'utf-8'
    rawtext = response.text
    return rawtext

def request_payload_generate(fetchNumber,pivot):
    CurNum = pivot
    dbconnQuery = sqlite3.connect("document-link.db")
    cursor = dbconnQuery.cursor()
    query = f"SELECT * from DOCUMENT limit {CurNum} ,{fetchNumber}"
    res = cursor.execute(query)
    payloads = []
    for i in range(0,fetchNumber):
        try:
            payload = {
            'type' : ["1005"],
            'page' : 1,
            'cnt' : 20,
            'secondSearchExpress' : "TI="+res.fetchone()[1][4:8],
            'order' : 1
        }
            payloads.append(payload)
        finally:
                try:
                        payload = {
            'type' : ["1005"],
            'page' : 1,
            'cnt' : 20,
            'secondSearchExpress' : "TI="+res.fetchone()[1][9:12],
            'order' : 1
        }
                        payloads.append(payload)
                except:
                    continue
    return payloads

if __name__ == '__main__':
    payload_num = 0
    current_payload=payload_num
    payloads = request_payload_generate(5000,payload_num)
    last_lines=0
    new_lines=0
    first_lines=0
    #manually update cookie needed
    updatedCookie =""
    for payload in payloads:
        print(f"\tCURRENT payload_num:{current_payload}")
        pageIndex=0
        while pageIndex<=50:
            pageIndex +=1
            print(f"CURRENTpageIndex:{pageIndex},out of 50")
            try:
                rawText = requestRawDocs(updatedCookie,payload)
            except:
                print("Requset Failed")
                pageIndex=1
            time.sleep(1)
            payload['page'] = pageIndex
            try:
                format_list = StrToDoc(rawText,0)
                DB_lines=write_to_DB_TEXT(format_list)
                if(first_lines==0):
                    first_lines=DB_lines
                new_lines=DB_lines
            except(TypeError):
                print("CurrentPayloadEnded,StartingNewOne...")
                break
            except:
                print(traceback.print_exc())
                time.sleep(1+random.randint(0,2))
                searchPages = (current_payload)*50 + pageIndex
                continue
            time.sleep(2+random.randint(0,2))
            if(pageIndex>2 and new_lines - last_lines <5 ):
                pageIndex += 10
            searchPages = (current_payload)*50 + pageIndex
            last_lines=new_lines
        current_payload += 1
        numberFilePos = "ScrapRecord.txt"
        with open(numberFilePos,"a") as file:
            try:
                file.write(f"RESTARTING FROM {payload_num} payload:{current_payload}, DBLines:{DB_lines}\n")
            except:
                print("FileWriteError")
                continue
    print(f"fistlines{first_lines} ; finishedlines{last_lines} ; increment{last_lines-first_lines}")

    


    