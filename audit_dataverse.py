import urllib.request
import json
import ssl
import pandas as pd
import os

context = ssl._create_unverified_context()

queries = {
    'Tomato Proxy': 'tomato water stress',
    'Chili/Capsicum Proxy': 'chili water stress',
    'Coconut Proxy': 'coconut water stress',
    'Sap Flow Proxy': 'sap flow dataset'
}

print('=== HARVARD DATAVERSE DATASET VERIFICATION AUDIT ===\n')

for label, q in queries.items():
    print(f'Querying Dataverse for: {label} ({q})')
    url = f'https://dataverse.harvard.edu/api/search?q={urllib.parse.quote(q)}&type=file'
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=context) as response:
            data = json.loads(response.read().decode())
    except Exception as e:
        print(f'Failed to query Dataverse: {e}\n')
        continue
        
    items = data.get('data', {}).get('items', [])
    if not items:
        print('-> RESULT: No dataset file found.\n')
        continue
        
    found_file = False
    for item in items:
        if found_file: break
        
        file_name = item.get('name', '')
        file_id = item.get('file_id', '')
        url_source = item.get('url', 'No URL')
        download_url = f'https://dataverse.harvard.edu/api/access/datafile/{file_id}'
        
        if file_name.endswith('.csv') or file_name.endswith('.txt') or file_name.endswith('.tab'):
            print(f'-> Found target file: {file_name}')
            print(f'-> Source URL: {url_source}')
            
            try:
                req_dl = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req_dl, context=context) as f_res:
                    with open(file_name, 'wb') as out_f:
                        out_f.write(f_res.read())
                
                size = os.path.getsize(file_name)
                print(f'-> File Size: {size} bytes')
                
                sep = ',' if file_name.endswith('.csv') else '\t'
                df = pd.read_csv(file_name, sep=sep, on_bad_lines='skip')
                
                print(f'-> Total Rows: {len(df)}')
                print(f'-> Top 3 Rows:')
                print(df.head(3).to_string())
                print('\n')
                
                found_file = True
                os.remove(file_name)
            except Exception as e:
                print(f'-> Failed to parse file: {e}\n')
                
    if not found_file:
         print('-> RESULT: No viable CSV dataset found in hits.\n')
