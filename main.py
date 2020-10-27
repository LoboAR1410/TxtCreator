import pathlib, os, time, io


def MainMenu():
    print("""================================
==  F I L E   E X P L O R E R ==
== == == ============== == == ==
==  1.- C R E A T E   F I L E == 
==  2.- R E A D   F I L E     ==
==  3.- D E L E T E   F I L E ==
================================""")

def CreateFile(FileName):
    Ruta = "Documentos\\"
    FileName = FileName+".txt"
    File = open(Ruta+FileName,"a+")
    return File

def ModifyFile(FileName):
    Ruta = "Documentos\\"
    FileName = FileName+".txt"
    File = open(Ruta+FileName,"r+")
    return File

def ReadFile(FileName):
    Ruta = "Documentos\\"
    FileName = FileName + ".txt"
    File = open(Ruta + FileName, "r")
    return File

def DeleteFile(FileName):
    FileName = FileName + ".txt"
    Route = "\Documentos\\"
    OR = str(pathlib.Path().absolute())+ Route+ FileName
    return OR



def MenuNav():
    try:
        while True:
            MenuSelected = input("\nSelecciona una opcion (1 , 2 o 3):")
            if MenuSelected in fibo.Option1:
                time.sleep(1)
                print("\n*****C R E A T E  F I L E*****")
                Name = input("Ingresa el nombre del archivo a crear: ")
                CreateFile(Name)
                CreateFile(Name).close()
                time.sleep(1)
                while CreateFile(Name):
                    write = input("Deseas añadir texto al archivo? (0 / 1):")
                    if write == "1":
                        print("Escribe tu texto a continuacion . . . ")
                        UserEntry = input("")
                        ModifyFile(Name).write(UserEntry)
                        ModifyFile(Name).close()
                        time.sleep(3)
                        print("Archivo Creado y Guardado con Exito ! !")
                        print("******************************")
                    elif write =='0':
                        print("Archivo vacio Guardado ! !")
                        time.sleep(1)
                    print("******************************")
                    break


            elif MenuSelected in fibo.Option2:
                print("\n*****R E A D   F I L E*****")
                EName = input("Ingresa el nombre del archivo:")
                try:
                    Content = ReadFile(EName).read()
                    print("\n . . .c a r g a n d o . . .")
                    time.sleep(2)
                    while Content:
                        print("=============================================")
                        print(Content)
                        print("=============================================")
                        break
                except Exception as e:
                    print(e)


            elif MenuSelected in fibo.Option3:
                print("\n*****D E L E T E   F I L E*****")
                DName = input("Ingresa el nombre del archivo:")
                try:
                    FFile = DeleteFile(DName)
                    while FFile:
                        OK = input(f"Estas seguro de eliminar '{DName+'.txt'}? . . .(Si/NO): '")
                        if OK in fibo.YesW:
                            print(' + + + B O R R A N D O + + + ')
                            time.sleep(2)
                            os.remove(str(FFile))
                            print('Archivo eliminado con exito!')
                            print('=============================================')
                            break
                        elif OK in fibo.Nope:
                            print('Arrumbale a la verga entonces ! !')
                            print('=============================================')
                            break

                except Exception as e:
                    print(e)


    except Exception as e:
        print(f"/++/ '{e}' /++/")

MainMenu()
MenuNav()
