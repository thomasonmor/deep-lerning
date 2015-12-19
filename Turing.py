#alfavit = None, '0', '1'
#sost = 'stop', 1, 2, 3
conf = [0,0,0,1,0,1,0,1,1]
lenta = ['B']*100 + conf + ['B']*100
pos = 100
state = 1
tabl = ((1, 1, 1, 1, 'r'),
        (0, 1, 0, 1,'r'),
        ('B', 1, 'B', 2, 'l'),
        (1, 2, 0, 2, 'l'),
        (0, 2, 1, 3,'l'),
        ('B', 2, 1, 'stop', ''),
        (0, 3, 0, 3,'l'),
        (1, 3, 1, 3,'l'),
        ('B', 3, 'B', 'stop','r'))
def naidi_mne_stroku():
 for n in tabl:
  if n[0] == lenta[pos]:
   if n[1] == state:
         return n
while state != 'stop':
  n = naidi_mne_stroku()
  lenta[pos] = n[2]
  state = n[3]
  if n[4] == 'r':
         pos = pos + 1
  elif n[4] == 'l':
         pos = pos - 1
  else:
         pos = pos
print lenta
