import csv


f = open("catanstats.csv").read()

def settle_sort(s1,s2):
    dices = sorted(s1[:3] + s2[:3])
    res = s1[3:] + s2[3:]
    fres = []
    for r in res:
        if len(r) > 1:
            fres.append('H')
        else:
            fres.append(r)
    return [dices] + [sorted(fres)]

def settle(csv):
  return csv[::2] + csv[1::2]

def player(csv):
  return [csv[2]] + settle_sort(settle(csv[15:21]), settle(csv[21:27]))

settlements = []

for i, line in enumerate(f.split("\r\n")[1:]):
  settlements.append(player(line.split(",")))

output = []

for line in settlements:
    output.append([line[0]] + ["".join(line[1])] +["".join(line[2])])

with open("settlements.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(["points","dices", "res"])
    writer.writerows(output)
