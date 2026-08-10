import os

class SVGGenerator:
    def __init__(self, output_dir="assets"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def _save(self, filename, content):
        with open(os.path.join(self.output_dir, filename), "w") as f:
            f.write(content)

    def generate_telemetry_svg(self, stats):
        svg = f"""<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: #0a0a0f; }}
    .border {{ stroke: rgba(139, 92, 246, 0.3); stroke-width: 1; fill: none; }}
    .text {{ font-family: 'Courier New', monospace; fill: #a1a1aa; font-size: 14px; }}
    .title {{ font-family: 'Courier New', monospace; fill: #8b5cf6; font-size: 16px; font-weight: bold; letter-spacing: 2px; }}
    .value {{ font-family: 'Courier New', monospace; fill: #06b6d4; font-size: 24px; font-weight: bold; }}
    .glow {{ filter: drop-shadow(0 0 5px rgba(6, 182, 212, 0.5)); }}
  </style>
  <rect width="800" height="200" rx="10" class="bg border"/>
  
  <text x="30" y="40" class="title">// GITHUB TELEMETRY</text>
  
  <text x="30" y="100" class="text">REPOSITORIES</text>
  <text x="30" y="130" class="value glow">{stats.get('total_repos', 0)}</text>
  
  <text x="230" y="100" class="text">STARS</text>
  <text x="230" y="130" class="value glow">{stats.get('total_stars', 0)}</text>
  
  <text x="430" y="100" class="text">FORKS</text>
  <text x="430" y="130" class="value glow">{stats.get('total_forks', 0)}</text>
  
  <text x="630" y="100" class="text">FOLLOWERS</text>
  <text x="630" y="130" class="value glow">{stats.get('followers', 0)}</text>
</svg>"""
        self._save("telemetry.svg", svg)

    def generate_languages_svg(self, langs):
        # langs is a dict: {'Python': 5, 'Java': 2}
        total = sum(langs.values())
        if total == 0:
            total = 1
            
        svg = """<svg width="800" height="250" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg { fill: #0a0a0f; }
    .border { stroke: rgba(139, 92, 246, 0.3); stroke-width: 1; fill: none; }
    .text { font-family: 'Courier New', monospace; fill: #a1a1aa; font-size: 14px; }
    .title { font-family: 'Courier New', monospace; fill: #8b5cf6; font-size: 16px; font-weight: bold; letter-spacing: 2px; }
    .bar-bg { fill: rgba(255, 255, 255, 0.05); rx: 4; }
    .bar-fg { fill: #d946ef; rx: 4; filter: drop-shadow(0 0 5px rgba(217, 70, 239, 0.5)); }
  </style>
  <rect width="800" height="250" rx="10" class="bg border"/>
  <text x="30" y="40" class="title">// PRIMARY LANGUAGES</text>
"""
        y = 80
        for lang, count in langs.items():
            pct = count / total
            width = int(pct * 500)
            if width < 10: width = 10
            
            svg += f"""
  <text x="30" y="{y+15}" class="text">{lang}</text>
  <rect x="200" y="{y}" width="500" height="20" class="bar-bg"/>
  <rect x="200" y="{y}" width="{width}" height="20" class="bar-fg"/>
  <text x="720" y="{y+15}" class="text">{int(pct*100)}%</text>
"""
            y += 40
            
        svg += "</svg>"
        self._save("languages.svg", svg)
