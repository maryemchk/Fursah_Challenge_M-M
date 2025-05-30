import pandas as pd
from pathlib import Path
import re

def merge_scenario_a(root_dir: str):
    """
    Merge all CSVs under *root_dir* and add a 'window_s' column
    extracted from the filename (e.g., 15s, 30s, 60s…).

    Parameters
    ----------
    root_dir : str
        Path to the Scenario-A directory that contains the CSV files
        (e.g., 'data/Scenario A1-ARFF').
    """
    root = Path(root_dir)
    csv_paths = list(root.rglob("*.csv"))
    if not csv_paths:
        raise FileNotFoundError(f"No CSVs found under {root}")

    frames = []
    for csv_path in csv_paths:
        # Extract the first number followed by 's' in the stem
        m = re.search(r"(\d+)s", csv_path.stem)
        if m is None:
            raise ValueError(f"Can't parse time window from {csv_path.name}")
        window = int(m.group(1))

        df = pd.read_csv(csv_path)
        df["window_s"] = window          # add the new column
        frames.append(df)

        print(f"Loaded {csv_path.name:40}  ➜ {len(df):6,d} rows")

    merged = pd.concat(frames, ignore_index=True)
    out_path = root / "scenarioA_merged.csv"
    merged.to_csv(out_path, index=False)
    print(f"\n✅  Merged dataset saved to: {out_path}  ({len(merged):,d} rows)")

if __name__ == "__main__":
    merge_scenario_a("data/Scenario A1-ARFF")   # <— adjust this path if needed
