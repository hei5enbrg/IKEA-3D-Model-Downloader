# IKEA-3D-Model-Downloader

Python script to fetch and download a .glb (or glb_draco) 3D model referenced in an IKEA product page's HTML. Based on https://github.com/apinanaivot/IKEA-3D-Model-Download-Button.

## Usage
Run from the project directory:

```bash
python3 ikea_downloader.py "<ikea_product_url>"
```

Example:

```bash
python3 ikea_downloader.py "https://www.ikea.com/us/en/p/example-product-12345678/"
```

Downloaded file will be saved as `ikea_model_<product_id>.glb` (or `ikea_model.glb` if no ID is found).
