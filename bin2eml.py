import os
import subprocess
import csv

f1 = open('Final_Data.csv', 'r')
f2 = open('data4.csv', 'w')
reader = csv.reader(f1)
writer = csv.writer(f2)
reader = list(reader)[300:]
list1 = sorted(os.listdir('bin/4'))
for i in range(0, len(list1)):
    print(list1[i], list(reader)[i][1])
    result = subprocess.check_output(
        "tools/pm3_amii_bin2eml.pl 'bin/4/" + list1[i] + "' > 'eml/4/" + reader[i][1] + ".eml'", shell=True,
        stderr=subprocess.STDOUT)
    print(result)
    print('result : hf mfu eload -f ' + list(reader)[i][1] + '.eml', result.splitlines()[-1].decode('utf - 8'))
    writer.writerow([list(reader)[i][0], list(reader)[i][1], 'hf mfu eload -f ' + list(reader)[i][1] + '.eml',
                     result.splitlines()[-1].decode('utf - 8')])

f2.close()
