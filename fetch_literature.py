import urllib.request
import json
import os
import ssl
from time import sleep

def fetch_real_papers():
    context = ssl._create_unverified_context()
    
    # We query Semantic Scholar for actual, verifiable agricultural IoT / dielectric plant papers
    query = "leaf water content dielectric OR capacitive sensor"
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit=15&fields=title,url,year,abstract,openAccessPdf,externalIds"
    
    print("Fetching verifiable papers from Semantic Scholar...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req, context=context) as response:
            data = json.loads(response.read().decode())
    except Exception as e:
        print(f"Failed to fetch from SS API: {e}")
        return
        
    papers = data.get('data', [])
    if not papers:
        print("No papers found.")
        return
        
    os.makedirs("pdf_references", exist_ok=True)
    
    matrix_lines = []
    matrix_lines.append("## 15-Paper Literature Survey Matrix (VERIFIED REAL DATA)")
    matrix_lines.append("| # | Verified Paper Title | Actual DOI / URL | Key Topic (from abstract) | Year | PDF Saved? |")
    matrix_lines.append("|---|---|---|---|---|---|")
    
    for idx, p in enumerate(papers):
        title = p.get('title', 'Unknown Title').replace("|", " ")
        year = p.get('year', 'N/A')
        
        # Link 
        link = p.get('url', '')
        if p.get('externalIds') and 'DOI' in p.get('externalIds'):
            link = f"https://doi.org/{p['externalIds']['DOI']}"
            
        # Summary attempt
        abstract = p.get('abstract', '')
        if abstract and len(abstract) > 10:
            summary = abstract[:100].replace("\n", " ") + "..."
        else:
            summary = "Abstract not provided via API."
            
        summary = summary.replace("|", "") # markdown table safety
        
        pdf_saved = "No"
        oa_pdf = p.get('openAccessPdf')
        if oa_pdf and oa_pdf.get('url'):
            pdf_url = oa_pdf['url']
            print(f"Attempting to download PDF {idx+1} for: {title[:30]}...")
            try:
                # Add proper user agent for arxiv/other repos
                pdf_req = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                with urllib.request.urlopen(pdf_req, context=context, timeout=10) as pdf_res:
                    pdf_data = pdf_res.read()
                    safe_title = "".join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
                    safe_title = safe_title[:40].replace(" ", "_")
                    pdf_path = f"pdf_references/{idx+1}_{safe_title}.pdf"
                    
                    with open(pdf_path, 'wb') as f:
                        f.write(pdf_data)
                    pdf_saved = "Yes"
                    print(f" -> Saved to {pdf_path}")
            except Exception as e:
                print(f" -> PDF download failed for {pdf_url}: {e}")
                
        matrix_lines.append(f"| {idx+1} | {title} | {link} | {summary} | {year} | {pdf_saved} |")
        sleep(0.5) # rate limit safety
        
    print("Writing to LITERATURE_SURVEY.md...")
    with open("LITERATURE_SURVEY.md", "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace the empty matrix section with the fresh data
    if "## 15-Paper Literature Survey Matrix" in content:
        parts = content.split("## 15-Paper Literature Survey Matrix")
        
        # Determine where the matrix ends (usually right before "## Gap Analysis")
        if "## Gap Analysis" in parts[1]:
            after_matrix = "## Gap Analysis" + parts[1].split("## Gap Analysis")[1]
        else:
            after_matrix = ""
            
        new_content = parts[0] + "\n".join(matrix_lines) + "\n\n" + after_matrix
        
        with open("LITERATURE_SURVEY.md", "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print("Could not find the matrix placeholder in the markdown.")
        
    print("Successfully pulled actual, verifiable literature and downloaded available PDFs.")

if __name__ == "__main__":
    fetch_real_papers()
