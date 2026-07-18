import pandas as pd
import numpy as np
from pyvalet import ValetInterpreter

def data_frame_display_config():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', None)

def main():
    data_frame_display_config()

    vi = ValetInterpreter()
    series_df = vi.list_series()
    print(series_df[["name", "description"]])

    return 0


if __name__ == '__main__':
    main()
