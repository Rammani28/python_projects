from bs4 import BeautifulSoup
import requests
import json


def remove_text_inside_brackets(text, brackets="(){}"):
    count = [0] * (len(brackets) // 2) # count open/close brackets
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b: # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close # `+1`: open, `-1`: close
                if count[kind] < 0: # unbalanced bracket
                    count[kind] = 0  # keep it
                else:  # found bracket to remove
                    break
        else: # character is not a [balanced] bracket
            if not any(count): # outside brackets
                saved_chars.append(character)
    return "".join(saved_chars)


URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
script = soup.find("script", type="application/json")  # source: stack overflow
data = json.loads(script.string)

x = data['props']['pageProps']['data']['getArticleByFurl']['_layout'][3]['content']['images']
movie_list = []
description_list = []
for file in x:
    title = file['titleText']
    movie_list.append(title)
    description = remove_text_inside_brackets(file['description']).replace("[", "").replace("]", "").replace("Read Empire's review of ", "... ")
    description.replace(''.join(title.split()[1:]), "")
    description_list.append(description)

with open("movies.txt", mode="w") as file:
    for num in range(99, -1, -1):
        file.write(f"{movie_list[num]}\n")
        txt = description_list[num].replace('\n', '')
        file.write(f"{txt}\n\n")

print("success")
# row = (soup.find(name="div", class_="listicle-item"))
# text = row.get_text()
# print(text)

