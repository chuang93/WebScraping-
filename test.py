from lxml import html
import requests

page =requests.get('http://basketball.fantasysports.yahoo.com/nba/buzzindex')

tree=html.fromstring(page.content)

trendingPlayers = tree.xpath('//a[@class="Nowrap"]/text()')

playerTeam = tree.xpath('//span[@class="Fz-xxs"]/text()')

netTrades= tree.xpath('//td[@class="Alt Last Ta-end Selected"]/text()')


i=0;

while i<len(trendingPlayers):
	print repr(i+1) + ". " + trendingPlayers[i] + " " + playerTeam[i]
	i+=1;





print 'Net Trades: ', netTrades


