# Write a program in python that will read a file from a repository. The program should then replace all the instances of the text "Andrew" with your name. The program should then commit those changes and push the file back to the repository.

from github import Github
from config import tempgit
import requests

# Search and replace designated strings in specified file, original not edited

# File
gth = Github(tempgit["https://github.com/d-redmond/data-representation-coursework.git/test.txt"])
# String variables
search_txt = "Andrew"
replace_txt = "Denise"
# Respository copy path
repo = gth.get_repo("https://github.com/d-redmond/data-representation-coursework.git")

test_txt = repo.get_contents("https://github.com/d-redmond/data-representation-coursework.git/test.txt")
test_url = test_txt.download_url

# Get file url, get file text, replace function
response = requests.get(test_url)
test_txt = response.text
test_copy = test_txt.replace(search_txt, replace_txt)

# https://stackoverflow.com/questions/40630829/how-to-update-a-file-using-pygithub
gth_response = repo.update_file(test_txt.path, "edited copy of test", test_copy, test_txt.sha)
print(gth_response)