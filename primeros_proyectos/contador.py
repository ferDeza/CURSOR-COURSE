from collections import Counter
read=input("introduce la ruta del archivo de texto: ")
with open(read, "r") as file:
    content = file.read()
    total_words = len(content.split())
    word_count = Counter(content.split())
    print(f"El archivo tiene {total_words} palabras")
    print(word_count)
