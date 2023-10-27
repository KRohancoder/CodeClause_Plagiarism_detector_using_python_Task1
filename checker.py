"""
from difflib import SequenceMatcher

with open("text_1.txt") as file1, open("text_2.txt") as file2 :
#open("1. txt") as file1, open("2.txt") as file2:
    file1data=file1.read()
    file2data=file2.read()
    similarity = SequenceMatcher(None,file1data,file2data).ratio()
    #print(similarity*100)
   """ 

from difflib import Differ
from difflib import SequenceMatcher

with open("text_1.txt") as file1, open("text_2.txt") as file2:
    file1data=file1.read()
    file2data=file2.read()

    differ = Differ()
    diff = differ.compare(file1data.splitlines(keepends=True), file2data.splitlines(keepends=True))
    similarity = SequenceMatcher(None,file1data,file2data).ratio()
    print(similarity*100)

    added, removed = 0, 0
    for line in diff:
        if line.startswith("+ "):
            added += 1
        elif line.startswith("- "):
            removed += 1

    print(f"Lines added: {added}")
    print(f"Lines removed: {removed}")
    
    
    
    