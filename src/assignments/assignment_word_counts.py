import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
import json
# Step 1: Convert a Text File to a String

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return str(e)
    

text = read_text_file(r"C:\Users\Tamás\Desktop\Minden fájl\MS\Code\PythonCodeBase\src\assignments\data.txt")
print(text)

# Step 2: Split the String into Words

def split_text(text):
    words = list()
    words = text.lower().split()
    return words
 
words = split_text(text)
print(words)

# Step 3: Exclude Stop Words

stop_words = set(stopwords.words('english'))
 
def remove_stop_words(words,stop_words):
    words_clean = [word for word in words if word not in stop_words]
    return words_clean
 
words_clean = remove_stop_words(words,stop_words)
print(words_clean)

# Step 4: Lemmatize the Words


lemmatizer = WordNetLemmatizer() 
 
def lemmatize_words(words_clean):
    lemmatizer = WordNetLemmatizer()
    words_lemmatized = [lemmatizer.lemmatize(word) for word in words_clean]
    return words_lemmatized
 
words_lemmatized = lemmatize_words(words_clean)
print(words_lemmatized)

# Stem 5: Count the Words

def compute_frequency_words(words_lemmatized):
    words_frequency = {}
    for word in words_lemmatized:
        if word in words_frequency:
            words_frequency[word] += 1
        else:
            words_frequency[word] = 1
    return words_frequency
words_frequency = compute_frequency_words(words_lemmatized)
print(type(words_frequency)) #should print dict
print(words_frequency)

# Stem 6: Export the Results to JSON

def save_words_frequency(words_frequency,file_path):
    with open(file_path, 'w') as json_file:
        json.dump(words_frequency, json_file, ensure_ascii=False, indent=4)

save_words_frequency(words_frequency,file_path=r"C:\Users\Tamás\Desktop\Minden fájl\MS\Code\PythonCodeBase\src\assignments\words_frequency.json")


# Step 7: Combine All Steps in a Single Program
text = read_text_file(r"C:\Users\Tamás\Desktop\Minden fájl\MS\Code\PythonCodeBase\src\assignments\data.txt")
words = split_text(text)
words_clean = remove_stop_words(words,stop_words)
words_lemmatized = lemmatize_words(words_clean)
words_frequency = compute_frequency_words(words_lemmatized)
save_words_frequency(words_frequency,file_path=r"C:\Users\Tamás\Desktop\Minden fájl\MS\Code\PythonCodeBase\src\assignments\words_frequency.json")