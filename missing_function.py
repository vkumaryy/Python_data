class CutomDict(dict):
    def __missing__(self, key):
        return f'key: "{key}" does not exist'
    
data ={'a':1,'b':2,'c':3}
cd = CutomDict(data)

print(cd['z'])
print(cd)