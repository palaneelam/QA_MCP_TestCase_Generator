import json
import pandas as pd
from pathlib import Path

OUTPUT_FOLDER = "output"

def export_to_excel(ai_response):
    Path(
        OUTPUT_FOLDER
    ).mkdir(
        exist_ok=True
    )

    try:

        data = json.loads(ai_response)

        df = pd.DataFrame(data)

        output_file = (
            Path(OUTPUT_FOLDER)
            / "Generated_TestCases.xlsx"
        )

        df.to_excel(
            output_file,
            index=False
        )

        print(
            f"\nExcel Created: {output_file}"
        )

    except Exception as e:

        print(
            "\nUnable to generate Excel"
        )

        print(e)

