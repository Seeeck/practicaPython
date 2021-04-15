
def gap(g, m, n):
    # your code
    def isPrime(num):
        sum=0
        for i in range(2,9):
            numTxt=str(num/i)
            arr=numTxt.split('.')
            if int(arr[1])==0:
                sum+=1
        if sum==0:
            return True
        else:
            return False
################################
    c=0
    for a in range(m, n):
        if c==1:
            break
        elif isPrime(a):
            for i in range(a,n):
                if isPrime(i) and i-a==g and i>a:
                    print([a,i])
                    c=1
                    break
                elif isPrime(i) and i-a<g and i>a:
                    break
gap(10,300,400)
