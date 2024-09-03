import ast

tasks_name = 'tasks.txt'
done_name = 'done.txt'

def save_value(input_value, filename):
    with open(filename, 'w') as file:
        file.write(str(input_value))
    
def load_value(filename):
    with open(filename, 'r') as file:
        read = file.read()
    return read

try:
    tasks = ast.literal_eval(load_value(tasks_name))
    tasks_done = ast.literal_eval(load_value(done_name))
    print('Loaded tasks:', tasks)
    print('Loaded tasks done:', tasks_done)

except:
    print('Creating a new file...')
    tasks = []
    tasks_done = []        

def main():
    
    while True:
        print("\n***** To-Do List *****")
        print(" 1) Add task to do")
        print(" 2) Delete task to do")
        print(" 3) Show tasks to do")
        print(" 4) Mark tasks as done")
        print(" 5) Show tasks already done")
        print(" 6) Desmark tasks as done")
        print(" 7) Exit program")
    
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                number_tasks = int(input("\nHow many tasks you want to add: "))

                for i in range(number_tasks):
                    length_before = len(tasks)
                    task = input("Enter task {}: ".format(i+1))
                    tasks.append(task)
                    length_after = len(tasks)
                    
                    if length_before < length_after:
                        save_value(tasks, tasks_name)
                        print("Task added")
                    else:
                        print("Failed to add task")
            
            elif choice == 2:
                
                length_before = len(tasks)
                if len(tasks) == 0:
                    print("No tasks to delete")
                else:
                    task_index = int(input("\nWhich task do you want to delete (1-{})? ".format(len(tasks)))) - 1
                    
                    if task_index > len(tasks):
                        print("Error: You don't have that task")
                    else:
                        del tasks[task_index]
                        length_after = len(tasks)
                        save_value(tasks, tasks_name)
                        
                        if length_before > length_after:
                            print("Task deleted")
                        else:
                            print("Failed to delete task")
            
            elif choice == 3:

                if len(tasks) == 0:
                    print("No tasks to show")
                else:
                    print("\nTasks to do:")
                    for i, task in enumerate(tasks, start=1):
                        print("{} - {}".format(i, task))
                    
            elif choice == 4:
                
                done_before = len(tasks_done)
                task_before = len(tasks)
                
                if len(tasks) == 0:
                    print("No tasks to mark as done")
                else:
                    print("\nTasks to mark as done:")
                    
                    for i, task in enumerate(tasks, start=1):
                        print("{} - {}".format(i, task))
                        
                    task_index = int(input("\nWhich task do you want to mark as done (1-{})? ".format(len(tasks)))) - 1
                    
                    if task_index > len(tasks):
                        print("Error: You don't have that task")
                    else:
                        tasks_done.append(tasks[task_index])
                        done_after = len(tasks_done)
                        
                        if done_before < done_after:
                            save_value(tasks_done, done_name)
                            del tasks[task_index]
                            task_after = len(tasks)
                            
                            if task_after < task_before:
                                save_value(tasks, tasks_name)  
                                print("Task marked as done")
                            else: 
                                print("Failed to mark task as done")
                        else: 
                            print("Failed to mark task as done")
                            
            elif choice == 5:
                
                if len(tasks_done) == 0:
                    print("No tasks already done")
                else:
                    print("\nTasks already done:")
                    
                    for i, task in enumerate(tasks_done, start=1):
                        print("{} - {}".format(i, task))
        
            elif choice == 6:
                
                before_done = len(tasks_done)
                before_task = len(tasks)
                
                if len(tasks_done) == 0:
                    print("No tasks to desmark as done")
                else:
                    task_index = int(input("\nWhich task do you want to desmark as done (1-{})? ".format(len(tasks_done)))) - 1
                    
                    if task_index > len(tasks_done):
                        print("Error: You don't have that task")
                    else:
                        tasks.append(tasks_done[task_index])
                        after_task = len(tasks)
                        if after_task > before_task:
                            save_value(tasks, tasks_name)
                            del tasks_done[task_index]
                            after_done = len(tasks_done)
                            if after_done < before_done:
                                save_value(tasks_done, done_name)
                                print("Task desmarked")
                            else:
                                print("Failed to desmark task")
                        else:
                            print("Failed to desmark task")
                            
            elif choice == 7:
                print("\nExiting...")
                break
            
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
if __name__ == "__main__":
    main()