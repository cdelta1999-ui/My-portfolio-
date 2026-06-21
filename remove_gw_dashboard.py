import re

with open(r'c:\Users\Admin\Desktop\My portfolio\global-warfare.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove from gallery
old_gallery_figure = '''<figure class="shot gallery-item" onclick="openLightbox(0)">
          <img src="global_warfare_dashboard.png" alt="Global Warfare Dashboard">
          <figcaption class="cap">Command Overview</figcaption>
        </figure>'''
if old_gallery_figure in html:
    html = html.replace(old_gallery_figure, '')
else:
    print("Warning: gallery figure not found")

# 2. Update the onclick indices for the remaining images
html = html.replace('onclick="openLightbox(1)"', 'onclick="openLightbox(0)"')
html = html.replace('onclick="openLightbox(2)"', 'onclick="openLightbox(1)"')

# 3. Update the CSS grid to 2 columns instead of 3 since we have 2 images now
html = html.replace('.dashboard-gallery { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 30px; }', 
                    '.dashboard-gallery { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 30px; }')

# 4. Update JS array
old_js_array = '''const images = [
  "global_warfare_dashboard.png",
  "WVI2.PNG",
  "WVI_Analysis.PNG"
];'''
new_js_array = '''const images = [
  "WVI2.PNG",
  "WVI_Analysis.PNG"
];'''
if old_js_array in html:
    html = html.replace(old_js_array, new_js_array)
else:
    print("Warning: js array not found")

with open(r'c:\Users\Admin\Desktop\My portfolio\global-warfare.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replacement complete.")
