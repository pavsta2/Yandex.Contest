import math


def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(int(i))
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(n))
   return primfac


def max_fac(a,b):
    gsd = math.gcd(a,b)
    facs_a = primfacs(a //gsd)
    facs_b = primfacs(b // gsd)
    facs = set(facs_a + facs_b)

    return gsd * max(facs)

def main():
    tasks = []
    with open('input.txt') as f:
        num = int(f.readline().rstrip('\n'))
        for _ in range(num):
            tasks.append([int(i) for i in f.readline().split(' ')])

    for i in tasks:
        a = i[0]
        b = i[1]
        result = max_fac(a, b)
        # with open('output.txt', 'a') as f:
        #     f.write(str(result))
        print(result)


if __name__ == '__main__':
    main()


