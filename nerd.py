import requests
url="https://hs-consumer-api.espncricinfo.com/v1/edition/details?lang=en&edition=in&navigation=true&trendingMatches=true&keySeriesItems=true&sponsoredItems=true"
res=requests.get(url)
result=res.json()
result1=result["trendingMatches"]
result2=result1["matches"]
length=len(result1["matches"])
for i in range(0,length):
  result3=result2[i]
  result8=result3["stage"]
  result4=result3["teams"]
  if(result8=="RUNNING"):
    print("Match Name-->",result3["slug"])
    result5a=result4[0]
    result5b=result4[1]
    result6a=result5a["score"]
    result6b=result5b["score"]
    print("Score for team1",result6a)
    print("Score for team2",result6b)
    print("--------------xXXXXXXXXXXXXXXXXXXXXXXXXXXXx---------------")
  else:
    print("Match Name-->",result3["slug"])
    print(" MATCH YET  TO BEGIN ")
    print("-----------xXXXXXXXXXXXXXXXXXXXXXXXXXx---------------")
