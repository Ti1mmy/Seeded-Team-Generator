import random
print('Seeded Duo Generator')
print('--------------------')
seed = input('Enter seed: ')
print('--------------------')
print('Paste list of names, separated by newlines (\n). You can do this easily in a word processor.')
print('Once complete, press enter twice.')
people = []
while True:
    individual = input()
    if individual == "":
        break
    people.append(individual)
teams = []
i = 0
random.seed(seed)
while len(people):
    team = random.sample(people, 2)
    teams.append(team)
    for person in team:
        people.remove(person)
    i += 1
print(f'Teams are as follows for seed "{seed}":')
print()
k = 1
for duo in teams:
    print(f'Team {k}:')
    print(f'{duo[0]} & {duo[1]}')
    print()
    k += 1
