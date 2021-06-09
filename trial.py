import requests
import json
import re

yoBoys = """$type":"com.linkedin.voyager.common.TextViewModel"},"url":"http://animationireland.com",  """

matpat = ""

websiteName = re.findall(r"\$type\"\:\"com\.linkedin\.voyager\.common\.TextViewModel\"\}\,\"url\"\:\".*\"\,", yoBoys)[0].strip()
websiteName = websiteName.split("\":\"")[2]
websiteName = websiteName.split("\",")[0]


print(websiteName)