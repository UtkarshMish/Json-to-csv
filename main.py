import json

jsonExport = []


def converter(filename):
    with open(filename) as json_pwd:
        jsonExport = json.load(json_pwd)
    with open(filename.split(".")[0]+".csv", 'w') as csv_pwd:
        csv_pwd.writelines("name,url,username,password\n")

    for index, data in enumerate(jsonExport['AUTHENTIFIANT']):
        name = f"www.{data['domain']}"
        url = f'https://{name}/'
        username = data['email'] if len(data['email']) > 0 else data['login']
        password = data['password']
        with open(filename.split(".")[0]+".csv", 'a') as csv_pwd:
            csv_pwd.writelines(f'{name},{url},{username},{password}\n')
        print("Completed", index+1)


if __name__ == "__main__":
    filename = input("Enter the JSON filename : ")
    try:
        converter(filename)
        print("File Saved Successfully !!")
    except FileNotFoundError as fnf:
        print(fnf)
