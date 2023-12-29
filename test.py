import requests
from bs4 import BeautifulSoup

results = []
url = 'https://myanimelist.net/topanime.php?type=airing'
d = requests.get(url)
all_data = BeautifulSoup(d.text, 'html.parser')
hightiers_nt = all_data.find_all('span', class_ = 'lightLink top-anime-rank-text rank1') 
lowtiers_nt = all_data.find_all('span', class_ = 'lightLink top-anime-rank-text rank2')
names_nt = all_data.find_all('h3', class_ = 'fl-l fs14 fw-b anime_ranking_h3')
scores_nt = all_data.find_all('div', class_ = 'js-top-ranking-score-col di-ib al')

tiers = [i.text for i in hightiers_nt] + [i.text for i in lowtiers_nt]
names = [i.text for i in names_nt]
scores = [i.text for i in scores_nt]

for i in range(0, 50):
    instance = [tiers[i], names[i], scores[i]]
    results.append(instance)

print(results)