import requests
from bs4 import BeautifulSoup

URL = "https://old.reddit.com/r/surrealmemes/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="siteTable")

if results != None:
    try:
        with open("page.txt", "w") as file:
            res = results.prettify()
            print(res)
            file.write(res)
    except:
        print("Couldn't write to file")

    posts = results.findAll("div", class_ = lambda x: x and x.startswith("thing t3"))
    posts = results.select("div[class^=thing]")

    print(posts)

    urls = []

    # Get URL
    try:
        for x in posts:
            print(x.prettify())
            pos = x.prettify().find("data-url=")

            # Dispose of ads
            if pos != -1:
                temp = x[pos + 9:]
                url = temp.split("\"")[0]
                urls.append(url)
    except:
        print("L")

    print(urls)
else:
    print("Please wait nerd")
