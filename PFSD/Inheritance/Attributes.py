from Inheritence.single import a
from Inheritence.multilevel import b

class e(a,b):
    var4=a.var1+b.var3
    print(var4)
