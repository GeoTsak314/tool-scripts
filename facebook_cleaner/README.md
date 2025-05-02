
# Facebook Cleaner

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/yourusername/facebook-cleaner)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-yellow.svg)](https://www.python.org/)

This script automates the removal of **posts**, **comments**, and **likes** from your personal Facebook profile. It supports both **English** and **Greek** versions of Facebook and offers options for date filtering and logging.

I came along with this script, because I wanted to erase all my previous FB history & just keep the messenger (with all my current friends/connections...), but Meta doesn't offer this option! They just give you the option to delete each comment/like/post seperately... 

So I came up with this script that does exactly that, but in massive automated scale & relieves you from this repetitive stupid task! (in short: it's a small tool that Meta hates to see you using it, since all their incomes are based on advertisment, which is based in turn to your FB history...)

⚠️ **IMPORTANT:** The script does not interfere with your Messenger messages or other private content.

---

## 🔧 Features

- ✅ Delete **posts**, **comments**, and **likes** from the Activity Log
- ✅ Supports **English** and **Greek** Facebook interfaces
- ✅ Set a **starting date** for deletions (e.g., only delete from 2022 onwards) -> Use carefully! 
- ✅ Optional **logging**
- ✅ Fully automated via Selenium

---

## 🖥️ Requirements

- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Install required libraries:

```bash
pip install selenium
```

---

## ▶️ Usage

1. **Download the script**:

```
facebook_cleaner.py
```

2. **Run it via terminal**:

```bash
python facebook_cleaner.py
```

3. You will be prompted to enter:

- Your Facebook email and password
- Your Facebook username (e.g., `facebook.com/john.smith` → `john.smith`)
- A start date (optional, leave blank to delete everything)
- Whether you want logging (`yes` or `no`)

---

## 🛡️ Safety

- No login data is saved
- The script does **not** delete your Messenger messages or other personal content

---

## 🪟 Build `.exe` for Windows

To run the script without needing Python installed:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Create the executable:

```bash
pyinstaller --onefile --windowed facebook_cleaner.py
```

The `.exe` file will be created in the `dist/` folder.

---

## 🤝 Contributing

Pull requests and improvement suggestions are welcome!
