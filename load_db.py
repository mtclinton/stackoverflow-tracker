from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3
from datetime import datetime
import time

conn = sqlite3.connect('database.db')


tag = input('enter stackoverflow tag: ')

pagenum = 1

url = f"https://stackoverflow.com/questions/tagged/{tag}?tab=votes&page={pagenum}"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

lastpage = 1
pages = soup.find_all('a', {"class": "s-pagination--item"})

for page in pages:
    try:
        pagination_page = int(page.text)
        if pagination_page > lastpage:
            lastpage = pagination_page
    except:
        pass
while pagenum <= lastpage:
    if pagenum == 1:
        pass

    else:
        # need to add error handling
        url = f"https://stackoverflow.com/questions/tagged/{tag}?tab=votes&page={pagenum}"
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

    for question in soup.find_all("div", {"class": "question-summary"}):
        try:
            votes = question.find('span', {'class': 'vote-count-post'}).text
            answer = str(question.find('div', {'class': 'status'}).text)
            answer=answer.replace(" ", "")
            answer=answer.replace("\n", "")
            answer=answer.replace("\r", "")
            answer=answer.replace("\t", "")
            answer=answer.replace('answer', '')
            answer=answer.replace("s", "")
            answer = int(answer)
            views = str(question.find('div', {'class': 'views'}).text)
            views=views.replace(" ", "")
            views=views.replace("\n", "")
            views=views.replace("\r", "")
            views=views.replace("\t", "")
            views=views.replace('view', '')
            views=views.replace("s", "")
            views=views.replace('k', '000')
            views = int(views)

            title = question.find('a', {'class': 'question-hyperlink'}).text
            link = question.find('a', {'class': 'question-hyperlink'})['href']
            subtitle = question.find('div', {'class': 'excerpt'}).text

            try:
                site_date = question.find('span', {'class': 'relativetime'})['title']
                date = int(datetime.fromisoformat(site_date[:-1]).timestamp())
            except:
                date = 0
            try:
                avatar = question.find('img', {'class': 'bar-sm'})['src']
            except:
                avatar = 'anon'
            user_container = question.find('div', {'class': 'user-details'})
            try:
                user = user_container.find('a')
                user_name = user.text
                user_link = user['href']
            except:
                user_name = 'anon'
                user_link = 'anon'

            data = (
            tag, votes, answer, views, title, link, subtitle, date, user_name, avatar, user_link, int(time.time()), 0,
            '', 0, 0)

            sql = ''' INSERT INTO stackoverflow(topic,votes,answers,views,title,link,subtitle,date,user,avatar,userlink,querydate,starred,notes,read,rank)
                                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()


        except Exception as e:
            print(str(e))
            # print(message)

    print('Finished page: ', str(pagenum))
    pagenum += 1
    time.sleep(10)

print('done')
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
