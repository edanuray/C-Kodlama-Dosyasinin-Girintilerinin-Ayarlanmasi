from kutuphane import ArrayStack

def reverse_file(filename):
  """Overwrite given file with its contents line-by-line reversed."""
  S = ArrayStack()
  original = open(filename,'r')       
  for line in original:
    S.push(line.rstrip('\n'))     # we will re-insert newlines when writing
  original.close()

  # now we overwrite with contents in LIFO order
  output = open(filename, 'w')    # reopening file overwrites original
  while not S.is_empty():
    output.write(S.pop() + '\n')  # re-insert newline characters
  output.close()

stack = ArrayStack()

with open('source.c','r+', encoding='utf-8') as file:
    for i in file:
        if i[0] == '#':
            reverse_file('source.c')
            break

with open('source.c','r+', encoding='utf-8') as file:
    for i in file:
        stack.push(i.rstrip('\n'))

data = ''
boslukSayisi = 0
bosluk = ''

for i in range(0,len(stack._data)):
    gecici = stack.pop()

    if gecici == '}':
        boslukSayisi = boslukSayisi - 1
        bosluk = '\t' * boslukSayisi
        
    data = data + bosluk + gecici + '\n'

    if gecici == '{':
        boslukSayisi = boslukSayisi + 1
        bosluk = '\t' * boslukSayisi
        
  

with open('target.c', 'w') as file:
    file.write(data)

reverse_file('source.c')   


 

      
 
