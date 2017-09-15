s = '''It was the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was ...'''
newS = s.replace('.,', ' ').replace(',.',' ').replace(';,',' ').replace('\n',' ').replace('was','is').lower().strip()
listS = newS.split(' ')
print(newS.count('it was'))
print(newS)
print(listS)