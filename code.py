import yaml

# Read the data of the format .yaml type
#f=open(path,'r')
#print(f.read())

# Find data type of the file
print(type(path))

# In which city, and at which venue the match was played and where was it played ?
with open(path,"r") as f:
    data=yaml.load(f)
city=data['info']['city']
print(city)

venue=data['info']['venue']
print("the match was played at Venue " + venue)

# Which are all the teams that played in the tournament ? How many teams participated in total?
teams=data['info']['teams']
print(teams)

# Which team won the toss and what was the decision of toss winner ?
winner=data['info']['toss']['winner']
decision=data['info']['toss']['decision']
print("The winner of toss is " + winner)
print("The decision of toss winner is " + decision)

# Find the first bowler and first batsman who played the first ball of the first inning

first_bowler=data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
print("The first bowler of first innings is " + first_bowler)
first_batsman=data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print("The first batsman of the first innings is " + first_batsman)

# How many deliveries were delivered in first inning ?
deliveries=len(data['innings'][0]['1st innings']['deliveries'])
print("no. of deliveries delivered in 1st innings " + ' '+str(deliveries))

# How many deliveries were delivered in second inning ?
deliveries_2=len(data['innings'][1]['2nd innings']['deliveries'])
print("no. of deliveries delivered in 2nd innings " + ' ' +str(deliveries_2))

# Which team won and how ?
by=data['info']['outcome']['by']['runs']
winner=data['info']['outcome']['winner']
print("The team that won tournament was " + winner + ' by ' + str(by) + 'runs')
