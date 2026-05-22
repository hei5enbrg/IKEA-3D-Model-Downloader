import sys
import re
import urllib.request
import os

def download_ikea_model(product_url):
    print(f"Fetching: {product_url}")
    
    # Headers to mimic a real browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        # Fetch the IKEA product page
        req = urllib.request.Request(product_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
        # Search for .glb or glb_draco URLs in the source code
        glb_urls = re.findall(r'(https?://[^\s"\']*?\.glb)', html)
        glb_draco_urls = re.findall(r'(https?://[^\s"\']*?glb_draco[^\s"\']*)', html)
        
        all_urls = list(set(glb_urls + glb_draco_urls))
        
        if not all_urls:
            print("No 3D model found on this page.")
            print("Note: If the model relies entirely on JavaScript to load, consider using Selenium.")
            return
            
        target_url = all_urls[0]
        print(f"Found model URL: {target_url}")
        
        # Extract product ID for the filename
        product_id = ""
        id_match = re.search(r'/p/.*?(\d+)/?', product_url)
        if id_match:
            product_id = id_match.group(1)
            
        filename = f"ikea_model_{product_id}.glb" if product_id else "ikea_model.glb"
        
        print(f"Downloading to {filename}...")
        
        # Download the model
        model_req = urllib.request.Request(target_url, headers=headers)
        with urllib.request.urlopen(model_req) as m_res, open(filename, 'wb') as out_file:
            out_file.write(m_res.read())
            
        print("Download complete!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ikea_downloader.py <ikea_product_url>")
        sys.exit(1)
        
    download_ikea_model(sys.argv[1])