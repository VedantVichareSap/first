# 🧮 Logic Calculator

A simple yet powerful calculator built with **Python** and a **Streamlit** web interface.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| ➕ Addition | Add two numbers |
| ➖ Subtraction | Subtract two numbers |
| ✖️ Multiplication | Multiply two numbers |
| ➗ Division | Divide two numbers (with zero-check) |
| 🌐 Web UI | Clean browser-based interface via Streamlit |
| ⚠️ Error Handling | Catches division by zero gracefully |

---

## 📁 Project Structure

```
project1/
│
├── 1.py        # Core calculator logic (add, subtract, multiply, divide)
├── app.py      # Streamlit web interface
└── README.md   # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/VedantVichareSap/first.git
cd first
```

### 2. Install dependencies

```bash
pip install streamlit
```

### 3. Run the web app

```bash
streamlit run app.py
```

Then open your browser at **http://localhost:8501**

---

## 🖥️ Web Interface Preview

```
┌─────────────────────────────────────────────┐
│           🧮  Calculator                     │
│                                             │
│  ┌──────────┐  ┌────────┐  ┌──────────┐    │
│  │  First   │  │  Op    │  │  Second  │    │
│  │   10     │  │   +    │  │    5     │    │
│  └──────────┘  └────────┘  └──────────┘    │
│                                             │
│         [ Calculate ]                       │
│                                             │
│   ✅  Result: 10 + 5 = 15                  │
└─────────────────────────────────────────────┘
```

---

## 🧪 How It Works

1. Enter the **first number**
2. Select an **operator** (`+`, `-`, `*`, `/`)
3. Enter the **second number**
4. Click **Calculate**
5. The result appears instantly below

---

## 🛠️ Built With

- ![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
- ![Streamlit](https://img.shields.io/badge/Streamlit-1.50-red?logo=streamlit&logoColor=white)

---

## 👤 Author

**Vedant Vichare**  
GitHub: [@VedantVichareSap](https://github.com/VedantVichareSap)
