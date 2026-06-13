try:
    # Open the text file
    file = open("sample.txt", "r")

    # Read file content
    content = file.read()

    # Split content into words
    words = content.split()

    # Count words
    word_count = len(words)

    print("Total number of words:", word_count)

    # Close the file
    file.close()

except FileNotFoundError:
    print("Error: File not found.")