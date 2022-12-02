import requests
from bs4 import BeautifulSoup
import re

b_url = 'https://www.acmicpc.net/user/백준유저ID'

response = requests.get(b_url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.select_one('div.problem-list')
    p = re.compile(r'[0-9]+')

    b_list = []
    for i in div.contents:
        if i != " ":
            i = i.get('href')
            match_obj = p.search(i)
            b_num = match_obj.group()
            b_list.append(b_num)
    print(len(sorted(set(b_list))))
else:
    print(response.status_code)

git_url = "https://api.github.com/repos/깃ID/레포네임/git/trees/main?recursive=1"
p1 = re.compile(r'(?=.*백준)(?=.*\.py).*')
p2 = re.compile(r'(\d+)\.')
g_list = []
for i in requests.get(git_url).json()["tree"]:
    i = i['path']
    match_obj = p1.search(i)
    if match_obj is not None:
        g_w = match_obj.group()
        match_obj2 = p2.search(g_w)
        g_num = match_obj2.group()
        g_list.append(g_num[:-1])
print(len(sorted(set(g_list))))


print(" ".join(set(b_list)-set(g_list)))
