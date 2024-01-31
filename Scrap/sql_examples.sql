-- SQLite
-- CREATE UNIQUE INDEX NUMBER ON DOCUMENT(ID);

--SELECT DISTINCT datasourceshow , COUNT(datasourceshow) FROM DOCTEXT 
--GROUP BY datasourceshow 
--ORDER BY COUNT(datasourceshow) DESC ; 

--SELECT DISTINCT sourceOrganization , COUNT(sourceOrganization) FROM DOCTEXT 
--WHERE datasourceshow == "国务院"
--GROUP BY sourceOrganization
--ORDER BY COUNT(sourceOrganization) DESC

--SELECT DISTINCT sourceOrganization , COUNT(sourceOrganization) FROM DOCTEXT 
--WHERE datasourceshow == "教育部"
--GROUP BY sourceOrganization
--ORDER BY COUNT(sourceOrganization) DESC

--SELECT DISTINCT sourceOrganization , COUNT(sourceOrganization) FROM DOCTEXT 
--WHERE datasourceshow == "交通运输部" AND policyType == "政策文件"
--GROUP BY sourceOrganization
--ORDER BY COUNT(sourceOrganization) DESC

--SELECT  ID,sourceOrganization,title , content FROM DOCTEXT 
--WHERE datasourceshow == "交通运输部" AND policyType == "政策文件"
--GROUP BY sourceOrganization
--ORDER BY COUNT(sourceOrganization) DESC

--SELECT  COUNT(sourceOrganization) FROM DOCTEXT 
--WHERE datasourceshow == "交通运输部" AND policyType == "政策文件"

--SELECT  title,content FROM DOCTEXT 
--WHERE policyType == "政策文件"
