from bs4 import BeautifulSoup
import requests
#
#
# AD = 'https://www.ycombinator.com/companies/charge-robotics/jobs/VFEVUkD-mechanical-engineer'
#
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# article_links = soup.find_all(name="span", class_="titleline")
# links = [link.select_one("a").get("href") for link in article_links]
#
# ad_index = links.index(AD)
# links.remove(links[ad_index])
#
# all_rows = soup.find_all(name="tr", class_="athing")
# article_texts = [row.get_text().strip("\n") for row in all_rows]
# article_texts.remove(article_texts[ad_index])
#
# article_scores = soup.find_all(name="span", class_="score")
# score_list = [int(score.get_text().strip(" points ")) for score in article_scores]
#
# max_vote_index = score_list.index(max(score_list))
#
# print(article_texts[max_vote_index])
# print(links[max_vote_index])
# print(score_list[max_vote_index])
#

response = requests.get()
