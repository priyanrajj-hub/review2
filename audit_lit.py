import urllib.request
import urllib.parse
import json
import os
import ssl
import re

def get_sentences(text, n=2):
    if not text: return "No abstract available."
    text = text.replace('\n', ' ').strip()
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return ' '.join(sentences[:n])

def run():
    context = ssl._create_unverified_context()
    os.makedirs('pdf_references', exist_ok=True)
    
    q = '("leaf capacitance" OR "plant bioimpedance" OR "leaf dielectric" OR "stem water potential" OR "crop water stress index" OR "dendrometer") AND ("water stress" OR drought OR moisture)'
    url = f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&format=json&resultType=core&pageSize=20'
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=context) as response:
            data = json.loads(response.read().decode())
    except Exception as e:
        print("API failed:", e)
        return

    results = []
    
    for item in data.get('resultList', {}).get('result', []):
        doi = item.get('doi', 'No DOI')
        title = item.get('title', 'Unknown Title')
        abstract = item.get('abstractText', '')
        year = item.get('pubYear', 'Unknown')
        authors = item.get('authorString', 'Unknown Authors')
        source_url = f"https://doi.org/{doi}" if doi != 'No DOI' else item.get('url', 'No URL')
        
        pdf_url = None
        # Check for open access full text PDF in EuropePMC
        pmcid = item.get('pmcid')
        if pmcid:
            pdf_url = f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf"
            
        pdf_saved = False
        file_size = 0
        failed = False
        
        if pdf_url:
            safe_title = "".join([c for c in title if c.isalnum()]).replace(" ", "_")[:30]
            pdf_path = f"pdf_references/{safe_title}_{pmcid}.pdf"
            try:
                pdfr = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(pdfr, context=context, timeout=15) as pres:
                    with open(pdf_path, 'wb') as f:
                        f.write(pres.read())
                file_size = os.path.getsize(pdf_path)
                # check if it downloaded a real pdf (usually > 10kb)
                if file_size > 10000:
                    pdf_saved = True
                else:
                    failed = True
                    os.remove(pdf_path)
            except Exception:
                failed = True
                
        results.append({
            'doi': doi,
            'title': title,
            'authors': authors,
            'year': year,
            'url': source_url,
            'pdf_url': pdf_url,
            'pdf_saved': pdf_saved,
            'failed_download': failed,
            'file_size': file_size,
            'abstract_first_2': get_sentences(abstract, 2),
            'abstract_full': abstract
        })

    with open('literature_raw_data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
        
    print(f"Total processed: {len(results)}")
    
if __name__ == '__main__':
    run()
