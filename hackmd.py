import pathlib
import requests
id = "N1naMCFAQb-J0FmQroVlyw"


revisions = F"https://hackmd.io/{id}/revision"

response = requests.get(revisions)

entry = requests.get(
    F"{response.url}/{response.json()['revision'][0]['time']}")

pathlib.Path('index.md').write_text(
    entry.json()['content']
)
