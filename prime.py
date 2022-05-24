# Prime number program by Ajeet Singh

def prime(n):
    for i in range(2,n+1):
        if(n % i == 0):
            break
    if (n == i):
        print(n,'is a Prime number')
    else:
        print(n,'is not a Prime number')

def main():
    n = int(input('Enter a number : '))
    prime(n)

if __name__ == '__main__':
    main()



