# def hap(a,b):
#     return a+b

# hap = lambda a,b:a+b
# rst = hap(10,20)
# print(rst)
data=[10,20,30,40,50]
def myfilter( dt , key ):
    return [n for n in dt if key(n) ]

# rst = myfilter(data,lambda v:v<=30)
rst = myfilter(data,lambda v:v>30)
print(rst)




