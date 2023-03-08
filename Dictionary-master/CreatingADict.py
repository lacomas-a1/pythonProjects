# # A dictionary is an example of a key value store also known as Mapping in Python. It allows you to store and retrieve
# # elements by referencing a key. As dictionaries are referenced by key, they have very fast lookups. As they are
# # primarily used for referencing items by key, they are not sorted./

# d={} #empty dict
# d={'key':'values'} #dict with initial values

# # makes a shallow copy of otherdict
# # d = {**otherdict}
# # also updates the shallow copy with the contents of the yetanotherdict.
# # d = {**otherdict, **yetanotherdict}

# #dict comprehension
# d={k:v for k,v in [('key','values')]}

# # built-n class
# d=dict()                  #empty dict
# d=dict(key='value')       #explicit keyword argument
# d=dict([('key','value')]) #passing in alist of key/value pairs
# #make a shallow copy of another dict(ony possible if the key are only String)
# # d=dict(**otherdict)

# #modifying a dict
# # To add items to a dictionary, simply create a new key with a value:
# d['newkey']=42

# # It also possible to add list and dictionary as value:
# d['new_list']=[1,2,3]
# d['new_dict']={'nested_dict':1}


mydict={}
print(mydict) #{}
# value = mydict.get(key, default_value)
print(mydict.get("foo","bar"))  #bar
print(mydict) #{}

print(mydict.setdefault("foo","bar"))   #bar
print(mydict)     #{'foo','bar'}
