from import_dictionary import load

def search_for_anagrams():
    while True:
        word_list = load('2of4brif.txt')
        anagrams = []
        print('Anagram Search Tool')
        print('by: Logan Dye')
        print()
        print('Please enter a word ar phrase: ', end=' ')
        user_input = input()
        user_input_sorted = sorted(user_input)
        for word in word_list:
            word = word.lower()
            if word != user_input:
                if sorted(word) == user_input_sorted:
                    anagrams.append(word)
        print()
        if len(anagrams) == 0:
            print('No anagrams found.')
        else:
            print('Anagrams are: ', *anagrams, sep=" ")
        print()
        print('Would you like to try again? ', end=' ')
        if input() == "yes":
            continue
        else:
            break