-- SQLite

--查询不同的datasourceshow标签
SELECT DISTINCT datasourceshow , COUNT(datasourceshow) FROM DOCTEXT 
GROUP BY datasourceshow 
ORDER BY COUNT(datasourceshow) DESC ; 

--查询不同的sourceOrganization标签，要求datasourceshow为“国务院”
SELECT DISTINCT sourceOrganization , COUNT(sourceOrganization) FROM DOCTEXT 
WHERE datasourceshow == "国务院"
GROUP BY sourceOrganization
ORDER BY COUNT(sourceOrganization) DESC

--查询一条数据，并限制了datasourceshow，policyType
SELECT  ID,sourceOrganization,title , content FROM DOCTEXT 
WHERE datasourceshow == "交通运输部" AND policyType == "政策文件"

--查询文本数据库总长
SELECT SUM(length(content)) FROM DOCTEXT ; 

--构成多标签分类数据集的复合查询
SELECT  * FROM DOCTEXT 
WHERE ( 
(datasourceshow = "国务院" AND(sourceOrganization = "国务院办公厅" OR  sourceOrganization ="交通运输部"  OR sourceOrganization = "财政部" 
OR sourceOrganization ="教育部" OR sourceOrganization = "工业和信息化部" OR sourceOrganization = "国家发展和改革委员会"
OR sourceOrganization = "农业农村部办公厅" OR sourceOrganization = "民政部" OR sourceOrganization = "税务总局"
OR sourceOrganization = "卫生健康委" OR sourceOrganization = "国家林业和草原局"OR sourceOrganization = "商务部" 
OR sourceOrganization = "自然资源部" OR sourceOrganization = "农业农村部" OR sourceOrganization = "文化和旅游部"))

OR (datasourceshow = "北京市人民政府" AND (sourceOrganization = "北京市人力资源和社会保障局" 
OR sourceOrganization = "北京市住房和城乡建设委员会" OR sourceOrganization = "北京市人民政府办公厅" OR sourceOrganization = "北京市教育委员会"
OR sourceOrganization = "北京市发展和改革委员会" OR sourceOrganization = "北京市民政局" OR sourceOrganization = "北京市财政局" OR sourceOrganization = "北京市商务局" ))

OR (datasourceshow = "黑龙江省人民政府" AND(sourceOrganization = "黑龙江省农业农村厅"
OR sourceOrganization = "黑龙江省应急管理厅" OR sourceOrganization = "黑龙江省文化和旅游厅" OR sourceOrganization = "黑龙江省政府办公厅"
OR sourceOrganization = "黑龙江省生态环境厅" OR sourceOrganization = "黑龙江省市场监督管理局" OR sourceOrganization = "黑龙江省物价局"
OR sourceOrganization = "黑龙江省煤炭生产安全管理局" OR sourceOrganization = "黑龙江省林业和草原局" OR sourceOrganization = "黑龙江省财政厅"
OR sourceOrganization = "黑龙江省住房和城乡建设厅" OR sourceOrganization = "黑龙江省水利厅" OR sourceOrganization = "黑龙江省人力资源和社会保障厅"
OR sourceOrganization =	"黑龙江省税务局" OR sourceOrganization = "黑龙江省卫生健康委员会" OR sourceOrganization = "黑龙江省教育厅" OR sourceOrganization = "黑龙江省机关事务管理局"))

OR (datasourceshow = "大连市人民政府" AND (sourceOrganization = "大连市交通运输局"

OR sourceOrganization = "大连市公安局" OR sourceOrganization = "大连市教育局" OR sourceOrganization = "大连市卫生健康委员会"
OR sourceOrganization = "大连市城市管理局" OR sourceOrganization = "大连市文化和旅游局" OR sourceOrganization = "大连市住房和城乡建设局"
OR sourceOrganization = "大连市工业和信息化局" OR sourceOrganization = "大连市民政局" OR sourceOrganization = "大连市自然资源局"
OR sourceOrganization = "大连市农业农村局" OR sourceOrganization = "大连市商务局" OR sourceOrganization = "大连市发展和改革委员会" ))

OR (datasourceshow = "杭州市人民政府" AND ( "市政府办公厅" 
OR sourceOrganization = "市经信局" OR sourceOrganization = "市发改委" 
OR sourceOrganization = "市建委" OR sourceOrganization = "市民政局"))

OR (datasourceshow = "广州市人民政府" AND (sourceOrganization ="广州市人民政府办公厅"
OR sourceOrganization = "广州市民政局" OR sourceOrganization = "广州市人力资源和社会保障局"
OR sourceOrganization = "广州市住房和城乡建设局" OR sourceOrganization = "广州市公安局" OR sourceOrganization = "广州市住房和城乡建设委员会"
OR sourceOrganization = "广州市发展和改革委员会" OR sourceOrganization = "广州市交通委员会"))

OR (datasourceshow = "河北省人民政府" AND (sourceOrganization = "河北省政府办公厅"
OR sourceOrganization = "河北省人民政府" OR sourceOrganization = "河北省发展改革委" 
OR sourceOrganization = "河北省住房和城乡建设厅"))

OR (datasourceshow = "云南省人民政府" AND (sourceOrganization = "云南省人民政府"
OR sourceOrganization =  "云南省老龄工作委员会办公室" OR sourceOrganization =  "云南省公安厅"
OR sourceOrganization =  "云南省农业农村厅" OR sourceOrganization =  "云南省发展和改革委员会"))
) 
