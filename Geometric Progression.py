#Program to create a G.P. using the common ratio and first term of the user's choice

cr=int(input("enter common ratio:"))
ft=int(input("enter first term:"))
te=int(input("enter number of terms:"))

te=te-2
i=0
print(ft)

while i <=te:
    
    ft*=cr
    i+=1
    print(ft)
