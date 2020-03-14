import json
import os
from requests import get
from xml.dom.minidom import parse, parseString

def getArgonRelease():
    import requests

    res = requests.get('https://github.com/solstice23/argon-theme/releases.atom')
    res.encoding = 'utf-8'
    res = res.text
    dom = parseString(res)
    versions = dom.getElementsByTagName("entry")
    version = versions[0].getElementsByTagName('title')[0].childNodes[0].data
    print("latest:" , version)
    print(version)

    url = "https://github.com/solstice23/argon-theme/releases/download/" + version + "/argon.zip"
    print("url:" , url)
    
    if os.path.exists('./argon_releases') == False:
        os.makedirs('./argon_releases')
    
    # download
    filename = './argon_releases/argon-{}.zip'.format(version)
    if (os.path.exists(filename) == False):
        print("downloading...")
        res = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(res.content)
        print("downloaded")

if __name__ == "__main__":
    getArgonRelease()
