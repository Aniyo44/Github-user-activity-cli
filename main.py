import requests

def main():
    print("WELCOME TO GitHub User Activity CLI")
    username=input("what is your github username ?: \n")
    url=f"https://api.github.com/users/{username}/events"
    data=requests.get(url).json()
    print(data)






if __name__== "__main__":
    main()
