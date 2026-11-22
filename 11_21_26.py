a = 4157 
b = 8906
# output should be 7500

def odd_integers(a: int, b: int) -> int:
    return ((b+1)//2)**2-(a//2)**2

print(odd_integers(a,b))


def odd_integers(a: int, b:int) -> int:
    start = a if a%2 ==1 else a+1
    return sum(range(start, b+1, 2))

print(odd_integers(a,b))


'rosalind_ini5.txt'

file = open('rosalind_ini5.txt','r')


words = file.read().splitlines()[1::2]


new_file = open('rosalind_ini5evenlines.txt','w')

new_file.write('\n'.join(words))
new_file.close()
