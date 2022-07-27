import requests
import json
from pprint import pprint as pp

unis = ['The University of Aberdeen', 'University of Abertay Dundee', 'Aberystwyth: United Theological College and College of Welsh Independents', 'The University of Wales', 'Anglia Polytechnic University', 'Askham Bryan College', 'Aston University', 'Aylesbury College', 'University of Wales, Bangor', 'Barking and Dagenham College', 'Barnsley College', 'Basingstoke College of Technology', 'University of Bath', 'Bath Spa University College', 'The University of Birmingham', 'Birmingham College of Food, Tourism and Creative Studies', 'Bishop Burton College', 'Bishop Grosseteste College', 'Blackburn College' ]#, ‘Blackpool and The Fylde College’, ‘University of Bolton’, ‘Boston College’, ‘Bournemouth University’, ‘The Arts University College at Bournemouth’, ‘The University of Bradford’, ‘Bradford College’, ‘Bretton Hall College’, ‘Bridgwater College’, ‘University of Brighton’, ‘University of Bristol’, ‘University of the West of England’, ‘British College of Naturopathy and Osteopathy’, ‘The British Institute in Paris’, ‘University of London)’, ‘Brunel University London’, ‘British School of Osteopathy’, ‘Brockenhurst College’, ‘Broxtowe College’, ‘The University of Buckingham’, ‘Buckinghamshire Chilterns University College’, ‘Burton College’, ‘Cambridge University’, ‘Cannington College’, ‘Canterbury Christ Church University’, ‘Canterbury College’, ‘Cardiff University’, ‘Cardiff Metropolitan University’]
valid_unis = []
invalid_unis = []

if __name__ == "__main__":
    for uni in unis:
        endpoint = "https://unidbapi.com/api/university/read_demographics?u={}&key=cfd3d28159".format(uni)
        response = requests.get(endpoint)
        if json.dumps(response.json()) != "{\"error\": \"Invalid Query\"}":
            valid_unis.append(uni)
        else:
            invalid_unis.append(uni)

    for unis in invalid_unis:
        try_the = 'The ' + uni
        endpoint = "https://unidbapi.com/api/university/read_demographics?u={}&key=cfd3d28159".format(try_the)
        response = requests.get(endpoint)
        if json.dumps(response.json()) != "{\"error\": \"Invalid Query\"}":
            valid_unis.append(uni)

    for unis in valid_unis:
        # endpoint = "https://unidbapi.com/api/university/read_demographics?u={}&key=cfd3d28159".format(uni)
        #
        # response = requests.get(endpoint)
        # pp(response.json())
        print(unis)



#%%
