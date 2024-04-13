import requests
import time
from bs4 import BeautifulSoup
from tkinter import *

def get_title(): # YYYY--MM-DD 제목
    title = time.strftime('%Y  -  %m  -  %d', time.localtime(time.time()))
    title += '일 오늘의 영어단어'
    return title

def get_data(before_data): # 영어 단어 가져오기
    tmp = list(before_data)
    for i in range(len(tmp)-1):
        if tmp[i].encode().isalpha() and tmp[i-1] == ' ':
            tmp[i-1] = '<p data-ke-size="size16">'
        if tmp[i].encode().isalpha() and not tmp[i+1].encode().isalpha():
            st = tmp[i]
            st += '&nbsp;  -&nbsp;  '
            tmp[i] = st
    After_data = ''.join(tmp)
    return After_data

def RUN():
    def Upload():
        url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%8B%A8%EC%96%B4&oquery=%EC%98%A4%EB%8A%98%EC%9D%98+%EC%98%81%EC%96%B4%EB%8B%A8%EC%96%B4&tqi=hecBksprvxsssj%2FGJxGssssstgC-317616'
        response = requests.get(url)
        if response.status_code == 200: 
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            data = soup.select_one('#_languageStudy > div > div.dicstudy_area > div.dicstudy_cont > div > div > ul').get_text().replace('발음듣기','')
            posting(get_data(data),get_title(),AT_insert.get(), BN_insert.get(), CT_insert.get())
        else : 
            print(response.status_code)

    def posting(content, title, access_token, blogName, category):
        tistory_url = 'https://www.tistory.com/apis/post/write?'
        parameters = {
            'access_token' : access_token,
            'output' : 'txt',
            'blogName' : blogName,
            'title' : title,
            'content' : content,
            'visibility' : '0',
            'category' : category,
        }
        result = requests.post(tistory_url, params=parameters)
        result = BeautifulSoup(result.text)
        print(result.prettify())

    root = Tk()
    root.title("Today's word")
    root.geometry('360x100')
    root.resizable(False,False)
    # Access Token 
    AT_Label = Label(root, text = 'Access Token', width = 13)
    AT_Label.grid(row = 0, column = 0)
    AT_insert = Entry(root, width = 35)
    AT_insert.grid(row = 0, column = 1)

    # Blog Name
    BN_Label = Label(root, text ='Blog Name', width = 13)
    BN_Label.grid(row = 2, column = 0)
    BN_insert = Entry(root, width = 35)
    BN_insert.grid(row = 2, column = 1)

    # category
    CT_Label = Label(root, text = 'Category', width = 13)
    CT_Label.grid(row = 4, column = 0)
    CT_insert = Entry(root, width = 35)
    CT_insert.grid(row = 4, column = 1)

    Run_Btn = Button(root, text = 'Run', command = Upload)
    Run_Btn.grid(row = 6, column = 1, sticky = N+W+E+S)

    root.mainloop()
    
RUN()
출처: https://khj1999.tistory.com/84 [프로그래밍 공부:티스토리]
