import numpy as np
from numpy.random import random_sample
import matplotlib.pyplot as plt

def weighted_values(values, probabilities, total_odds):
    bins = np.add.accumulate(probabilities)
    return values[np.digitize(random_sample(total_odds), bins)]


human 	= {'life_span':80, 'odds':0.001}
bird	= {'life_span':5,  'odds':0.003}
cat 	= {'life_span':15, 'odds':0.004}
dog 	= {'life_span':15, 'odds':0.001}
bug 	= {'life_span':1,  'odds':0.994}
tortoise= {'life_span':250, 'odds':0.001}
species = {'dog':dog, 'human':human, 'cat':cat, 'bug':bug, 'bird':bird, 'tortoise':tortoise}









N = 100 # trial number
T = 1000 # years of trial



values = species.keys()
probabilities 	= np.zeros(len(species))
total_odds = 0
for counter, i in enumerate(species):
	probabilities[counter] = species[i]['odds']
	species[i]['count'] = 0
	total_odds += species[i]['odds']
data = np.zeros([len(species)+1,N])
for j in np.arange(0,N):
	t = T
	while t > 0.0:
		karmad_species = weighted_values(values, probabilities, total_odds)
		t -= species[karmad_species]['life_span']
		species[karmad_species]['count'] += 1
	for counter, i in enumerate(species):
		species[i]['years_lived'] = species[i]['life_span']*species[i]['count']
		data[counter,j] = species[i]['years_lived']
		species[i]['count'] = 0

data[-1] = data.sum(axis=0)
data = data.transpose()
data = data[data[:,5].argsort()]
data = data.transpose()

plt.close('all')
fig, ax = plt.subplots()
ax.set_xlim([0,N-1])
ax.set_ylim([0,T])
ax.legend(loc='best')
ax.set_xlabel('Trial')
ax.set_ylabel('Years lived')
ax.grid()

for i in np.arange(0,len(data)-1):
	ax.plot(np.arange(N), data[i,:], label=species.keys()[i]+'\nodds = %s\nage = %s'%(species[species.keys()[i]]['odds'],species[species.keys()[i]]['life_span']))

plt.legend(loc='best')
plt.show()

