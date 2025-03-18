def dcecor(func):
    def inner(name):
        if name=="sunny":
            print("this is sunny")
        else:
            func(name)
    return inner

@dcecor
def wish(name):
    print("helo",name)
wish("durga")
wish("sunny")

def mygan():
    yield "A"
    yield "b"
    yield "c"

g=mygan()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

def count(num):
    print("counter")
    while(num>0):
        yield num
        num=num-1


a=count(5)
for i in a:
    print(i)