class hangman:
    def __init__(self) :

        def random_word(difficulty) :
        if difficulty == "easy" :print()
        if difficulty == "medium" : print()
        if difficulty == "hard" :print ()

        def run(word) :
            word = word
            l = len(word)
            if l <7 : max = 8
            if l >=7 : max = 13
    
            for n in range(max) :
                revealed = []
                for character in word : 
                    for i in revealed :
                        if character==word.asList[i] :
                            print(character)
                            break
                        else :
                            print("_ ")
                user_input = input("Enter your guess")
                counter = 0

                for character in word :
                    if (user_input.lower() == character.lower()) :
                        revealed.append(counter)

                        counter = counter+1


        
    