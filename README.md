

# To-Do List Manager

This project is a command-line based to-do list manager written in Python. It allows users to create, read, update, and delete tasks, as well as update their status. The tasks are stored in a text file for persistence.

## Features

- **Create Task:** Add a new task with a name, time, and status.
- **Read Task:** View the details of a specific task.
- **Update Task:** Change the time associated with a task.
- **Delete Task:** Remove a task from the list.
- **Update Status:** Change the status of a task to pending, started, or finished.
- **Data Persistence:** Save and load tasks from a text file.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/todo-list-manager.git
    cd todo-list-manager
    ```

2. Run the to-do list manager:
    ```bash
    python todo_manager.py
    ```

### Usage

1. Upon running the script, you will be presented with a menu of options:

    ```
    1. Add Task
    2. Read Task
    3. Update Task
    4. Delete Task
    5. Update Status
    6. Exit
    ```

2. Select an option by entering the corresponding number.

3. Follow the prompts to perform the desired action.

## Code Overview

### Class `task`

This class represents a task with a name, time, and status.

### Class `task_manager`

This class manages the tasks, providing methods to create, read, update, and delete tasks. It also handles saving and loading tasks to and from a text file.

- `create_task(name, time, status)`: Adds a new task.
- `read_task(name)`: Displays the details of a task.
- `read_status(name)`: Displays the status of a task.
- `status_change(name, new_status)`: Changes the status of a task.
- `update_task(name, new_time)`: Updates the time of a task.
- `delete_task(name)`: Deletes a task.
- `load_data()`: Loads tasks from the text file.
- `save_data()`: Saves tasks to the text file.

## License

This project is licensed under the MIT License - see the [LICENSE](#LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Authors

- **Fitsum Helina** - [Your GitHub Profile](https://github.com/Fitsumhelina)

---

## LICENSE

MIT License

