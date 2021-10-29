olom = 18
rez = 23
olomS = 11.34
rezS = 8.69
olomT = olomS * olom
rezT = rez * rezS
print(f'{olomT} g nehez az olom')
print(f'{rezT} g nehez az rez')
if rezT>olomT:
    print('Ezert a rez nehezebb')
else:
    print('Ezert az olom a nehezebb')