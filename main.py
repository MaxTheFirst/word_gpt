from gpt import ChatGPT
from config import API_KEY
import win32com.client as win32

def get_selections():
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.ActiveDocument
    return word.Selection

def main():
    gpt = ChatGPT(API_KEY, 'last_message.txt')
    selection = get_selections()
    result = gpt.generate(selection.Range.Text)
    selection.InsertAfter('\n'+result)

if __name__ == '__main__':
    main()

