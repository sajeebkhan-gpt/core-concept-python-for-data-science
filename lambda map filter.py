#What is lambda
'''A lambda is an anonymous(unnamed) short function defined with the lambda keyword'''
#syntax
'''def f(arguments):
    return expression'''
#3.simple e example
g=lambda: 5
print(g())

#one arguments
square=lambda x:x*x
print(square(5))

#two arguments
add=lambda a,b:a+b
print(add(2,3))

#conditional expression inside lambda
max_two=lambda a,b:a if a>b else b
print(max_two(7,10))
#where lambda is commonly used
'''1.As a short callback sorted()
   2.In map(),filter(),reduce() calls
   3.In GUI or async callbacks(small handers)
   4.For small inline computaions you won't reuse'''
#sorting by a custom key
people=[('sajeeb',22),('arif',19),('naila',24)]
people_sorted=sorted(people,key=lambda item:item[1])
print(people_sorted)

#lambda vs def--which to prefer which
'''use lambd for very short one-line functions used temporary
   use for def:
   multi-line logic
   documentations
   reusability and readability
   lambda has no return statement---expression result is returend and bad readability
   '''

#example:
f=lambda x: x**2 if x>0 else -x**3 if x<0 else 0
#with def example
def f(x):
    if x>0:
        return x**2
    if x<0:
        return -x**3
    return 0
#store lamda in a list /dict
ops={
    'add':lambda a,b: a+b,
    'mul':lambda a,b: a*b
}
print(ops['mul'](4,5))

#apply lambda in a list comprehension style (map like)
nums=[1,2,3,4]
squares=list(map(lambda x:x*x,nums))
#map() applies lambda to each element
#example --lambda capturing variable 
def make_multiplier(n):
    return lambda x: x*n
double=make_multiplier(2)
print(double)
