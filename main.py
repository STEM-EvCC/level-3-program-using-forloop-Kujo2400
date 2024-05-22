mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]


totalMis = 0

for mission in mission_names:
    totalMis += 1

print('Total number of space missions:',totalMis)

print('\n')

totalSuc = 0

for success in mission_success:
    if success:
        totalSuc += 1

print('Total successful space missions:',totalSuc)

successPerc = (totalSuc / totalMis) * 100

print('\n')

print('Total success rate of space missions: {:.2f}%'. format(successPerc))

print('\n')

print('Missions launched before the year 2000: ')
for name, year in zip(mission_names, mission_years):
    if year < 2000:
        print(name)