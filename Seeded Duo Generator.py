import random
print('Seeded Duo Generator')
print('------------------------------------------------------------------------')
print('INFO: GENERATES SEEDED DUOS/GROUPS FROM LIST OF NAMES')
print('note: will create .txt file inside parent directory of python file')
print('------------------------------------------------------------------------')
seed = input('Enter seed: ')
team_size = int(input('Team size: '))
print()
print('------------------------------------------------------------------------')
print('Input player names. Once complete, leave next input empty (press enter).')
print('------------------------------------------------------------------------')
print()
people = []
number = 1
while True:
    individual = input(f'Player {number}: ')
    if not individual:
        break
    people.append(individual)
    number += 1
if len(people) < 2:
    print('Error: More players needed')
elif not len(people) // team_size:
    print('Error: Not enough players to evenly distribute: try again.')
else:
    teams = []
    i = 0
    random.seed(seed)
    while len(people):
        team = random.sample(people, team_size)
        teams.append(team)
        for person in team:
            people.remove(person)
        i += 1
    with open('Seeded Teams.txt', 'a', encoding='utf-8') as output:
        output.write(f'Seeded Duo Generator\n')
        output.write('------------------------------------------------------------------------\n')
        output.write(f'Seed: {seed}\n')
        output.write(f'Team Size: {team_size}\n')
        output.write('------------------------------------------------------------------------\n')
        output.write('\nTeams:\n')
        k = 1
        for group in teams:
            output.write(f'\nTeam {k}:\n')
            for member in group:
                output.write(f'     - {member}\n')
            k += 1
