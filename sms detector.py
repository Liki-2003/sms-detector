import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Define a list of common stop words to filter out noise
stop_words = set(stopwords.words('english'))

# Define a function to detect if a message is an SMS
def is_sms(text):
    # Tokenize the input text
    words = word_tokenize(text.lower())

    # Remove stopwords and punctuation
    words = [word for word in words if word.isalnum() and word not in stop_words]

    # Check if the text contains common SMS abbreviations or symbols
    sms_keywords = ["u", "r", "2", "l8r", "gr8", "omg", "brb", "ttyl", "lol", "idk", "b4", "cu", "sry", "thx", "plz", "smh", "btw"]
    for keyword in sms_keywords:
        if keyword in words:
            return True

    return False

# Test the SMS detector
input_text = input("Enter a text message: ")
if is_sms(input_text):
    print("This text appears to be an SMS.")
else:
    print("This text does not appear to be an SMS.")
