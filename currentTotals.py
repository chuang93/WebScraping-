from lxml import html
import requests



def findMatchupURL(week,playerOne,playerTwo):
	matchupURL='https://basketball.fantasysports.yahoo.com/nba/78003/matchup?week='+str(week)+'&mid1='+ str(playerOne)+'&mid2='+str(playerTwo)

	return matchupURL


def performLogin():
	payload = {
	"username": "<USER NAME>", 
	"password": "<PASSWORD>", 
	"csrfmiddlewaretoken": "<CSRF_TOKEN>"
			}

				
def getMatchupTotals(matchupURL):

	page=requests.get(matchupURL)

	tree=html.fromstring(page.content)

	matchupResults = tree.xpath('//td[@class="contest"]/text()')

	return matchupResults



def main():

	myMatchupURL=findMatchupURL(1,4,10)

	print myMatchupURL

	matchupResults= getMatchupTotals(myMatchupURL)

	print matchupResults

main()