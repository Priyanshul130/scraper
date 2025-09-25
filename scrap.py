import requests
from bs4 import BeautifulSoup
import  csv as c

def go(query):
    url = "https://html.duckduckgo.com/html/"
    params = {"q": query}


    response = requests.get(url, params=params, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116 Safari/537.36"
    })

    #print("response", response) 
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for link in soup.select("a.result__a"):  
        results.append(link.get("href"))

    return results
def bing(query):
    url = "https://www.bing.com/search"
    params = {"q": query}

    response = requests.get(url, params=params, headers={
        "User-Agent": "Mozilla/5.0"
    })

    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for link in soup.select("li.b_algo h2 a"):
        results.append(link.get("href"))
    return results

def csv(query, results):
    filename = f"{query.replace(' ', '_')}_results.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = c.writer(f)
        writer.writerow(["Query", "Link"])
        for r in results:
            writer.writerow([query, r])
    print(f"✅ Saved {len(results)} results to {filename}")

if __name__ == "__main__":
    query = input("Enter your search query: ")
    results = go(query)
    bing_res=bing(query)
    #print(bing_res)
    if results:
        csv(query, results)
    else:
        print("⚠️ No results found. Try a different query.")
