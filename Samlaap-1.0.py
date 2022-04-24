from nltk.chat.util import Chat, reflections
from ExtractKnowledge import from_excel_file

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "your": "my",
    "you'll": "I will",
    "yours": "mine",
    "you": "me",
    "me": "you"
}
pairs = from_excel_file("./References/Knowledgebase.xlsx")


def chat():
    print("Namskaar!")
    chat_bot = Chat(pairs, reflections)
    chat_bot.converse()


if __name__ == '__main__':
    chat()
