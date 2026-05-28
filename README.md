# 🎓 Student Manager Application

A lightweight, terminal-based Python application to manage student profiles, roll numbers, and marks across multiple subjects. The application features persistent data storage using built-in file handling to ensure data remains saved even after closing the program.

## 🚀 Features

- **Add Student Profiles**: Store student names, secure integer roll numbers, and dynamic lists of custom subjects with corresponding marks.
- **View Database**: Displays structured, highly readable profiles for all registered students directly in the console.
- **Dynamic Performance Assessment**: Automatically calculates total marks obtained, global percentage limits, and outputs standard decimal precision values.
- **Secure Record Deletion**: Wipe records from active application memory and automatically update storage files.
- **Persistent Storage**: Leverages Python's built-in `json` module to read/write structured data safely to disk.

## 📂 Data Structure Schema

The application handles file processing by mapping data into a nested JSON structure within `students.json`:

```json
{
    "Student Name": {
        "Roll no": 12345,
        "Marks": {
            "Subject A": 85,
            "Subject B": 92
        }
    }
}
```

## 🛠️ Prerequisites

- **Python 3.x** installed locally.
- No external libraries or third-party frameworks are required (uses built-in standard libraries `json` and `os`).

## 💻 How To Run

1. Clone or download this repository to your local system.
2. Open your terminal or command prompt and navigate to the project directory.
3. Execute the script using the following command:

```bash
python student_manager.py
```

## ⚙️ How It Works (Behind the Scenes)

- **`os.path.join(SCRIPT_DIR, "students.json")`**: Ensures that the storage file is always generated in the absolute directory path of the active script, avoiding workspace route directory confusion inside code editors like VS Code.
- **`json.load()` & `json.dump()`**: Handles standard stream serialization to seamlessly read from and overwrite data to disk.
- **Error Handling Optimization**: Uses specific formatting conditions (such as handling whitespace blocks with `.strip()`) to guarantee robust inputs.
