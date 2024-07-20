from collections import deque

#open wordlists
try:
    with open("ordlista_4bok.txt", "r", encoding="utf-8") as file:
        fourLetterList = file.read()
    with open("alphabet.txt", "r", encoding="utf-8") as file2:
        alphabet = file2.read()
except FileNotFoundError:
    print(f"The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

#Tree node class for search tree
class TreeNode:
    def __init__(self, value, level):
        self.value = value
        self.children = []
        self.level = level

#Functions that creates new words by scrabbling letters in a word
def scrabbler(word):
    combos = ['1234','1243','1324','1342','1423','1432','2134','2143','2314','2341','2413','2431','3124','3142','3214','3241','3412','3421','4123','4132','4213','4231','4312','4321']
    possibleWords = []
    for combo in combos:
        newWord = ""
        for i in range(4):
            newWord = newWord + word[int(combo[i])-1]
        if newWord in fourLetterList and newWord != word and newWord not in possibleWords:
            possibleWords.append(newWord)
    return(possibleWords)

#Function that creates new words by replacing one letter in a word
def replacer(word):
    possibleWords = []
    for i in range(4):
        for letter in alphabet:
            wordList = list(word)
            wordList[i] = letter
            newWord = "".join(wordList)
            if newWord in fourLetterList and newWord != word and newWord not in possibleWords:
                possibleWords.append(newWord)   
    return(possibleWords)

#Search function. Returns the shortest path between two values in a tree
def search(root, startValue, targetValue):
    if root is None:
        return None
    
    queue = deque([(root, [])])

    while queue:
        current_node, path = queue.popleft()
        
        # Update the path
        current_path = path + [current_node.value]
        
        # Check if we have reached the target node
        if current_node.value == startValue:
            # If the start node is found, initialize the path from the start node
            start_path = current_path
        
        if current_node.value == targetValue:
            # If the target node is found, return the path
            return current_path
        
        # Add the children to the queue
        for child in current_node.children:
            queue.append((child, current_path))
    
    # If no path is found
    return "no path found"

#Creates the tree
def createTree(startValue, targetValue):
    tree = []
    #Setup tree root
    parent = TreeNode(startValue, 0)
    for result in scrabbler(startValue):
        parent.children.append(TreeNode(result, 1))
    for result in replacer(startValue):
        parent.children.append(TreeNode(result, 1))
    tree.append(parent)

    for child in parent.children:
        for result in scrabbler(child.value):
            child.children.append(TreeNode(result, 2))
        for result in replacer(child.value):
            child.children.append(TreeNode(result, 2))
        tree.append(child)
        for grandChild in child.children:
            for result in scrabbler(grandChild.value):
                grandChild.children.append(TreeNode(result, 3))
            for result in replacer(grandChild.value):
                grandChild.children.append(TreeNode(result, 3))
            tree.append(grandChild)
            for grandGrandChild in grandChild.children:
                for result in scrabbler(grandGrandChild.value):
                    grandGrandChild.children.append(TreeNode(result, 4))
                for result in replacer(grandGrandChild.value):
                    grandGrandChild.children.append(TreeNode(result, 4))
                tree.append(grandGrandChild)
                for grandGrandGrandChild in grandGrandChild.children:
                    for result in scrabbler(grandGrandGrandChild.value):
                        grandGrandGrandChild.children.append(TreeNode(result, 5))
                    for result in replacer(grandGrandGrandChild.value):
                        grandGrandGrandChild.children.append(TreeNode(result, 5))
                    tree.append(grandGrandGrandChild)

    
    return tree

#Main function
if __name__ == "__main__":
    startWord = input("Choose starting word: ")
    targetWord = input("Choose target word: ")

    tree = createTree(startWord, targetWord)
    print(search(tree[0], startWord, targetWord))

    # print(f"Possible letter scrambles: {scrabbler(word)}")
    # print(f"Possible letter switches: {replacer(word)}")

