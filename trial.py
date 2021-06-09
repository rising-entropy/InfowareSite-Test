import requests
import json
import re

file1 = open("aboutUs.txt","r") 

yoBoys = file1.read()

websiteName = re.findall(r"\<span class\=\"link\-without\-visited\-state\" dir\=\"ltr\"\>.*?\<\/span\>", yoBoys, re.MULTILINE | re.DOTALL)[0]
websiteName = websiteName.split(">")[1].strip()
websiteName = websiteName.split("<")[0].strip()





print(websiteName)

"""
<span class="link-without-visited-state" dir="ltr">
              http://www.onanimationstudios.com
            </span>
"""