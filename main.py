from win32com import __gen_path__
from gpt import ChatGPT
from config import API_KEY
import win32com.client as win32
from os import walk
from shutil import rmtree



def get_selections():
    try:
        word = win32.gencache.EnsureDispatch('Word.Application')
        word.ActiveDocument
    except AttributeError:
        paths = list(walk(__gen_path__))
        rmtree(paths[0][0] + '\\' + paths[0][1][0])
        return get_selections()
    return word.Selection

def main():
    gpt = ChatGPT(API_KEY, 'last_message.txt')
    selection = get_selections()
    result = gpt.generate(selection.Range.Text)
    selection.InsertAfter('\n'+result)

if __name__ == '__main__':
    main()

