text = "This is text with an [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)"
for words in text.split('['):
    if ")" in words:
        for word in words.split(')'):
            if "]" in word:
                print(f'[{word})')
            else:
                print(word)
    else:
        print(words)