import requests

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

# pixela = requests.post(url = pixela_endpoint, json =Pixela_Params)

# print(pixela)

#example message{"message":"Success. Let's visit https://pixe.la/@a-know , it is your profile page!","isSuccess":true}

graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"

graph_params = {
    "id":"test-graph",
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
    "X-USER-TOKEN": token,
}
graph_response = requests.post(url = graph_endpoint, json =graph_params, headers = headers)
graph_response.raise_for_status()
print(graph_response.text)
