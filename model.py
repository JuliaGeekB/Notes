import json
import uuid
from datetime import datetime

from note import Note

notes = []
# Функция добавления заметки
def add_note():
    title=input("Введите заголовок заметки: ")
    body=input("Введите текст заметки: ")
    date=datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    id=str(uuid.uuid4())
    new_note=Note(id,title,body,date)
    notes.append(new_note)
    save_notes(notes)

# Функция чтения заметки
def read_notes():
    try:
        with open('notes.txt', 'r') as file:
            data=json.load(file)
            notes=[Note(**note) for note in data]
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        notes=[]
    return notes

# Функция сохранения заметки
def save_notes (notes):
    with open ('notes.txt',"w") as file:
        json.dump( [note.__dict__ for note in notes], file, indent=4, separators=(',', ': '))

# Функция редактирования заметки
def edit_note():
    id = input("Введите идентификатор заметки для редактирования: ")
    note=next((note for note in notes if note.id ==id), None)
    if note:
        print(f'Редактирование заметки: {note.title}')
        title=input('Введите новый заголовок заметки(оставьте пустым, чтобы не менять): ')
        body=input('Введите новый текст заметки(оставьте пустым, чтобы не менять): ')
        date = input('Введите новую дату и время заметки в формате dd.mm.yyyy hh.mm.ss (оставьте пустым, чтобы не менять): ')
        if title:
            note.title=title
        if body:
            note.body=body
        if date:
            note.date=date
        save_notes(notes)
    else:
        print ('Заметка не найдена')





    
    
   