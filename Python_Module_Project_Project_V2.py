tasklist = []
########################################################### 
def menu():
    print('---Welcome User, to the task manager---')
    print('please choose option from the below menu')
    print('1. Add task')
    print('2. View tasks')
    print('3. Delete tasks')
    print('4. Quit the application')
    
    while True:
        try:
            numpick = input("Select numeric option: ").strip()
            
            if numpick not in ['1', '2', '3', '4']:
                raise ValueError('Invalid menu option!')
        except ValueError as e:
            print('Oh no, you have selected an invalid option!')
            print('Please choose a valid number')
        else:
            return numpick
        finally:
            pass
   
##############################################################
def selector(numpick, tasklist):
    if numpick == '1': 
        add_task(tasklist) 
    elif numpick == '2': 
        view_task(tasklist)
    elif numpick == '3': 
        delete_task(tasklist) 
    elif numpick == '4': 
        quitapp() 
############################################################## 
def add_task(tasklist): 
    if len(tasklist) == 0:
        print('What would you like to add?', '\n')
    else:
        print('Here is the current list. What would you like to add?') 
        print(f'Tasks: {tasklist}', '\n') 
    task = input("Enter the task you would like to add: ")
    while not task.strip():
         task = input("Enter the task you would like to add or enter 'no' to go to menu: ")
    if task != 'no':     
        tasklist.append(task) 
        print('Here is the updated list', '\n', f'Tasks: {tasklist}') 
############################################################## 
def view_task(tasklist):
    if len(tasklist) == 0: 
        print('There are no tasks at this time.') 
    else: 
        print('Here is the current list.', '\n', f'Tasks: {tasklist}', '\n', '\n') 
############################################################## 
def delete_task(tasklist): 
    print('Here is the current list. What would you like to delete?', '\n', f'Tasks: {tasklist}', '\n', '\n') 
    task = input("Enter the task to delete or enter 'no' to go to menu: ") 
    while (task not in tasklist or not task.strip()): 
        if task == 'no':
            break
        print('You have entered an invalid task. This is the current list:', '\n', f'Tasks: {tasklist}') 
        task = input("Please try entering another task or enter 'no' to go to menu: ") 
    if task != 'no': 
        tasklist.remove(task) 
        print('Here is the updated list', '\n', f'Tasks: {tasklist}') 
############################################################## 
def quitapp(): 
    print('thank you for visting!') 
    exit() 
############################################################## 
##############################################################

while True: 
    try:
        numpick = menu() 
        selector(numpick, tasklist)
    except Exception as e:
        print('Look like we have an issue, here is the error:', e)
    finally:
        pass