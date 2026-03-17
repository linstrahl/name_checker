# MetaTrader Name Match Checker

**Name Match Checker** is a Streamlit-based application used to match trading account Login and Name data against the master data from MetaTrader 5 (MT5). This application helps users easily verify whether the entered account data matches the official data in the master CSV file.

# ✨ Key Features

- 📤 Upload the MT5 master trading accounts file in CSV format.
- 📝 Input account data manually using the format:
    ```bash
    number login name
    ```

    Example:
    ```bash
    1 123456 John Doe
    2 987654 Jane Smith
    ```

- 🔎 Automatic matching between input and master file:
  -  ✔ Match → input name exactly matches the master file.
  -  ❌ Not Match → mismatch is detected, with a similarity score as reference.
  -  🚫 Data not found → login ID is missing from the master file.

- 📑 Summary of results:
  - Total matches
  - Total mismatches
  - List of detailed comparison results


# 🚀 How to Run

## Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/linstrahl/name-checker.git
cd name-checker
```

### 2. Create a Virtual Environment (Recommended)

#### Windows
```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
env\Scripts\activate
```

#### Linux / macOS
```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
source env/bin/activate
```

### 3. Install Dependencies

#### Windows
```bash
# Make sure your virtual environment is activated, then run:
pip install -r requirements.txt
```

#### Linux / macOS
```bash
# Make sure your virtual environment is activated, then run:
pip3 install -r requirements.txt
```

### 4. Run the Application

#### Windows
```bash
streamlit run name_checker.py
```

#### Linux / macOS
```bash
streamlit run name_checker.py
```

### 5. Access the Application
Open your web browser and navigate to:
```
http://localhost:8501
```

## Troubleshooting

**Windows users:** If you encounter issues activating the virtual environment, try:
```bash
. env/Scripts/activate
```

**Linux/macOS users:** If you get a permission error, ensure the activate script is executable:
```bash
chmod +x env/bin/activate
```

# 📊 Example Output

### Summary
```
✅ Total matches: 15
❌ Total not matched: 3
```

### Detailed Results
```
✅ 1 | 123456 | ✔ Match: (Master)👉🏼 John Doe => (Input)👉🏼 John Doe
❗ 2 | 987654 | ❌ Does not match:
    Master     : Jane Smith
    Input      : Jane Smyth
    Similarity : 0.92
❌ 3 | 555555 | Michael Lee → Data not found in master file!
```

# 📝 License

This project is open source and available under the MIT License.
