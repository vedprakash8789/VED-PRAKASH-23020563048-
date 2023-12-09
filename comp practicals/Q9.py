def analyze_file(file_path):
   with open(file_path, 'r') as file:
        content = file.read()
        char_count = len(content)
        word_count = len(content.split())
        line_count = content.count('\n') + 1

        print("Total number of characters:", char_count)
        print("Total number of words:", word_count)
        print("Total number of lines:", line_count)

        char_frequency = {}
        for char in content:
              char_frequency[char] = char_frequency.get(char, 0) + 1

        print("\nCharacter frequency:")
        for char, count in char_frequency.items():
              print(f"'{char}': {count}")
        reversed_words = content.split()[::-1]
        print("\nWords in reverse order:", ' '.join(reversed_words))

    with open(file_path, 'r') as file, open('File1.txt', 'w') as file1, open('File2.txt', 'w') as file2:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i % 2 == 0:
                file1.write(line)
            else:
                file2.write(line)


analyze_file(file_path)
