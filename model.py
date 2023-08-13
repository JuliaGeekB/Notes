import json
import uuid
from datetime import datetime

from note import Note

notes = []
def add_note():
    title=input("Введите заголовок заметки: ")
    body=input("Введите текст заметки: ")
    date=datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    id=input("Введите номер заметки: ")
    new_note=Note(id,title,body,date)
    notes.append(new_note)
    save_notes(notes)

def read_notes():
    try:
        with open('notes.txt', 'r') as file:
            data=json.load(file)
            notes=[Note(**note) for note in data]
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        notes=[]
    return notes

def save_notes (notes):
    with open ('notes.txt',"w") as file:
        json.dump( [note.__dict__ for note in notes], file, indent=4, separators=(',', ': '))
    




    
    
   