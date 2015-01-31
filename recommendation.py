# A dictionary of movie critics and their ratings of a small  set of movies

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Monish': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

# Going for Pearson because Euclidean distance method found less effective
from math import sqrt

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
 # Get the list of mutually rated items
	si={}
	for item in prefs[p1]:
 		if item in prefs[p2]: 
 			si[item]=1
 # Find the number of elements
	n=len(si)
 # if they are no ratings in common, return 0
	if n==0:
		return 0
 # Add up all the preferences
 	
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])
 # Sum up the squares
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
 # Sum up the products
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
 # Calculate Pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0: 
 		return 0
	r=num/den
	return r

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional parameters
def topMatches(prefs,person,n=5,similarity=sim_pearson):
	scores=[(similarity(prefs,person,other),other)
	for other in prefs if other!=person]
 # Sort the list so the highest scores appear at the top
	scores.sort( )
	scores.reverse( )
	return scores[0:n]

#Shows the similarity coefficient with other critics
print (topMatches(critics,'Monish',n=6))


# Gets recommendations for a person by using a weighted average  of every other user's rankings

def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
 # Not comparing me to myself
		if other==person: continue
		sim=similarity(prefs,person,other)
 # ignore scores of zero or lower so that only similarity parmeters are considered
		if sim<=0: continue
		for item in prefs[other]:
 # I will ask for recommendation for the movies i havent seen
			if item not in prefs[person] or prefs[person][item]==0:
 # Similarity * Score
				totals.setdefault(item,0)
				totals[item]+=prefs[other][item]*sim
 # Sum of similarities
				simSums.setdefault(item,0)
				simSums[item]+=sim
 # Create the normalized list
	rankings=[(total/simSums[item],item) for item,total in totals.items( )]
 # Return the sorted list and reverse it to get the movies in order of highest recommendation values
	rankings.sort( )
	rankings.reverse( )
	return rankings

#Enjoy your day with the recommended movies
print (getRecommendations(critics,'Monish'))

#Above code can be extended for any static input for example: movies, books, videos, games,etc along with their corresponding input ratings 
#And then enjoy with your recommended thrills!!

