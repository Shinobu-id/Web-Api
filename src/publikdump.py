import requests

def publik(user,token):
    id = []
    try:
        po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
        for i in po['friends']['data']:
            data = {
                    "id":i["id"],
                    "name":i["name"]
                    }
            id.append(data)
        result = {
                "data": {
                    "status":"True",
                    "users":id
                    }}
        return result
    except KeyError:
        text = {
                "response":"false",
                "message":"Pertemanan tidak ada atau di private"
                }
        return text
