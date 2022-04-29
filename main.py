from collections import defaultdict

per_minute_counter = defaultdict(int)

with open('events.log', 'rt') as file:
    line = file.readline()
    while line:
        # Уберем лишние пробелы
        line = " ".join(line.split())
        if 'NOK' in line:
            line = line.split("]")

            date_parts = line[0].split(":")
            minute = date_parts[0] + ":" + date_parts[1] + "]"

            per_minute_counter[minute] += 1

        line = file.readline()

for date_time_minute, count in per_minute_counter.items():
    print(f'{date_time_minute} {count}')
