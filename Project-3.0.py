word=input("Enter The string: ")
def initialize_dictionary(d):
    dictionary = {}
    for alphabet in d:
        dictionary[alphabet] = 1 + dictionary.get(alphabet, 0)
    return dictionary

def most_frequent(text):
    all_alphabets = [alphabet.lower() for alphabet in text if alphabet.isalpha()]
    dictionary = initialize_dictionary(all_alphabets)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, alphabet in result:
        print (alphabet,':',count)

most_frequent(word)
