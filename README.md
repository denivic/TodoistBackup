
# 📝 TodoistBackup

> A simple backup utility for Todoist using their API. 🚀💾

---

## ✨ Main Features

- 🔒 Backup your Todoist tasks & projects safely
- 🔄 Sync your local Todoist data with the cloud
- 🔁 Transfer tasks or projects to other destinations

---

## 🚀 Commands

| Command Aliases       | Description                                                                                       |
|----------------------|---------------------------------------------------------------------------------------------------|
| `b`, `backup`        | 💾 Creates a backup of a single task, project, or everything. Saves it in your chosen format & path. |
| `s`, `sync`          | 🔄 Synchronizes your local Todoist data with the cloud.                                          |
| `t`, `trans`, `transfer` | 🔀 Transfers a task or project to a specified destination.                                     |
| `st`, `set-token`    | 🔑 Sets your API token to enable access.                                                        |
| `lp`, `proj`, `projects` | 📁 Lists all available projects.                                                               |
| `lt`, `tasks`        | 📋 Lists all tasks in a project or across projects.                                             |

---

## ⚙️ Usage Examples

```bash
# Backup everything in JSON format to a folder. Can also do CSV and XLSX.
py -m todoistbackup backup all json ./backups
py -m todoistbackup backup task 123 json ./backups

# Sync your local data with Todoist cloud.
py -m todoistbackup sync

# Transfer a task with id 123 from proj A (ID: A123) to proj B (ID: B123).
py -m todoistbackup transfer task 123 A123 B123

# Transfer entire project with ID 123 from one account to another using the API token of the other account.
py -m todoistbackup transfer project 123 YOUR_API_TOKEN

# Set your API token.
py -m todoistbackup set-token YOUR_API_TOKEN

# List all projects.
py -m todoistbackup projects

# List tasks in a project.
py -m todoistbackup tasks PROJECT_ID project
```

---

## 📦 Installation

First:
```bash
git clone https://github.com/denivic/TodoistBackup
```

Then:
```bash
py -m venv "TodoistBackup"
```


Finally:
```bash
.\Scripts\activate
py -m pip install -r .\requirements.txt
```
---


## 🛠️ Development

Built with:

- Python 🐍
- Typer CLI ⚡
- Colorama for beautiful terminal colors 🌈
- Custom logging for clear debug info 📝

---

## 🙏 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

[MIT License](https://github.com/denivic/TodoistBackup/blob/main/LICENSE)

---

Made with ❤️ for Todoist users.
