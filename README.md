# 🚗 MOTORS: Vehicle Management System

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/YOUR_GITHUB_USERNAME/MOTORS.svg?style=social)](https://github.com/YOUR_GITHUB_USERNAME/MOTORS/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/YOUR_GITHUB_USERNAME/MOTORS.svg?style=social)](https://github.com/YOUR_GITHUB_USERNAME/MOTORS/network/members)

---

## ✨ Overview

**MOTORS** is a robust, modular Python project designed to manage vehicle-related operations, serving as a simplified car sales application through a Command-Line Interface (CLI). The core strength of this project lies in its recent architectural overhaul (Refactoring) to adhere strictly to **Clean Code** principles and **Separation of Concerns** using dedicated Python packages.

---

## 🚀 Key Features

* **Vehicle Browsing:** Display and search the catalog of available vehicles.
* **Shopping Cart Management:** Core logic for adding, removing, and viewing items in the user's cart.
* **Favorites List:** Functionality to maintain a user-specific list of preferred vehicles.
* **User Data Persistence:** Secure handling of user and feedback data.
* **Modular Architecture:** Organized into distinct packages for logic, processing, and data access.

---

## 🏗️ Project Architecture (Post-Refactoring)

The project structure is now organized into specialized packages, ensuring maximum clarity and maintainability. 

| Package/Folder | Responsibility | Description |
| :--- | :--- | :--- |
| `main_program.py` | Entry Point | Application startup and main feature loop. |
| `data_files/` | Data Storage | Isolated folder for all raw persistence files (`.txt`, to be migrated to `.json` later). |
| `data_access/` | Repository Layer | Manages all read/write operations for data files (e.g., `user_repo.py`, `cart_repo.py`). **Knows WHERE the data is.** |
| `user_cart_logic/` | Cart Business Logic | Contains functions related to cart addition, removal, and state management. |
| `vehicle_processing/` | Vehicle Logic | Handles pricing calculations, searching, and filtering of vehicle data. |
| `user_interface/` | Presentation Layer | Handles all user interaction, including prompts, input (`input()`), and output (`print()`). |

---

## ⚙️ Setup and Installation

### Prerequisites

* Python 3.x installed on your system.

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/MOTORS.git](https://github.com/YOUR_GITHUB_USERNAME/MOTORS.git)
    cd MOTORS
    ```

2.  **Install dependencies:**
    *(This project primarily uses the Python standard library, making dependency installation minimal.)*

---

## ▶️ How to Run

Since the project uses internal packages, running the application requires specifying the project root directory using the `PYTHONPATH` environment variable to allow Python to find all packages (e.g., `user_cart_logic`).

| Operating System | Command |
| :--- | :--- |
| **Linux/macOS** | `PYTHONPATH=. python main_program.py` |
| **Windows (PowerShell)** | `$env:PYTHONPATH='.'; python main_program.py` |
| **Windows (Command Prompt / CMD)** | `set PYTHONPATH=. & python main_program.py` |

---

## 🧪 Code Quality

This project is committed to high code quality, achieving a high score on **Pylint** metrics by enforcing PEP 8 standards and minimizing code smells.

---

## 🤝 Contributing

We welcome contributions! If you have suggestions for improvements, bug fixes, or enhancements to the current modular design, please feel free to:

1.  Open an Issue to discuss proposed changes.
2.  Submit a Pull Request with your implementation.

---

## 📄 License

This project is licensed under the **MIT License**.

### Author

* **[Elias]** - *Initial Development and Complete Architectural Refactoring*