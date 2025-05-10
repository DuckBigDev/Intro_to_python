def main(words):

    def text_to_binary(text):
        return ' '.join(format(ord(char), '08b') for char in text)

    def binary_to_text(binary):
        return ''.join(chr(int(b, 2)) for b in binary.split())

    def sort_binary_words(words):
        binary_words = {word: text_to_binary(word) for word in words}
        sorted_binary_words = sorted(binary_words.items(), key=lambda x: int(x[1].replace(" ", ""), 2), reverse=True)
        return sorted_binary_words

    #Urutkan
    sorted_words = sort_binary_words(words)

    #Print
    print("Data terbesar ke terkecil:")
    for word, binary in sorted_words:
        print(f"{word}: {binary}")

#Contoh
if __name__ == "__main__":
        Data1 = ["takut", "putih", "serang", "pintu"]
        main(Data1)

        Data2 = ["pelan", "daki", "hitam", "dahsyat", "gelas"]
        main(Data2)