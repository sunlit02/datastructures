def perm(word, i, n):
    if i == n:
        print(''.join(word), end=' ')
    else:
        for j in range(i, n+1):
            word[i], word[j] = word[j], word[i]
            perm(word, i+1, n)
            word[i], word[j] = word[j], word[i]
          
word = ['L','A','N','G']
perm(word,0,3)
