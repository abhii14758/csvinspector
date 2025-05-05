# run_inspector.py

import sys
from csvinspector.inspector import CSVInspector

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_inspector.py <path_to_csv_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    inspector = CSVInspector(file_path)
    inspector.run_analysis()

