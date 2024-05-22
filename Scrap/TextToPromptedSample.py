from pathlib import Path
import sqlite3
import json
import random
#this code saves list of TEXT entry to TEXT DB

def generate_summary(input_text,input_title,randomTemplate,template_text,template_title,contrastive_title):
    prompt_template = ["现在有一段文本，请根据文本特征并总结文本的信息。对比以下例子中正确的标题和错误的标题的例子，给这段文本总结一个正确的标题",
                       "请依据文本的内容特征，归纳其信息作为依据，对比以下例子中正确的标题和错误的标题的例子，为文本拟定一个正确的标题。",
                       "根据文本的特点，总结其信息作为依据，对比以下例子中正确的标题和错误的标题的例子，给出一个正确的标题。",
                       "现有一段文本，要求依据其特征总结信息作为依据，对比以下例子中正确的标题和错误的标题的例子，为其命名一个正确的标题。",
                       "根据文本的特征，归纳信息作为依据，对比以下例子中正确的标题和错误的标题的例子，给出一个正确的标题。",
                       "要求根据文本的特性，总结其信息作为依据，对比以下例子中正确的标题和错误的标题的例子，为其起一个正确的标题。",
                       "根据文本内容的特征，归纳其信息作为依据，对比以下例子中正确的标题和错误的标题的例子，为其命名一个正确的标题。",
                       "依据文本的特征，归纳其信息作为依据，对比以下例子中正确的标题和错误的标题的例子，拟定一个正确的标题。",
                       "要求：根据文本的特点总结信息作为依据，对比以下例子中正确的标题和错误的标题的例子，为其命名一个正确的标题。"]
    exampleTemplate = "例：" + template_text + "\n" + "上述例子文本正确的标题可以是：“" + template_title+ "”\n"
    exampleTemplate = exampleTemplate +  "\n" + "上述例子文本的错误的标题是：“" + contrastive_title + "”\n"
    prompt = prompt_template[randomTemplate] +  exampleTemplate + "现在给输入文本命名一个正确的标题"
    return {'instruction':prompt,'input':input_text,'target':input_title}


    
def generate_classfication(input_text,input_tag,randomTemplate,template_text,template_tag,tag_base):
    prompt_template = ["现在有一段文本，请根据文本特征，判断文本是由以下哪个机关发布的。其中可能发布的单位有这些：",
                       "现在有一份文本，要求根据其特征来判断其发布机构，可能的发布单位包括以下选项。",
                       "要求根据文本的特点确定其发布机构，可供选择的发布单位列举如下。",
                       "现有一段文字，需要根据其特征来判别发布机构，可能的发布单位包含以下几个。",
                       "现有一篇文本，要求根据其特征来辨别出发布机构，可能的发布单位有以下列举。",
                       "现在有一段文本，需要通过文本特征来判断其发布机构，可供选择的单位包括以下内容。",
                       "要求根据文本特征确定其发布机构，可能的发布单位列举如下。",
                       "现有一段文本，需要根据其特点来确定发布机构，可能的发布单位包括以下选项。",
                       "要求根据文本的特征来判断其发布机构，可供选择的发布单位列举如下。"]
    tag_options = ""
    for item in tag_base:
        tag_options = tag_options + f"“{item}”,"

    exampleTemplate = "例：" + template_text + "\n" + "上述例子文本正确的标签是：“" + template_tag + "”\n"
    exampleTemplate = exampleTemplate +  "\n" + "上述例子文本的错误的标签是：“" + tag_base[randomTemplate] + "”\n" #random
    prompt = prompt_template[randomTemplate] + tag_options +  exampleTemplate + "对比例子中正确的标签和错误的标签，给输入文本总结一个正确的标签"
    return {'instruction':prompt,'input':input_text,'target':input_tag}

def generate_multi_classfication(input_text,input_tag,input_tag_sec,randomTemplate,template_text,template_tag,template_tag_sec,tag_base,tag_base_sec,template_base_sec,ref_base):
    prompt_template = ["现在有一段文本，请根据文本特征，判断文本是由以下哪个机构下属的哪个单位发布的。其中可能且仅可能的发布的单位有这些：",
                       "现在有一份文本，要求根据其特征来判断其发布机构以及其下属机构，可能且仅可能的发布单位包括以下选项。",
                       "要求根据文本的特点确定其发布机构以及其下属机构，所有可供选择的发布单位列举如下。",
                       "现有一段文字，需要根据其特征来判别发布机构以及其下属机构，可能且仅可能的发布单位包含以下几个。",
                       "现有一篇文本，要求根据其特征来辨别出发布机构以及其下属机构，可能且仅可能的发布单位有以下列举。",
                       "现在有一段文本，需要通过文本特征来判断其发布机构以及其下属机构，所有可供选择的单位包括以下内容。",
                       "要求根据文本特征确定其发布机构以及其下属机构，可能且仅可能的发布单位列举如下。",
                       "现有一段文本，需要根据其特点来确定发布机构以及其下属机构，可能且仅可能的发布单位包括以下选项。",
                       "要求根据文本的特征来判断其发布机构以及其下属机构，所有可供选择的发布单位列举如下。"]
    tag_options = ""
    for item in tag_base:
        tag_options = tag_options + f"“{item}”,"
    tag_options_sec = ""
    randtagbase = tag_base_sec + ref_base
    random.shuffle(randtagbase)
    for item in randtagbase:
        tag_options_sec = tag_options_sec + f"“{item}”,"

    randRefbase=[]
    if randomTemplate%2 == 1:
        randRefbase = template_base_sec + ref_base
    else:
        randRefbase = template_base_sec + tag_base_sec
    random.shuffle(randRefbase)

    tamplate_tag_options_sec = ""
    for item in randRefbase:
        tamplate_tag_options_sec = tamplate_tag_options_sec + f"“{item}”,"

    tag_base.remove(template_tag)
    template_base_sec.remove(template_tag_sec)

    exampleTemplate = "例：" + template_text + "；该文本可能的发布单位为" + tag_options + "；可能的下属单位有且仅有：" + tamplate_tag_options_sec + "；\n" + "上述例子文本正确的标签是：“" + template_tag + "”，下属单位是“" + template_tag_sec + "”\n"
    exampleTemplate = exampleTemplate +  "\n" + "上述例子文本的错误的标签是：“" + random.choice(tag_base) +"”和下属单位“"+ random.choice(template_base_sec) + "”\n" #random
    prompt = prompt_template[randomTemplate] + tag_options + "所有可能的下属标签是"+ tag_options_sec +  exampleTemplate + "对比例子中正确的标签和错误的标签，给输入文本总结一个正确的标签和下属标签"
    targets= input_tag + "-" + input_tag_sec
    
    tag_base.append(template_tag)
    template_base_sec.append(template_tag_sec)

    return {'instruction':prompt,'input':input_text,'target':targets}



def generate_nextsentence(input_text,input_next,randomTemplate,template_text,template_next,contrastive_next):
    prompt_template = ["现在有一段文本，请根据文本特征和叙述方式。对比以下例子中正确的续写和错误的续写，给这段文本续写下一段内容",
                       "现在有一段文本，要求基于文本的特征和叙述方式，对比下面正确和错误的续写的特点，给出下一段的内容。",
                       "现在有一份文本，需要根据文本的特点和叙述方式，对比以下正确和错误的续写，补充下一段的内容。",
                       "根据文本的特征和叙述方式，对比以下正确和错误的续写，给出下一段的内容。",
                       "请根据文本的特点和叙述方式，对比以下正确和错误的续写，为文本撰写下一段内容。",
                       "现有一段文本，要求基于文本的特点和叙述方式，对比下面正确和错误的续写，给出下一段的内容。",
                       "要求根据文本的特征和叙述方式，对比下列正确和错误的续写，为文本续写下一段内容。",
                       "现有一份文本，需要根据文本的特征和叙述方式，对比以下正确和错误的续写，补充下一段的内容。",
                       "根据文本的特征和叙述方式，对比下面正确和错误的续写，为文本补充下一段内容。"]
    exampleTemplate = "例：" + template_text + "\n" + "上述例子文本正确的续写可以是：“" + template_next + "”\n"
    exampleTemplate = exampleTemplate +  "\n" + "上述例子文本的错误的续写是：“" + contrastive_next + "”\n"
    prompt = prompt_template[randomTemplate] +  exampleTemplate + "现在给出文本下一段的一个正确的续写"
    return {'instruction':prompt,'input':input_text,'target':input_next}

#this code inputs raw text (str) , outputs a list of document entry
def TxtToSentence(taskratioC,taskratioS):
    SQLCommand= """
    SELECT  * FROM DOCTEXT WHERE publishYear = ?  
    """
    dbconn = sqlite3.connect("document.db")
    cursor = dbconn.cursor()
    refcursor = dbconn.cursor()

    tag1base = cursor.execute(
        '''
            SELECT DISTINCT  datasourceshow FROM DOCTEXT 
        '''
    ).fetchall()
    tag1list = []
    for tag in tag1base:
        if len(tag[0])<8:
            tag1list.append(tag[0]) 
    yearNums = cursor.execute(
        '''
            SELECT DISTINCT  publishYear FROM DOCTEXT 
        '''
    ).fetchall()
    yearlist = [2013,2014,2015,2016,2017,2018,2019,2020] #train
    #yearlist_template = [2005,2006,2007,2008,2009,2010,2011,2012] #template
    #yearlist = [2021,2022,2023] #test
    cleanList = ["打印本页","电子邮件","附件","文件下载","邮箱","相关稿件","原文下载","联系人","联系方式","电话","免去","相关政策解读","相关解读",".pdf","此件公开发布","打印","&#xa0;","&ensp;"]
    
    
    
    textsentencedict = []
    for year in yearNums:
        if(year[0] not in yearlist):
            continue
        #print(year[0])
        query = (year[0],)
        cursor.execute(SQLCommand,query)
        query2 = (year[0]-8,)
        refbase = refcursor.execute(SQLCommand,query2).fetchall()
        i=0
        for row in cursor:
            text = row[9]
            if len(text)<20:
                continue
            title = row[6]
            tag1 = row[4]
            #tag2 = row[5]
            randRef =random.choice(refbase)
            
                    
            reftext = randRef[9]
            reftitle = randRef[6]
            reftag1 = randRef[4]
            reftag2 = randRef[5]
            randRef2 =random.choice(refbase)
            
            reftitle2 = randRef2[6]
            reftext2 = randRef2[9]
            for elem in cleanList:
                cleanedTemp = text.split(elem)
                text = ''.join(cleanedTemp)
                cleanedRefTemp = reftext.split(elem)
                reftext = ''.join(cleanedRefTemp)
            
            inst = None
            templateNum=random.randint(0,8)
            maxTextlength = min(int(len(text)/2),300)
            maxTemplateLength  = min(int(len(reftext)/2),300)
            maxRefLength  = min(int(len(reftext2)/2),300)
            input_text = text[:maxTextlength]
            next_text = text[maxTextlength:]
            template_in = reftext[:maxTemplateLength]
            template_next = reftext[maxTemplateLength:]
            contrastive_next = reftext2[maxRefLength:]
            if i%10 < taskratioC*10:
                reflist = tag1list
                if tag1 not in reflist:
                    reflist.append(tag1)
                inst=generate_classfication(input_text,tag1,templateNum,template_in,reftag1,reflist)
            elif i%10 > 10 - taskratioS*10:
                inst=generate_summary(input_text,title,templateNum,template_in,reftitle,reftitle2)
            else:
                inst=generate_nextsentence(input_text,next_text,templateNum,template_in,template_next,contrastive_next)

            textsentencedict.append(inst)
            i+=1
            
            #    string += json.dumps(elem,ensure_ascii=False,indent=1)+","
            #with open(f"./data/TrainTest.json",'a',encoding='utf-8') as f:
            #    f.write(string)
    print(len(textsentencedict))
    #generaltrain300.json : filename
    with open(f"./data/generaltrain300.json",'a',encoding='utf-8') as f:
        json.dump(textsentencedict,f,ensure_ascii=False,indent=1)



        
    cursor.close()
    return 0

if __name__ == '__main__':

    #filename = "Train.json"
    taskratioC=0.4
    taskratioS=0.4
    Formatted_File = TxtToSentence(taskratioC,taskratioS)
