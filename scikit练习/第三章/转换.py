import codecs
txt_dir = r'mytree'
txt_dir_utf8 = r'mytree_utf8.txt'

with codecs.open(txt_dir, 'r') as f, codecs.open(txt_dir_utf8, 'w', encoding='utf-8') as wf:
    for line in f:
        lines = line.strip().split('\t')
        print(lines)
        if 'label' in lines[0]:
            newline = lines[0].replace('\n', '').replace(' ', '')
        else:
            newline = lines[0].replace('\n','').replace('SimSun-ExtB', 'Microsoft YaHei')
        wf.write(newline + '\t')
#
