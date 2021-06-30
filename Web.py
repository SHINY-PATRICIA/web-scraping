omputers, listed 1-100 with each 1, 2, 3, 4, etc. item listed by '' and the each characteristic of the computer listed as '' (it's storage, max power, etc).

Here is my code:

# read the data from a URL
url = requests.get("https://www.top500.org/list/2018/06/")
url.status_code
url.content


# parse the URL using Beauriful Soup
soup = BeautifulSoup(url.content, 'html.parser')

filename = "computerRank10.csv"
f = open(filename,"w")

headers = "Rank, Site, System, Cores, RMax, RPeak, Power\n"
f.write(headers)

for record in soup.findAll('tr'):
# start building the record with an empty string
  tbltxt = ""
  tbltxt = tbltxt + data.text + ";"
  tbltxt = tbltxt.replace('\n', ' ')
  tbltxt = tbltxt.replace(',', '')
#    f.write(tbltxt[0:-1] + '\n')
f.write(tbltxt + '\n')

f.close()
