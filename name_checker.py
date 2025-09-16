import streamlit as sl
import pandas as pd
import difflib
import io

sl.set_page_config(layout="wide")
sl.title("🔍 Name Match Checker")

uploaded_file = sl.file_uploader("📄 Upload trading accounts master file from MT5 in CSV format", type=["csv"])
input_text = sl.text_area("📝 Input accounts data (format: number login name)", height=300)

if sl.button("🔎 Check Data"):
    if uploaded_file and input_text:
        df = None
        raw_bytes = uploaded_file.read() # Read the entire file content as bytes

        try: # Try reading the file as UTF-16 with ';' delimiter and skip the first row
            decoded = raw_bytes.decode("utf-16")
            df = pd.read_csv(io.StringIO(decoded), delimiter=";", skiprows=1, usecols=["Login", "Name"])
        except Exception as e:
            sl.error("❌ Unable to read master CSV file.")
            sl.text(f"Failed to decode with utf-16: {e}")

        if df is not None:
            df['Login'] = df['Login'].astype(str).str.strip()
            df['Name'] = df['Name'].astype(str).str.strip()

            master_dict = dict(zip(df['Login'], df['Name']))

            sl.subheader("📑 Results Summary")

            results = []
            non_matching_results = []
            match_count = 0
            non_match_count = 0

            for line in input_text.strip().splitlines():
                parts = line.strip().split()
                if len(parts) < 3:
                    continue

                number = parts[0]
                login = parts[1]
                input_name = " ".join(parts[2:]).strip()

                if login in master_dict:
                    master_name = master_dict[login].strip()
                    
                    # Strict comparison: must be identical
                    if input_name == master_name:
                        match_count += 1
                        result = f"✅ {number} | {login} | ✔ Match: (Master)👉🏼 {master_name} => (Input)👉🏼 {input_name}"
                    else:
                        similarity = difflib.SequenceMatcher(None, master_name, input_name).ratio() # Show similarity score as a reference
                        result = (
                            f"❗ {number} | {login} | ❌ Does not match:\n"
                            f"    Master     : {master_name}\n"
                            f"    Input      : {input_name}\n"
                            f"    Similarity : {similarity:.2f}"
                        )
                        non_match_count += 1
                        non_matching_results.append(f"{number} {login}")
                else:
                    non_match_count += 1
                    result = f"❌ {number} | {login} | {input_name} → Data not found in master file!"
                    non_matching_results.append(f"{number} {login}")

                results.append(result)

            # Show result summary
            sl.success(f"✅ Total matches: {match_count}")
            sl.error(f"❌ Total not matched: {non_match_count}")

            # Show only non-matching results
            if non_matching_results:
                sl.subheader("❌ All Non-Matching Results")
                sl.code("\n".join(non_matching_results), language="text")

            # Show all matching and non-matching results
            sl.subheader("📋 All Matching Results")
            sl.code("\n".join(results), language="text")
    else:
        sl.warning("⚠️ Make sure the master CSV file is uploaded and the input data is not empty before pressing the button.")
