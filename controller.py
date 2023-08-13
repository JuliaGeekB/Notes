import view
import model
import text

def start():
    while True:
        choice=view.main_menu()
        
        match choice:
            case 1:
                model.add_note()
                view.print_message(text.add_successful)
            case 2:
                model.view_notes()    
            case 3:
                model.edit_note()
                view.print_message(text.edit_successful)
            case 4:
                model.delete_note()
                view.print_message(text.delete_successful)
            case 5:
                break    
