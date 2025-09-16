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
1. Clone repository
    ```bash
    git clone https://github.com/linstrahl/name_checker.git
    cd name_checker
    ```

2. (Optional but recommended) Create a virtual environment
   ```bash
   python -m venv env # rename 'env' as what you want
   source env/Scripts/activate
   or
   . env/Scripts/activate
   ```

3. Install dependency
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app
    ```bash
    streamlit run name_checker.py
    ```

5. Open your browser at 
    ```bash
    http://localhost:8501
    ```

# 📊 Example Output
- Summary
  - ✅ Total matches: 15
  - ❌ Total not matched: 3
- Detailed results
    ```yaml
    ✅ 1 | 123456 | ✔ Match: (Master)👉🏼 John Doe => (Input)👉🏼 John Doe
    ❗ 2 | 987654 | ❌ Does not match:
        Master     : Jane Smith
        Input      : Jane Smyth
        Similarity : 0.92
    ❌ 3 | 555555 | Michael Lee → Data not found in master file!
    ```