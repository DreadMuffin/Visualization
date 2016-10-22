import csv
import numpy as np


f = open("catanstats.csv").read()
t = open('temp.csv','w')
t.write("settle1,rolls1,settle2,rolls2\n")


def settle_sort(s1,s2):
    rolls1 = [abs(7 - int(n)) for n in s1[:3]]
    rolls2 = [abs(7 - int(n)) for n in s2[:3]]
    type1 = s1[3:]
    type2 = s2[3:]
    settle1 = []
    settle2 = []
    for r in type1:
        if len(r) > 1:
            settle1.append('H')
        else:
            settle1.append(r)
    for r in type2:
        if len(r) > 1:
            settle2.append('H')
        else:
            settle2.append(r)
    so1 = [i[0] for i in sorted(enumerate(settle1), key=lambda x:x[1])]
    so2 = [i[0] for i in sorted(enumerate(settle2), key=lambda x:x[1])]
    printstring = ""
    for n in np.array(settle1)[so1]:
        printstring += str(n)
    printstring += ","
    for n in np.array(rolls1)[so1]:
        printstring += str(n)
    printstring += ","
    for n in np.array(settle2)[so2]:
        printstring += str(n)
    printstring += ","
    for n in np.array(rolls2)[so2]:
        printstring += str(n)
    printstring += "\n"
    t.write(printstring)
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
