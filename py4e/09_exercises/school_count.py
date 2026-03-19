fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    if line.startswith('From '):
        email_address = line.split()[1]
        domains = email_address.split('@')[1]
        counts[domains] = counts.get(domains, 0) + 1
            
print(counts)
