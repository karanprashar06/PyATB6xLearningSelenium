# Selenium 4 with Python – Web Automation

This repository contains **Selenium 4 web automation examples and notes using Python**, focused on modern Selenium practices, clean test design, and real‑world automation scenarios.

It is suitable for **QA Engineers, Automation Testers, and Beginners** who want to learn or strengthen their Selenium 4 skills.

---

## 🚀 Tech Stack

* **Python 3.x**
* **Selenium 4.x**
* **PyTest** – Test execution framework
* **Allure Report** – Test reporting
* **Chrome Browser** (can be extended to Firefox, Edge)

---

## 📂 Project Structure (Sample)

```
project-root/
│
├── tests/              # Test cases
├── pages/              # Page Object Model (POM) classes
├── utils/              # Utilities (waits, helpers)
├── reports/            # Allure reports output
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ✅ Key Concepts Covered

* Selenium 4 WebDriver setup
* Locating elements (ID, Name, XPath, CSS)
* Browser navigation & window handling
* Wait strategies (Implicit & Explicit waits)
* Page Object Model (POM)
* PyTest test execution
* Allure reporting integration
* Debugging & best practices

---

## ▶️ How to Run Tests

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Tests Using PyTest

```bash
pytest
```

### 3. Run a Specific Test File

```bash
pytest test_selenium.py
```

### 4. Generate Allure Report

```bash
pytest --alluredir=reports
allure serve reports
```

---

## 🧪 Example Test

```python
from selenium import webdriver

def test_open_website():
    driver = webdriver.Chrome()
    driver.get("https://thetestingacademy.com")
    assert "The Testing Academy" in driver.title
    driver.quit()
```

---

## 📌 Best Practices

* Always close the browser using `driver.quit()`
* Avoid hard waits (`sleep`) in real frameworks
* Use explicit waits for stability
* Follow Page Object Model for scalability
* Keep tests independent and readable

---

## 👤 Author

**Karan Prashar**
QA Automation Engineer
Specialized in Selenium, API Automation, PyTest & Test Framework Design

---

## 📄 License

This project is for **learning and educational purposes**.

