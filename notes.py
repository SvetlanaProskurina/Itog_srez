import datetime
import json

datas = 'notes.json'

def file_exist(data):
    file_exist = 0
    try:
        with open(data, 'r', encoding='utf-8') as openfile:
            file_exist = 1
        
    except FileNotFoundError: 
        print ("Запрашиваемый файл не был найден")  
        file_exist = 0
        
        
    return file_exist
# file_exist(datas)       
        
def read_data(data):
    file_e = file_exist(data)
    adds = {}
    if file_e !=0:
        with open(data, 'r', encoding='utf-8') as openfile:
            adds = json.load(openfile)
            for line, body in adds.items():
                print(line,":")
                print(body,"\n")
                
    return adds
          
read_data(datas)   
 
def add_new_note(data):
    adds ={}
    file_e = file_exist(data)
    
    if file_e == 0:
        with open(data, 'w',encoding='utf-8') as f:
                print ("Создан новый пустой файл")
                adds={}
                json.dump(adds, f, ensure_ascii=False, indent=4, default = str)
        add_new_note(data)
    else:
        print("Идет добавление заметки...")
            
        current_dt = datetime.datetime.now()
        str_date = current_dt.strftime("%d-%m-%Y %H:%M:%S")
        
        print("Введите название заметки:")
        name = input()
        
        print ("Введите тело заметки:")
        body = input()
        
        print ("Заметка соханена!")
        
        adds = {}
         
        with open(data, 'r', encoding='utf-8') as r:
            adds = json.load(r)    
            adds[name] = body + " #" + str_date
      
        with open(data, 'w', encoding='utf-8') as f:
            
            json.dump(adds, f, ensure_ascii=False, indent=4, default = str)
            f.write('\n')
   


def search_data(data):
    if file_exist(data) == 1:
        print("Введите данные для поиска: ")
        search_value = input()
        note = ""
        len = 0
    
        with open(data,'r', encoding='utf-8') as file:
            
            for line in file:
                if search_value in line:
                    print("Найдены следующие заметки:", line, end='')
                    note = line
                    len+=1
                    
            if len == 0: 
                print("Такой заметки нет, попробуйте снова")
                
    else:
        print("Файл c заметками не найден")
    
    return [len, note]


def edit_note(data):
    if file_exist(data) == 1:
        print ("Выберите заметку которую хотите редактировать или удалить")    
        searching = search_data(datas)
        edits = {}
        if searching[0] > 1:
            print("Выберите конкретную заметку:")
            
        else:
            print("Вы выбрали: "+ searching[1])
            key_str = ((str(searching[1].split(": ")[0])).lstrip()).replace('"','')
            
            print("Хотите удалить заметку? Y/N ")
            yn = input()
            if yn == "y" or yn == "Y":
                with open(data, 'r', encoding='utf-8') as r:
                    edits = json.load(r)  
                 
                edits.pop(key_str)
                
                with open(data, 'w', encoding='utf-8') as f:
                    json.dump(edits, f, ensure_ascii=False, indent=4, default = str)
                print ("Заметка удалена!")
            else:
                print ("Введите новые данные:")  
                new_data = input()
                
                
                with open(data, 'r', encoding='utf-8') as r:
                    edits = json.load(r)
                    
                with open(data, 'w', encoding='utf-8') as f:
                    current_dt = datetime.datetime.now()
                    str_date = current_dt.strftime("%d-%m-%Y %H:%M:%S")
                    
                    edits[key_str] = str_date + " : " + new_data
                    json.dump(edits, f, ensure_ascii=False, indent=4, default = str)
                print ("Заметка соханена!")
            
        
def menu (data):
    choice = 0
    while choice < 5:
        try: 
            choice = int(input("Выберите действие и введите соответствующую цифру: "
            "\n1 - Прочитать все заметки"
            "\n2 - Добавить заметку"
            "\n3 - Редактировать/удалить заметку"
            "\n4 - Поиск заметки\n") )
         
            if choice == 1:
                read_data(datas)
            elif choice == 2:
                add_new_note(datas)
            elif choice == 3:
                    edit_note(datas)
            elif choice == 4:
                search_data(datas)
            elif choice >3:
                break
        except:
            print("Неверный ввод, попробуйте еще раз")
    else:
        print("попробуйте снова")
menu(datas)
