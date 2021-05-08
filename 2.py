dataKey = ['dumb','ways','the','best']
word = 'dumbways'

def check(dataKey, word):
    for i in dataKey:
        if i in word.lower():
            print(i + ' => true')
        else:
            print(i + ' => false')

check(dataKey, word)
