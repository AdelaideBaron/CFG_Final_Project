#double check what was written:
f = open("passwords.txt", "r")

f = open("uniDB_api.txt", "r")
g = open("geocode_ow_api.txt", "r")

#print(f.read())
api_key = f.readline()
api_key_2 = g.readline()

print(api_key + 'a')
print(api_key_2 + 'a')
#
# print(f.readline())
# print(f.readline())
#%%
