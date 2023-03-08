# There may be many levels of functions nested within functions, but within any one function there is only one local
# scope for that function and the global scope. There are no intermediate scopes.

foo =1
def f1():
    bar = 1
    
    def f2():
        baz=2
        #here, foo is a global variable, baz is a local variable
        #Bar is not in either scope
        print(locals().keys()) #['baz']
        print('bar' in locals()) #False
        print('bar' in globals()) #False
    def f3():
        baz = 3
        print(bar) #bar from f1 is referenced so it enters loccal scope of f3
        print(locals().keys()) #[ 'bar', 'baz']
        print('bar' in local()) # True
        print('bar' in globals()) #False
    def f4():
        bar = 4
        baz = 4
        print(bar)
        print(locals().keys()) #[bar', 'baz']
        print('bar' in locals())
        print('bar' in globals()) #True
        
        
        
        

