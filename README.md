# 🧪 Appium Practice Project – Android Calculator Test

This is a **practice project** to learn and experiment with **Appium automation** for Android apps.  
The test launches the built-in **calculator app** on an Android emulator and performs a basic **2 + 3** operation using Appium in Python.

---

## 🎯 What It Does

- Opens the Calculator app on an Android emulator
- Taps the digits `2` and `3` with the `+` operation
- Validates and prints the result (`5`)
- Closes the app

---

## ▶️ Demo

![Appium Calculator Demo](assets/Appium_test_calc.gif)

---

## 📁 Project Structure

```
appium_tests/
├── calculator_test.py     - where the script is
├── requirements.txt
└── assets/
    └── Appium_test_calc.gif
```

---

## 🚀 Getting Started

1. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start Appium Server**
   ```bash
   appium
   ```

3. **Launch Your Emulator** (e.g. Pixel 2)

4. **Run the Test**
   ```bash
   python calculator_test.py
   ```

---

## ⚙️ Requirements

- Python 3.10+
- Appium v2.x
- Android Emulator (Pixel 2 or similar)
- Node.js (to install Appium)
- Appium-Python-Client
- Android SDK (set `ANDROID_HOME` environment variable)

---

## 📦 Python Dependencies

```
Appium-Python-Client==3.1.1
selenium==4.20.0
```

You can install them with:
```bash
pip install -r requirements.txt
```

---

## 📌 Notes

- This is for **learning purposes** only.
- Make sure the Calculator app is present on the emulator (`com.android.calculator2`).
- If elements can't be found, try restarting the emulator or checking app package/activity.

---

