letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'," "]
write_encrypt = input (" Do you want to write a letter or encrypt the letter (write/encrypt/end) : ")
while write_encrypt != "end":
    if write_encrypt == "write":
        sentence = input("Please enter the sentence : ")
        spacing_words = int(input("tedad fasele ra vared konid :"))
        if " " in sentence:
            sentence.replace(" ","")
        for word in sentence :
            index = letters.index(str(word))
            word_size =  index + spacing_words
            if word_size > 25 :
                g = word_size % len(letters)
                print(letters[g],end="")
            else :
                print(letters[word_size],end="")
    elif write_encrypt == "encrypt" :
        sentence = input("Please enter the sentence : ")
        spacing_words = int(input("tedad fasele ra vared konid :"))
        if " " in sentence:
            sentence.replace(" ","")
        for word in sentence :
            index = letters.index(str(word))
            word_size =  index - spacing_words
            if word_size > 25 :
                g = word_size % len(letters)
                print(letters[g],end="")
            else :
                print(letters[word_size],end="")
    else :
        print("Nothing to do")
    print()
    print("---------------------")
    write_encrypt = input (" Do you want to write a letter or encrypt the letter (write/encrypt/end) : ")
exit()
