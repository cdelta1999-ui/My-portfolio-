import re

with open(r'c:\Users\Admin\Desktop\My portfolio\streamflix.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the gallery HTML
old_gallery = '''<div class="shots dashboard-gallery">
      <figure class="shot gallery-item" onclick="openLightbox(0)">
        <img src="streamflix_dashboard.png" alt="StreamFlix Dashboard 1">
        <figcaption class="cap">Overview & KPIs</figcaption>
      </figure>
      <figure class="shot gallery-item" onclick="openLightbox(1)">
        <img src="streamflix_dash_2.png" alt="StreamFlix Dashboard 2">
        <figcaption class="cap">Retention Heatmap</figcaption>
      </figure>
      <figure class="shot gallery-item" onclick="openLightbox(2)">
        <img src="streamflix_dash_3.png" alt="StreamFlix Dashboard 3">
        <figcaption class="cap">Revenue Risk Model</figcaption>
      </figure>
    </div>'''

new_gallery = '''<div class="shots dashboard-gallery" style="grid-template-columns: 1fr;">
      <figure class="shot gallery-item" onclick="openLightbox(0)">
        <img src="imp.png" alt="StreamFlix Dashboard">
        <figcaption class="cap">Executive Dashboard</figcaption>
      </figure>
    </div>'''

if old_gallery in html:
    html = html.replace(old_gallery, new_gallery)
else:
    print("WARNING: old_gallery not found")

# Replace the JS array
old_js = '''const images = [
  "streamflix_dashboard.png",
  "streamflix_dash_2.png",
  "streamflix_dash_3.png"
];'''

new_js = '''const images = [
  "imp.png"
];'''

if old_js in html:
    html = html.replace(old_js, new_js)
else:
    print("WARNING: old_js not found")

# Also hide prev/next buttons if only 1 image
js_nav_fix_old = '''<button class="lightbox-prev" onclick="changeSlide(-1)">&#10094;</button>
  <img class="lightbox-img" id="lightboxImg" src="">
  <button class="lightbox-next" onclick="changeSlide(1)">&#10095;</button>'''

js_nav_fix_new = '''<button class="lightbox-prev" onclick="changeSlide(-1)" style="display:none;">&#10094;</button>
  <img class="lightbox-img" id="lightboxImg" src="">
  <button class="lightbox-next" onclick="changeSlide(1)" style="display:none;">&#10095;</button>'''

if js_nav_fix_old in html:
    html = html.replace(js_nav_fix_old, js_nav_fix_new)
else:
    print("WARNING: js_nav_fix_old not found")

with open(r'c:\Users\Admin\Desktop\My portfolio\streamflix.html', 'w', encoding='utf-8') as f:
    f.write(html)
