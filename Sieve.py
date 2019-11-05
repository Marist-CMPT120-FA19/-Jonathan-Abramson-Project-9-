#Designed by Jonathan Abramson
#jonathanabramson14@gmail.com
#This project has been designed to aid in finding prime numbers

def main():

    #This next line allows the user to put in the number that primes will display up until
    Upperlimit = int(input("Enter the maximum integer you would like: "))
    Prime_Numbers = []
    other= []
    
    for i in range(2, Upperlimit +1):
        Prime_Numbers.append(i)
        
    while len(Prime_Numbers)>0:
        prime = Prime_Numbers.pop(0)

    #Shows the user the prime integers leading up to their number they submitted
        print(prime, "is a prime integer")
        for x in Prime_Numbers:
            if x % prime == 0: 
               Prime_Numbers.remove(x)
               
    return other
    print(prime(Upperlimit))
    
main()