import requests
import json 

def describe_event(event):
    type_ = event['type']
    repo_name = event['repo']['name']
    payload = event.get('payload', {})

    if type_ == 'PushEvent':
        count = payload.get('size', 0)
        return f"- Pushed {count} commit{'s' if count != 1 else ''} to {repo_name}"
    elif type_ == 'IssuesEvent':
        action = payload.get('action', 'did something with')
        return f"- {action.capitalize()} an issue in {repo_name}"
    elif type_ == 'IssueCommentEvent':
        return f"- Commented on an issue in {repo_name}"
    elif type_ == 'PullRequestEvent':
        action = payload.get('action', 'acted on')
        return f"- {action.capitalize()} a pull request in {repo_name}"
    elif type_ == 'WatchEvent':
        return f"- Starred {repo_name}"
    elif type_ == 'CreateEvent':
        ref_type = payload.get('ref_type', 'content')
        ref = payload.get('ref')
        if ref:
            return f"- Created {ref_type} '{ref}' in {repo_name}"
        else:
            return f"- Created new {ref_type} in {repo_name}"
    else:
        return f"- Did a {type_} in {repo_name}"


def main():
    print("WELCOME TO GitHub User Activity CLI")
    username = input("What is your GitHub username?: \n")
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data. Please check the username and try again.")
        return

    events = response.json()


    print("\nRecent GitHub Activity:")
    for event in events:
        print(describe_event(event))


if __name__ == "__main__":
    main()
