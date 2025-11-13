# 🚗 Motors: CLI E-Commerce Simulation

### A complex procedural Python project demonstrating advanced data structure management for a simulated vehicle e-commerce platform.

This project, developed using a procedural (pre-functional) approach, simulates the core logic of an e-commerce website's backend. It manages a complex, nested inventory of vehicles, user authentication, a persistent shopping cart, and dynamic data filtering, all within a single command-line interface.

## ✨ Key Features Implemented

* **Complex Inventory Database:** Utilizes nested Python Dictionaries to model a multi-level vehicle database (e.g., `Vehicles > Cars > Sport > Ferrari`).
* **User Authentication & Sign-In:** A simple system to differentiate between registered users (like `Yasseen`) and new guests, including a basic sign-in process.
* **Full Shopping Cart:** Complete cart management, allowing users to **Add**, **Remove**, **Clear**, and **Calculate Total Price** of items in their cart.
* **Advanced Price Filtering:** A feature to browse and sort vehicles based on specific price ranges (e.g., "Under $50,000", "Under $100,000").
* **Favourite List:** Allows users to add and manage a separate list of their "favourite" vehicles.
* **Profile Management:** Users can update their personal information (Email, Address, Phone).

## 🛠️ Technical Skills & Concepts Demonstrated

This project showcases a strong grasp of intermediate Python concepts, even without the use of functions:

| Skill / Concept | Description |
| :--- | :--- |
| **Advanced Data Structures** | **(Skill Highlight)** Using complex nested Dictionaries and Lists to manage application state and inventory. |
| **State Management** | Managing the state of `Cart` and `favourite` lists dynamically throughout the user session. |
| **Complex Loop Logic** | Heavy use of nested `while` and `for` loops to iterate through deep data structures (e.g., searching for items, calculating prices). |
| **String & Input Handling** | Extensive use of `.strip()`, `.capitalize()`, and tuple-based validation (e.g., `Agree`, `rejection`) for robust user input. |
| **Procedural Programming** | Demonstrates the ability to build a feature-rich application using a single, continuous execution loop. |

## 🚀 Getting Started

1.  Download the main Python file (`motors.py`).
2.  Run the application using: `python motors.py`
3.  Log in using the email: `User12345@gmail.com` to test the full features.

## 💡 Future Development (Next Steps)

This project is the perfect candidate for refactoring. The immediate next steps are:

1.  **Modularity (Refactoring):** Break down the single `while` loop into dedicated functions (e.g., `def handle_login()`, `def manage_cart()`, `def display_price_list()`) to make the code clean, readable, and maintainable.
2.  **Data Persistence:** Use File Handling (like in the "Digital Contacts Manager" project) to save the `Cart` and `user_info` to a file, so data isn't lost when the program closes.
3.  **Error Handling:** Implement `try/except` blocks to prevent crashes (e.g., if a user enters text instead of a number).