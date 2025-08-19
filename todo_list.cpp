#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Structure to hold task info
struct Task {
    string description;
    bool completed;
};

// Function to display menu
void showMenu() {
    cout << "\n===== TO-DO LIST MANAGER =====\n";
    cout << "1. Add Task\n";
    cout << "2. View Tasks\n";
    cout << "3. Mark Task as Completed\n";
    cout << "4. Remove Task\n";
    cout << "5. Exit\n";
    cout << "Choose an option: ";
}

int main() {
    vector<Task> tasks; // list of tasks
    int choice;

    do {
        showMenu();
        cin >> choice;
        cin.ignore(); // to handle newline after number input

        switch (choice) {
            case 1: { // Add Task
                Task newTask;
                cout << "Enter task description: ";
                getline(cin, newTask.description);
                newTask.completed = false;
                tasks.push_back(newTask);
                cout << "Task added!\n";
                break;
            }
            case 2: { // View Tasks
                if (tasks.empty()) {
                    cout << "No tasks available.\n";
                } else {
                    cout << "\nYour Tasks:\n";
                    for (size_t i = 0; i < tasks.size(); i++) {
                        cout << i + 1 << ". " << tasks[i].description
                             << " [" << (tasks[i].completed ? "Completed" : "Pending") << "]\n";
                    }
                }
                break;
            }
            case 3: { // Mark Task Completed
                int index;
                cout << "Enter task number to mark as completed: ";
                cin >> index;
                if (index > 0 && index <= tasks.size()) {
                    tasks[index - 1].completed = true;
                    cout << "Task marked as completed!\n";
                } else {
                    cout << "Invalid task number.\n";
                }
                break;
            }
            case 4: { // Remove Task
                int index;
                cout << "Enter task number to remove: ";
                cin >> index;
                if (index > 0 && index <= tasks.size()) {
                    tasks.erase(tasks.begin() + index - 1);
                    cout << "Task removed!\n";
                } else {
                    cout << "Invalid task number.\n";
                }
                break;
            }
            case 5: {
                cout << "Exiting... Goodbye!\n";
                break;
            }
            default:
                cout << "Invalid option. Please try again.\n";
        }
    } while (choice != 5);

    return 0;
}
