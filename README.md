# 🔐 Password Strength Checker

A simple open-source Python program that checks the strength of a password and provides suggestions for making it stronger.

## 📋 Features

* Checks password length
* Checks for uppercase letters
* Checks for lowercase letters
* Checks for numbers
* Checks for special characters
* Detects some repeated characters
* Detects several common passwords
* Gives a password score from 0–100
* Provides suggestions for improvement
* Does not save or transmit passwords

## 💻 Requirements

Before using this program, you need:

* Windows, macOS, or Linux
* Python 3 installed
* Git (optional)

## 📥 Installation

### Option 1 — Download from GitHub

1. Go to this GitHub repository.
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Find the downloaded ZIP file.
5. Extract the ZIP file.
6. Open the extracted `password-strength-checker` folder.

### Option 2 — Clone with Git

Open a terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/password-strength-checker.git
```

Replace `YOUR-USERNAME` with your GitHub username.

Then move into the project folder:

```bash
cd password-strength-checker
```

## ▶️ How to Run

Open a terminal inside the project folder.

Run:

```bash
python src/checker.py
```

If your computer uses `python3` instead of `python`, use:

```bash
python3 src/checker.py
```

The program will display:

```text
========================================
       PASSWORD STRENGTH CHECKER
========================================

Enter a password to check:
```

Enter a password and press **Enter**.

The program will then show your password's score, strength level, and suggestions.

## 📊 Strength Levels

The program rates passwords using these levels:

|  Score | Strength    |
| -----: | ----------- |
|   0–29 | Very Weak   |
|  30–49 | Weak        |
|  50–69 | Moderate    |
|  70–89 | Strong      |
| 90–100 | Very Strong |

## 🔒 Privacy

This project is designed to check passwords **locally on your computer**.

Passwords are not:

* Uploaded to a server
* Sent to an API
* Stored in a database
* Saved to a file

For safety, do not enter a real password that you currently use for an important account. Use an example password when testing the program.

## 📁 Project Structure

```text
password-strength-checker/
│
├── src/
│   └── checker.py
│
├── tests/
│   └── test_checker.py
│
├── README.md
├── LICENSE
└── .gitignore
```

## 🛠️ Technologies

This project currently uses:

* Python
* Regular Expressions
* Git
* GitHub

## 🚀 Future Improvements

Possible future features include:

* [did it] Improve password scoring
* [ ] Add more common-password detection
* [ ] Add a graphical user interface
* [ ] Add more automated tests
* [ ] Add a password entropy estimate
* [ ] Create a web version
* [ ] Create a Windows executable
* [ ] Improve the user interface

## 🤝 Contributing

Contributions and suggestions are welcome.

If you find a bug or have an idea for a new feature, you can create a GitHub Issue.

## 📄 License

This project is open source and available under the MIT License.
