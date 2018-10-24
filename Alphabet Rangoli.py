#&dru

#imports
import string

#fun
def print_rangoli(size):
    list = list(string.ascii_lowercase)

list1 = list(string.ascii_lowercase)


#input
N = int(input("-> "))
N -= 1 ##due to 0dex
print(list1[N::-1])


size = 1 + (4 * N)
#size = int(input("Size: -> "))

print((list1[N]).center(size, "-"))

for i in range(N+1):
    listvar = [(list1[N:i:-1])]
    listvar.append(list1[i:N+1])
    print(listvar)
