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
            # case 2:
            # model.open_pb()    
            # model.save_pb()
            #     view.print_message(text.save_successful)
            #case 3:
            #    model.read_notes()
            #    view.print_message(text.)
            case 4:
                model.edit_note()
                view.print_message(text.edit_successful)
            #     view.print_message(text.new_contact_successful(name))
            # case 5:
            #     key_word=view.input_search()
            #     result=model.search_contact(key_word)
            #     view.print_contacts(result, text.empty_search(key_word))
            # case 6:
            #     key_word=view.input_search(text.input_change)
            #     result=model.search_contact(key_word)
            #     if result:
            #         if len(result) !=1:
            #             view.print_contacts(result, ' ')
            #             current_id=view.input_search(text.input_index)

            #         else:
            #             current_id=result[0].get('id')
            #         new_contact=view.input_contact(text.change_contact)
            #         name=model.change_contact(new_contact, current_id)
            #         view.print_message(text.change_successful(name))
            #     else:
            #         view.print_message(text.change_successful(name))

            # case 7:
            #     key_word=view.input_search(text.input_delete)
            #     result=model.search_contact(key_word)
            #     if result:
            #         if len(result) !=1:
            #             view.print_contacts(result, ' ')
            #             current_id=view.input_search(text.input_index)

            #         else:
            #             current_id=result[0].get('id')
            #         model.delete_contact(result)
            #         view.print_message(text.delete_successful)
            #     else:
            #         view.print_message(text.delete_successful)


            case 7:
                break    
