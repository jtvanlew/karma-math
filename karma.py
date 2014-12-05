import numpy as np
from numpy.random import random_sample
import matplotlib.pyplot as plt

def weighted_values(values, probabilities):
    bins = np.add.accumulate(probabilities)
    return values[np.digitize(random_sample(1), bins)]

N = 500 # trial number
t = 1000 # years of trial

bug_odds = 0.994    # odds of being born a bug
bugLifeSpan = 1 # life span of bugs in years

dog_odds = 0.003   # odds of being a dog
dogLifeSpan = 15 # life span of a dog in years

human_odds = 1-dog_odds-bug_odds  # odds of being born a human
humanLifeSpan = 80 # life span of a human in years


values = ['bug', 'dog', 'human']
probabilities = np.array([bug_odds, dog_odds, human_odds])



total = []
humans = []
bugs = []
dogs = []
for j in np.arange(0,N):
	T = t
	count0 = 0
	count1 = 0
	count2 = 0

	while T > 0.0:
		x = weighted_values(values, probabilities)
		if x == 'bug':
			T -= bugLifeSpan
			count0 += 1
		elif x == 'dog':
			T -= dogLifeSpan
			count1 += 1
		elif x == 'human':
			T -= humanLifeSpan
			count2 += 1

	bugs.append(count0)
	dogs.append(count1)
	humans.append(count2)

	total.append(count0+count1+count2)

data = zip(total, bugs, dogs, humans)
sorted_data = sorted(data, key=lambda x:x[0])
total = [row[0] for row in sorted_data]
bugs = [row[1] for row in sorted_data]
dogs = [row[2] for row in sorted_data]
humans = [row[3] for row in sorted_data]

plt.close('all')


# plt.figure(1)
# plt.title('total time units = %s, total trials = %s'%(t,N))
# plt.xlabel('trial')
# plt.ylabel('Lives lived in %s years'%(t))
# bottom = []
# for i in np.arange(N):
# 	bottom.append(humans[i] + dogs[i])
# plt.bar(np.arange(N), humans, color = 'c',label='Humans')
# plt.bar(np.arange(N), dogs, bottom=humans, color = 'r',label='Dogs')
# plt.bar(np.arange(N), bugs, bottom=bottom, color = 'k',label='Bugs')
# plt.legend(loc='best')




bugYears = [i*bugLifeSpan for i in bugs]
dogYears = [i*dogLifeSpan for i in dogs]
humanYears = [i*humanLifeSpan for i in humans]


for i in np.arange(N):
	dogYears[i] += humanYears[i]
	bugYears[i] += dogYears[i]


fig, ax = plt.subplots(1)
ax.plot(np.arange(N), humanYears, lw=2, label='Humans', color='blue')
ax.plot(np.arange(N), dogYears, lw=2, label='Dogs', color='red')
ax.plot(np.arange(N), bugYears, lw=2, label='Bugs', color='cyan')

ax.fill_between(np.arange(N), np.zeros(N), humanYears, facecolor='blue', alpha=0.5)
ax.fill_between(np.arange(N), humanYears, dogYears, facecolor='red', alpha=0.5)
ax.fill_between(np.arange(N), dogYears, bugYears, facecolor='cyan', alpha=0.5)
ax.set_ylim([0,N])
ax.set_ylim([0,t])
#ax.set_title('total time units = %s, total trials = %s'%(t,N))
ax.legend(loc='best')
ax.set_xlabel('Trial')
ax.set_ylabel('Years lived')
ax.grid()



plt.show()