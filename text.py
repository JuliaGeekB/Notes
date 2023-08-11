main_menu='''\n Главное меню:
    1. Создать заметку.
    2. Сохранить заметку.
    3. Вывести список заметок.
    4. Редактировать заметку.
    5. Удалить заметку.
    6. Открыть заметку.
    7. Выход. \n'''
input_choice='Выберите пункт меню: '
add_successful='Заметка успешно создана'
load_successful='Заметка успешно открыта'
save_successful='Телефонная книга успешно сохранена'
pb_empty='Телефонная книга пуста или не загружена'
input_new_contact='Введите данные нового контакта: '
new_contact={'name':'Введите имя: ','phone':'Введите номер телефона: ','comment':'Введите комментарий: '}
def new_contact_successful(name:str):
    return f'Контакт {name} успешно добавлен'
input_search='Введите параметр поиска: '
def empty_search(word) -> str:
    return f'Контакты, содержащие слово "{word}" не найдены'
input_change='Какой контакт будем изменять?'
change_contact='Введите новые данные или оставьте пустым, чтобы не менять: '
input_index='Введите индекс контакта: '

def change_successful(name: str)->str:
    return f'Контакт {name} успешно изменен'
input_delete='Какой контакт удалить? '

delete_successful='Контакт успешно изменен'