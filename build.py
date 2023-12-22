import os
import httpx
import re
import urllib.parse

def fetch_ci_time(filePath):
    entries = httpx.get("https://api.github.com/repos/tjxj/ml-weekly/commits?path=" + filePath + "&page=1&per_page=1")
    ciTime = entries.json()[0]["commit"]["committer"]["date"].split("T")[0]
    return ciTime

if __name__ == "__main__":
    readmefile = open('README.md', 'w')
    readmefile.write("# 机器学习周刊\n\n> 关注Python、机器学习、深度学习、大模型，欢迎订阅\n\n> Fork From https://github.com/tw93/weekly\n\n")

    for root, dirs, filenames in os.walk('./src/pages/posts'):
        # Ensure that the file has a number to sort by, defaulting to 0 if not
        filenames = sorted(filenames, key=lambda x: float(re.findall("(\d+)", x)[0]) if re.findall("(\d+)", x) else 0, reverse=True)

    for name in filenames:
        if name.endswith('.md'):
            filepath = urllib.parse.quote(name)
            oldTitle = name.split('.md')[0]
            url = 'https://weekly.zhanglearning.com/posts/' + oldTitle
            title = '第 ' + oldTitle.split('-')[0] + ' 期 - ' + oldTitle.split('-')[1]
            readmeMd = '* [{}]({})\n'.format(title, url)
            readmefile.write(readmeMd)

    readmefile.close()