# Tasks
# Input
# Title, Start Date, End Date
# Output
# Title, Start Date, # Days
from datetime import datetime

try:
    schedules = []
    date_format = "%d-%b-%Y"
    with open("schedules.txt", "rt") as schedules_lines:
        for line in schedules_lines:
            splits = line.strip().split(",")
            if len(splits) != 3:
                continue
            course = splits[0]
            start_date = splits[1]
            end_date = splits[2]
            duration = datetime.strptime(end_date, date_format) - datetime.strptime(start_date, date_format)
            schedules.append((course, start_date, duration.days))
    print(schedules)
except Exception as ex:
    print(ex)
# Players
# Input
# Name, Date of Birth
# Output
# Name, Age [In descending order]
try:
    players = []
    date_format = "%d-%b-%Y"
    with open("players.txt", "rt") as players_lines:
        for line in players_lines:
            splits = line.strip().split(",")
            if len(splits) != 2:
                continue
            player_name = splits[0]
            date_of_birth = splits[1].strip()
            age = datetime.today() - datetime.strptime(date_of_birth, date_format)
            players.append((player_name, age.days//365))
    print(players)
except Exception as ex:
    print(ex)
