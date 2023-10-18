# Tamás Bus, 2023.10.17

s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, 
and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, 
but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges -
and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said 
"my universe": but now my mind has been opened to higher views of things."""



def main():
    # Step 1: Normalize the Letter Casing
    s_lower = s.lower()
    print(s_lower)

    # Step 2
    words = list() #do not delete. this list must contain the list of words. 
 
    words = s_lower.split()
    
    print(words) #do not delete 
    #do not write any code past here

    # Step 3
    word_count = len(words)
    print(word_count)

    # Step 4 
    distinct_words = set(words)
    distinct_word_count = len(distinct_words)
    print(distinct_word_count)

    # Step 5
    #we define w as a list of words 
    w = ["haythem","is","eating","tacos.","haythem","loves","tacos","",":"]
    
    #we define an empty dictionary that will hold the token/frequency key-value pair
    #  key:word, value:int that corresponds to the frequency of occurrence
    freq_occur = dict()
    
    for word in w:
        if word in freq_occur:
            freq_occur[word] += 1
        else:
            freq_occur[word] = 1
    
    print(freq_occur)

    word_freq = dict()
 
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    print(word_freq)

    # Step 6 - Remove Punctuation Marks

    import string #import the string module 
    #use the built-in string.punctuation method to create a list of all punctuation marks
    punctuation_list =  list(string.punctuation)
    #display the punctuation_list
    print(punctuation_list)
    
    w = ["haythem!","is","eating","tacos.",".haythem","loves","tacos","",":"]
    w_clean = list()
    #do not change the code above this line.
    
    #your code goes here 
    
    print(w_clean)
    print(len(w_clean))



if __name__ == "__main__":
    main()