'''
1233. Remove Sub-Folders from the Filesystem
Solved
Medium
Topics
Companies
Hint
Given a list of folders folder, return the folders after removing all sub-folders in those folders.
 You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of
folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a",
but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more
lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/"
 are not.
 

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
 

Constraints:

1 <= folder.length <= 4 * 104
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'.
folder[i] always starts with the character '/'.
Each folder name is unique.
'''

# Solution - Hash map

'''
If we sort the input folders by length, we can ensure we are storing smallest subfolder first 
meaning longer folder strings will be able to be removed if they match what's already in the hash. 

We can iterate over each folder and add those characters to a new string, if we find the curr
string in the hash and the next character is '/' it means we found a subfolder so we break and go to the next
iteration.

Otherwise, if we iterate over the entire string without finding a match, then its a new folder that can be added
to the hash and the resulting list. 

Time complexity - O(nlog(n) + n * m), worst case we search through every string and every char
Space: O(n)

'''

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: len(x))
        hash = {}
        res = []
        for s in folder:
            curr = ''
            for i in range(len(s)):
                curr += s[i]
                if curr in hash and s[i + 1] == '/':
                    break
            if len(curr) == len(s):
                hash[curr] = True
                res.append(curr)
        return res

# Simplified
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  
        result = []
        prev = ''
        for path in folder:
            if not prev or not path.startswith(prev + '/'):
                result.append(path)
                prev = path  # Update 'prev' to the current folder
        return result    


# Set

class Solution:
    def removeSubfolders(self, folder) -> list[str]:
        # Create a set to store all folder paths for fast lookup
        folder_set = set(folder)
        result = []

        # Iterate through each folder to check if it's a sub-folder
        for f in folder:
            is_sub_folder = False
            prefix = f

            # Check all prefixes of the current folder path
            while not prefix == "":
                pos = prefix.rfind("/")
                if pos == -1:
                    break

                # Reduce the prefix to its parent folder
                prefix = prefix[0:pos]

                # If the parent folder exists in the set, mark as sub-folder
                if prefix in folder_set:
                    is_sub_folder = True
                    break

            # If not a sub-folder, add it to the result
            if not is_sub_folder:
                result.append(f)
        return result

# Sorting

class Solution:
    def removeSubfolders(self, folder):
        # Sort the folders alphabetically
        folder.sort()

        # Initialize the result list and add the first folder
        result = [folder[0]]

        # Iterate through each folder and check if it's a sub-folder of the last added folder in the result
        for i in range(1, len(folder)):
            last_folder = result[-1]
            last_folder += "/"

            # Check if the current folder starts with the last added folder path
            if not folder[i].startswith(last_folder):
                result.append(folder[i])

        # Return the result containing only non-sub-folders
        return result

# Trie

class Solution:

    class TrieNode:
        def __init__(self):
            self.is_end_of_folder = False
            self.children = {}

    def __init__(self):
        self.root = self.TrieNode()

    def removeSubfolders(self, folder):
        # Build Trie from folder paths
        for path in folder:
            current_node = self.root
            folders = path.split("/")

            for folder_name in folders:
                if folder_name == "":
                    continue

                # Create new node if it doesn't exist
                if folder_name not in current_node.children:
                    current_node.children[folder_name] = self.TrieNode()
                current_node = current_node.children[folder_name]

            # Mark the end of the folder path
            current_node.is_end_of_folder = True

        # Check each path for subfolders
        result = []
        for path in folder:
            current_node = self.root
            folders = path.split("/")
            is_subfolder = False

            for i, folder_name in enumerate(folders):
                if folder_name == "":
                    continue
                next_node = current_node.children[folder_name]
                # Check if the current folder path is a subfolder of an existing folder
                if next_node.is_end_of_folder and i != len(folders) - 1:
                    is_subfolder = True
                    break  # Found a subfolder
                current_node = next_node

            # If not a subfolder, add to the result
            if not is_subfolder:
                result.append(path)

        return result

