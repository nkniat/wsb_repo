path1 = 'C://Users//kamil//Desktop//sample.xml'
mode1 = 'r'
with open (path1, mode1) as sample:
    content = sample.readlines()

#print(content)
version_update = False
for i in content:
    if 'xml version="' in i:
        version = i[15:18]
        if float(i[15:18]) < 2:
            version_update = True

if version_update:
    for i in range (len(content)):
        content[i] = content[i].replace('version="1.0"', 'version="3.1"')
        content[i] = content[i].replace('>2000-', '>2020-')
        content[i] = content[i].replace('>2001-', '>2021-')

    path2 = 'C://Users//kamil//Desktop//sample_updated.xml'
    mode2 = 'a'

    with open (path2, mode2) as sample_updated:
        for i in content:
            sample_updated.write(i)
else:
    print(f'Version {version}. No changes required ')
