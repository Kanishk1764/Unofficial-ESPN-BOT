api_url_telegram = "https://api.telegram.org/bot5017801497:AAETaPzUr2egHwYqa4dIIXYWDXk08t_q9n0/sendMessage?chat_id=@__groupid__&text="
group_id = "JUSTAPROJECT"
def Forkingnerd():
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
      message="result for team A:->",result6a,"result for team B:->",result6b
      sendmessage(str(message))
    else:
      print("Match Name-->",result3["slug"])
      print(" MATCH YET  TO BEGIN ")
      print("-----------xXXXXXXXXXXXXXXXXXXXXXXXXXx---------------")
      message="Match Name-->",result3["slug"],"MATCH YET TO BEGIN"
      sendmessage(str(message))
def sendmessage(message):
  final_telegram_url = api_url_telegram.replace("__groupid__",group_id)
  final_telegram_url = final_telegram_url + message
  response = requests.get(final_telegram_url)
  print(response)
Forkingnerd()
