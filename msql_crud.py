import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect('todolist.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed INTEGER DEFAULT 0
)
''')
conn.commit()

def add_task(task):
    cursor.execute('INSERT INTO todos (task) VALUES (?)', (task,))
    conn.commit()

def list_tasks():
    cursor.execute('SELECT id, task, completed FROM todos')
    for row in cursor.fetchall():
        status = 'Done' if row[2] else 'Pending'
        print(f"{row[0]}. {row[1]} [{status}]")

def update_task(task_id, new_task):
    cursor.execute('UPDATE todos SET task = ? WHERE id = ?', (new_task, task_id))
    conn.commit()

def mark_completed(task_id):
    cursor.execute('UPDATE todos SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()

def delete_task(task_id):
    cursor.execute('DELETE FROM todos WHERE id = ?', (task_id,))
    conn.commit()

def main():
    while True:
        print("\nTodo List:")
        list_tasks()
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Lists Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            task_id = int(input("Enter task ID to update: "))
            new_task = input("Enter new task: ")
            update_task(task_id, new_task)
        elif choice == '3':
            list_tasks
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_completed(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '6':
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
    conn.close()