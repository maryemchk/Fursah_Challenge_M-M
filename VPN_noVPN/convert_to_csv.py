import os
import pandas as pd

def fix_and_convert_arff(arff_path, csv_path):
    with open(arff_path, "r") as f:
        lines = f.readlines()

    # Find @DATA section
    data_start = next(i for i, line in enumerate(lines) if line.strip().startswith("@DATA"))

    # Extract attribute names
    attributes = []
    for line in lines:
        if line.strip().lower().startswith("@attribute"):
            name = line.strip().split()[1]
            attributes.append(name)

    # Extract data lines
    data_lines = lines[data_start + 1:]
    data_lines = [line.strip() for line in data_lines if line.strip()]

    # Write to CSV
    df = pd.DataFrame([row.split(",") for row in data_lines], columns=attributes)
    df.to_csv(csv_path, index=False)
    print(f"✅ Converted: {arff_path} -> {csv_path}")

def convert_all_arffs(input_dir="data"):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".arff"):
                arff_path = os.path.join(root, file)
                csv_path = os.path.splitext(arff_path)[0] + ".csv"
                try:
                    fix_and_convert_arff(arff_path, csv_path)
                except Exception as e:
                    print(f"❌ Failed: {arff_path} — {e}")

if __name__ == "__main__":
    convert_all_arffs("data")
