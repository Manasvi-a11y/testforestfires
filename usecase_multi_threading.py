# ... 

# https://blog.langchain.dev/tag/case-studies/

# https://www.langchain.com/customers

# https://langchain-ai.github.io/langgraph/tutorials/introduction/

# ...

import threading 
import requests
from bs4 import BeautifulSoup

urls=[
    'https://blog.langchain.dev/tag/case-studies/',
    'https://www.langchain.com/customers',
    'https://langchain-ai.github.io/langgraph/tutorials/introduction/'

]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'htmll.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
    threads=[]

    for url in urls:
        threads=threading.Thread(target=fetch_content,args=(url,))
        threads.append(thread)
        thread.start()

        for thread in threads:
            thread.join()

            print("All web pages fetched")
