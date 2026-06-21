import re

with open('c:\\Users\\Admin\\Desktop\\My portfolio\\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the Experience section
html = re.sub(r'<section class=\"section on-img\" id=\"experience\">.*?</section>', '', html, flags=re.DOTALL)

# 2. Remove the Feature article (Salifort)
html = re.sub(r'<article class=\"feature reveal\">.*?</article>', '', html, flags=re.DOTALL)

# 3. Add Salifort to proj-grid
salifort_card = '''
      <a href="salifort.html" class="card reveal">
        <div class="swatch" style="background:linear-gradient(135deg, #7C5CFF, #CC52DE);">SM</div>
        <div class="cstatus"><div class="d"></div>Live Project</div>
        <h3>Salifort Motors</h3>
        <p>Predicting Employee Attrition. An ML system flagging at-risk employees with 0.97 AUC, turning each prediction into a concrete HR retention action.</p>
        <div class="cfoot"><span>Read case study &#8599;</span></div>
      </a>
'''
html = html.replace('<div class="proj-grid">', '<div class="proj-grid">' + salifort_card)

# 4. Shorten About section
about_original = r'''<div class="about-body">
      <p>An <b>M.Sc. and B.Sc. in Geography</b> trained me to make sense of complex, interconnected systems &mdash; turning messy spatial, demographic, and behavioral data into structured insight. That discipline now drives how I work in product: defining the right metrics, mapping the real user journey, and turning observation into strategy.</p>
      <p>As <b>founder of Manastej</b>, an AI platform uniting mental wellness and education, I built the product end to end &mdash; sharpening product strategy, user-journey mapping, and metric definition. I decide not just what to measure, but which numbers actually move outcomes.</p>
      <a class="manastej-link" href="https://www.manastej.com" target="_blank" rel="noopener">Visit manastej.com &#8599;</a>
    </div>'''
about_short = '''<div class="about-body">
      <p>I combine my background in geography with data science to map complex user journeys and predict behaviors. As founder of Manastej, I build AI systems that move real business outcomes.</p>
      <a class="manastej-link" href="https://www.manastej.com" target="_blank" rel="noopener">Visit manastej.com &#8599;</a>
    </div>'''
html = html.replace(about_original, about_short)

# 5. Remove the Nav link for Experience
html = html.replace('<a href="#experience">Experience</a>', '')

with open('c:\\Users\\Admin\\Desktop\\My portfolio\\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
