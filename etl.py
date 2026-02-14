import requests
import json
import pandas as pd

limit = 10

def extract_data(endpoint):
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Falha ao extrair dados da API: {response.status_code}")
        return None
    
def load_data(data, path):
    id = data["id"]
    #Dentro da pasta path criar um arquivo json com o nome do arquivo sendo o id o nome do .json
    with open(f"{path}/{id}.json", "w") as file:
        json.dump(data, file)



def loop_load_data(endpoint):
    url = "https://dummyjson.com/" + endpoint
    c = 1
    while True:
        data = extract_data(url + "/" + str(c))
        if data and c <= limit:
            load_data(data, "data/" +  endpoint)
        elif c >= limit:
            print(f"Fim da extração de dados do endpoint: {endpoint}")
            break
        else: 
            print(f"Falha ao extrair dados do endpoint: {endpoint} com id: {c}")
            break
        c += 1


def transform_data_json_to_csv(endpoint, c):
    print(f"Transformando {endpoint}/{c}.json para csv")
    with open (f"data/{endpoint}/{c}.json", "r") as file:
        data = json.load(file)
    df = pd.DataFrame([data])
    df.to_csv(f"curated/{endpoint}/{c}.csv", index=False)


endpoints = ["products", "user"]

for endpoint in endpoints:
    #loop_load_data(endpoint)
    for c in range (1, limit + 1):
        transform_data_json_to_csv(endpoint, c)