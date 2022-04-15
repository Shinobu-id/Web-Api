import requests 

def license(device):
    validate = ""
    if device in validate:
        data =  {
                "message":"device Terdaftar",
                "response":"True",
                "device":device
                }
    if device not in validate:
        data = {
                "message":"device Tidak Terdaftar",
                "response":"false",
                "device":device
                }
    return data
