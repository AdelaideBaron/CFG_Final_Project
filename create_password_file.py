f = open("uniDB_api.txt", "x")
g = open("geocode_ow_api.txt", "x")



f = open("uniDB_api.txt", "a")
g = open("geocode_ow_api.txt", "a")

f.write(uniDB_api_key)
g.write(geocode_ow_api_key)

f.close()
g.close()


#%%

#%%
