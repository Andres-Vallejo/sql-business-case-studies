from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sample_data.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def main() -> None:
    df = pd.read_csv(DATA_PATH)
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    text_cols = [c for c in df.columns if c not in numeric_cols]
    summary = df[numeric_cols].agg(["count", "sum", "mean", "min", "max"]).T.round(2)
    summary.to_csv(OUTPUT_DIR / "numeric_summary.csv")
    if text_cols and numeric_cols:
        grouped = df.groupby(text_cols[0])[numeric_cols].sum(numeric_only=True).reset_index()
        grouped.to_csv(OUTPUT_DIR / "grouped_summary.csv", index=False)
        ax = grouped.sort_values(numeric_cols[0], ascending=False).plot(kind="bar", x=text_cols[0], y=numeric_cols[0], legend=False, figsize=(8, 4))
        ax.set_title(f"{numeric_cols[0]} by {text_cols[0]}")
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / "summary_chart.png", dpi=160)
    print("Analysis complete. Outputs written to outputs/.")
    print(summary)

if __name__ == "__main__":
    main()
