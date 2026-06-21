import re

with open(r'c:\Users\Admin\Desktop\My portfolio\global-warfare.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the typo in the hero image
html = html.replace('global-warfare-dashboard.png', 'global_warfare_dashboard.png')

gallery_html = '''
    <section>
      <h2>Analysis &amp; Intelligence Dashboards</h2>
      <p>Detailed views of the Wound Vulnerability Index (WVI) and geopolitical forecasts.</p>
      <div class="shots dashboard-gallery">
        <figure class="shot gallery-item" onclick="openLightbox(0)">
          <img src="global_warfare_dashboard.png" alt="Global Warfare Dashboard">
          <figcaption class="cap">Command Overview</figcaption>
        </figure>
        <figure class="shot gallery-item" onclick="openLightbox(1)">
          <img src="WVI2.PNG" alt="WVI Assessment">
          <figcaption class="cap">WVI Assessment</figcaption>
        </figure>
        <figure class="shot gallery-item" onclick="openLightbox(2)">
          <img src="WVI_Analysis.PNG" alt="WVI Analysis">
          <figcaption class="cap">WVI Analysis Breakdown</figcaption>
        </figure>
      </div>
    </section>
'''

# Add CSS for the gallery and lightbox
css_to_add = '''
.dashboard-gallery { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 30px; }
.gallery-item { cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; }
.gallery-item:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(124,92,255,0.3); }
.gallery-item img { width: 100%; height: auto; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); }
@media(max-width: 900px) { .dashboard-gallery { grid-template-columns: 1fr; } }
.lightbox { position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 2000; display: flex; align-items: center; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.3s; backdrop-filter: blur(10px); }
.lightbox.open { opacity: 1; pointer-events: auto; }
.lightbox-close { position: absolute; top: 20px; right: 30px; font-size: 50px; color: white; cursor: pointer; background: none; border: none; }
.lightbox-prev, .lightbox-next { position: absolute; top: 50%; transform: translateY(-50%); font-size: 40px; color: white; cursor: pointer; background: rgba(255,255,255,0.1); border: none; padding: 20px; border-radius: 50%; backdrop-filter: blur(5px); }
.lightbox-prev { left: 30px; }
.lightbox-next { right: 30px; }
.lightbox-prev:hover, .lightbox-next:hover { background: rgba(124,92,255,0.5); }
.lightbox-img { max-width: 85%; max-height: 85vh; border-radius: 12px; box-shadow: 0 20px 50px rgba(0,0,0,0.8); transition: opacity 0.3s, transform 0.3s; }
</style>
'''

html = html.replace('</style>', css_to_add, 1) # Only replace the first one (in <head>)

# Add the gallery section before </main>
html = html.replace('</main>', gallery_html + '\n  </main>')

# Add JS for lightbox at the end
js_to_add = '''
<div class="lightbox" id="lightbox">
  <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
  <button class="lightbox-prev" onclick="changeSlide(-1)">&#10094;</button>
  <img class="lightbox-img" id="lightboxImg" src="">
  <button class="lightbox-next" onclick="changeSlide(1)">&#10095;</button>
</div>
<script>
const images = [
  "global_warfare_dashboard.png",
  "WVI2.PNG",
  "WVI_Analysis.PNG"
];
let currentIdx = 0;
const lb = document.getElementById('lightbox');
const lbImg = document.getElementById('lightboxImg');

function openLightbox(idx) {
  currentIdx = idx;
  lbImg.src = images[currentIdx];
  lb.classList.add('open');
}
function closeLightbox() {
  lb.classList.remove('open');
}
function changeSlide(dir) {
  currentIdx += dir;
  if (currentIdx < 0) currentIdx = images.length - 1;
  if (currentIdx >= images.length) currentIdx = 0;
  lbImg.style.opacity = 0;
  lbImg.style.transform = 'scale(0.95)';
  setTimeout(() => {
    lbImg.src = images[currentIdx];
    lbImg.style.opacity = 1;
    lbImg.style.transform = 'scale(1)';
  }, 200);
}
</script>
</body>
'''

html = html.replace('</body>', js_to_add)

with open(r'c:\Users\Admin\Desktop\My portfolio\global-warfare.html', 'w', encoding='utf-8') as f:
    f.write(html)
