import re

with open(r'c:\Users\Admin\Desktop\My portfolio\global-warfare.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the hero image with an iframe
old_img_wrap = '<div class="hero-img-wrap">\n      <img src="global_warfare_dashboard.png" alt="Global Warfare Analysis Dashboard">\n    </div>'
new_img_wrap = '<div class="hero-img-wrap" style="height: 650px; display: flex; flex-direction: column;">\n      <iframe src="dashboard/index.html" style="width: 100%; height: 100%; border: none; flex: 1;"></iframe>\n    </div>'

html = html.replace(old_img_wrap, new_img_wrap)

# Also let's handle if it was already modified or had different spacing:
if new_img_wrap not in html:
    # try regex
    html = re.sub(
        r'<div class="hero-img-wrap">\s*<img src="global_warfare_dashboard\.png" alt="Global Warfare Analysis Dashboard">\s*</div>',
        new_img_wrap,
        html
    )

with open(r'c:\Users\Admin\Desktop\My portfolio\global-warfare.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Patched global-warfare.html")
