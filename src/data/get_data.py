import os
import pandas as pd

class Olist:
    def get_data():
        csv_path = os.path.join(os.path.dirname(os.getcwd()),'data','raw')
        file_names = [f for f in os.listdir(csv_path) if f.endswith('.csv')]

        key_names = []
        for f in file_names:
            if f == 'product_category_name_translation.csv':
                key_names.append('product_category_name_translation')
            else:
                key_names.append(f[6:-12])
        data = {}
        for k, f in zip(key_names, file_names):
            data[k] = pd.read_csv(os.path.join(csv_path, f))
        return data
