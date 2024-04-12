class task:

    '''
    creating a new task class for entire project
    that has :
       -task name and
       -task time
    with:
     -task_manager
     -task_creator
     -task_reader
     -task_updater
     -task_deleter

     option 

    '''

    def __init__(self, name, time, status):
        self.name = name
        self.time = time
        self.status = status

# Creating a new task manager to control the todo list
        
class task_manager:

#initialize the task manager
    
    def __init__(self, file_path="todo_list.txt"):
        print("Welcome to the to-do list manager")
        self.file_path = file_path
        self.tasks = {}
       

#creating 'create_task ' function

    def create_task(self, name, time, status):
        tasks = task(name, time, status)
        self.tasks[name] = tasks
        self.save_data()

#creating a 'read_task' manager

    def read_task(self, name):
        if name in self.tasks:
            print(f"Task: {self.tasks[name].name}, \n time: {self.tasks[name].time} , ")
        else:
            print("Task not found.")

#creating 'read_status' function 
            
    def read_status(self, name):
        if name in self.tasks:
            task_status = self.tasks[name].status
            if task_status == '1':
                print("Task status: pending")
            elif task_status == '2':
                print("Task status: started")
            elif task_status == '3':
                print("Task status: finished")
        else:
            print("status  not found.")

#creating 'status_changer' function

    def status_change(self, name, new_status):
        if name in self.tasks:
            self.tasks[name].status = new_status
            self.save_data()
        else:
            print("task  not found.")

#creating 'update_task' function 

    def update_task(self, name, new_time):
        if name in self.tasks:
            self.tasks[name].time = new_time
            self.save_data()

#creating 'delete_task' function           

    def delete_task(self, name):
        if name in self.tasks:
            del self.tasks[name]
            self.save_data()
        else:
            print("Task not found.")



# #creating 'load_data' function 

    def load_data(self):
            
            with open(self.file_path, "r") as f:
                for line in f:
                    name, time, status = line.strip().split(",")
                    self.tasks[name] = task(name, time, status)

#creating 'save_data' function  
    

    def save_data(self):
        # with open(self.file_path, "a") as file:
          file=open (self.file_path, "w")
          for task in self.tasks.values():
                file.write(f"{task.name},{task.time} , {task.status}\n")
           
                   
        


# Creating menu function
                
task_mgt = task_manager()
while True:

#displaying the menu option for the user
    
    print("1. Add Task\n2. Read Task\n3. Update Task\n4. Delete Task \n5. Update Status \n6. Exit\n")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter the task name: ")
        time = input("Enter the task time: ")
        status = input("Enter the task status: (1-for pending , 2- for started , 3- finished) ")
        task_mgt.create_task(name, time, status)

    elif choice == '2':
        name = input("Enter the task name: ")
        task_mgt.read_task(name)
        task_mgt.read_status(name)

    elif choice == '3':
        name = input("Enter the task name: ")
        new_time = input("Enter the new time: ")
        task_mgt.update_task(name, new_time)

    elif choice == '4':
        name = input("Enter the task name: ")
        task_mgt.delete_task(name)

    elif choice == '5':
        name = input("Enter the task name: ")
        new_status = input("Enter the task status: (1-for pending , 2- for started , 3- finished)")
        task_mgt.status_change(name, new_status)

    elif choice == '6':
        break
