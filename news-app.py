import requests	 
from win32com.client import Dispatch
import time

source=input("what new u want to search:")
main_url = f" https://newsapi.org/v2/everything?q={source}&from=2023-12-21&to=2023-12-21&sortBy=popularity&apiKey=b55757eb57cd4fec96c1cb9624e42f30"

# fetching data in json format
res = requests.get(main_url)
open_bbc_page = res.json()

# getting all articles in a string article
article = open_bbc_page["articles"]

# empty list which will 
# contain all trending news
results = []

for ar in article:
    results.append(ar["title"])
    
for i in range(len(results)):
     if (i<15):
        # printing all trending news
        print(i + 1, results[i])
        time.sleep(0.5)
        # speak = Dispatch("SAPI.Spvoice")
        # speak.Speak(results[i])


				 


