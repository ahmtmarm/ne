def complicated_function(*args,**kwargs):
    print(args,kwargs)
    pass

complicated_function(3,y =1,z= 2, s="hello",b=True)

def complicated_function(a,b,c=True,d=False):
    print(a,b,c,d)
    pass

complicated_function(*[1,2],**{"c": "hello", "d":"cool"})