print('-----please enter words only in lower case-----')
list = []
n = int(input('Please provide number of words:  '))


for i in range(n):
    wordinput = str(input('Enter the word:  '))
    word = wordinput
    list.append(word)

def countingthe(words):
    from collections import Counter
    lst = [list[j] for j in range(n)]
    count = Counter(lst)

    print(len(count))
    print(*count.values())

Ans = countingthe(list)
