import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
token= "DV32DidUNwko46vassdf"
username = "buffaloman50"

Pixela_Params ={
    "token":token,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
   # "thanksCode":"ThisIsThanksCode"
}

#pixela = requests.get(url = pixela_endpoint, json =Pixela_Params)
#
# print(pixela)

#example message{"message":"Success. Let's visit https://pixe.la/@a-know , it is your profile page!","isSuccess":true}
#
# graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
#
graph_params = {
    "id":"graph1",
    "name":"graph-name",
    "unit":"commit",
    "type":"int",
    "color":"shibafu",
    "timezone":"Asia/Tokyo",
    "description":"This is a graph for test.",
    # "isSecret":True,
    # "publishOptionalData":true
}

headers = {
    "X-USER-TOKEN": token
}
# graph_response = requests.post(url = graph_endpoint, json =graph_params, headers = headers)
# print(graph_response.text)


##### Post a pixel ######
pixela_add_data_endpont = f"{pixela_endpoint}/{username}/graphs/{graph_params['id']}"


pixel_add_params = {
    "date":datetime.now().strftime("%Y/%m/%d"),
    "quantity":"5",
    "optionalData":"{\"key\":\"value\"}"
}


# Pixel_post_response = requests.post(url = pixela_add_data_endpont, json =pixel_add_params, headers = headers)
# print(Pixel_post_response.text)

#pixela_update_data_endpont = f"{pixela_endpoint}/{username}/graphs/{graph_params['id']}/{datetime.now().strftime('%Y/%m/%d')}"
pixela_update_data_endpont = f"{pixela_endpoint}/{username}/graphs/{graph_params['id']}/20261011"
#pixela_update_data_endpont = f"{pixela_endpoint}/{username}/graphs/graph1/20261011"

#### update a pixel ####
pixel_update_params = {
    "quantity":"20"
}
Pixel_update_response = requests.put(url = pixela_update_data_endpont, json =pixel_update_params, headers = headers)
print(Pixel_update_response.text)
