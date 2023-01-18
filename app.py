from controllersMessage import ControllersMessage


class App:

    def menu(self):
        while True:
            print('****************************************************\n'+
                '****************************************************\n'+
                '*******                 MENU                 *******\n'+
                '******* 1)Crear mensaje encriptado           *******\n'+
                '******* 2)Visualizar mensajes                *******\n'+
                '******* 3)Actualizar mensaje                 *******\n'+
                '******* 4)Eliminar mensaje                   *******\n'+
                '******* 5)Salir                              *******\n'+
                '*******                                      *******\n'+
                '****************************************************\n'+
                '****************************************************\n')

            option = input("Ingrese opcion: ")
            if option == "1":
                message = input('Ingrese Mensaje para encriptar:')
                ControllersMessage().postMessage(message)
            elif option == "2":
                ControllersMessage().getMessage()
            elif option == "3":
                _id = input("Ingrese id del mensaje para actualizar:")
                updateMessage = input("Ingrse mensaje nuevo:")
                ControllersMessage().UpdateMessage(_id,updateMessage)
            elif option == "4":
                deleteMessage = input("Ingrese id del mensaje:")
                ControllersMessage().deleteMessage(deleteMessage)
            elif option == "5":
                break
            else:
                print("Opcion invalida")

App().menu()
