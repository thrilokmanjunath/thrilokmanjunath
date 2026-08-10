import re

class ReadmeGenerator:
    def __init__(self, readme_path="README.md"):
        self.readme_path = readme_path
        with open(readme_path, "r") as f:
            self.content = f.read()

    def replace_section(self, marker_name, new_content):
        pattern = re.compile(
            r"(<!-- AUTO:START:" + marker_name + r" -->\n).*?(\n<!-- AUTO:END:" + marker_name + r" -->)",
            re.DOTALL
        )
        self.content = pattern.sub(r"\g<1>" + new_content + r"\g<2>", self.content)

    def save(self):
        with open(self.readme_path, "w") as f:
            f.write(self.content)

    def generate_activity_html(self, events):
        html = "```text\n"
        count = 0
        for event in events:
            if count >= 5: break
            etype = event.get("type", "").replace("Event", "")
            repo = event.get("repo", {}).get("name", "unknown").split("/")[-1]
            created = event.get("created_at", "")[:10]
            
            if etype in ["Push", "Create", "Watch", "Issues", "PullRequest"]:
                html += f"{created}  {etype.upper().ljust(12)} {repo}\n"
                count += 1
        html += "```"
        return html

    def generate_projects_html(self, projects):
        html = ""
        for p in projects:
            name = p.get("name")
            desc = p.get("description") or "Engineering project."
            stars = p.get("stargazers_count", 0)
            lang = p.get("language") or "Unknown"
            url = p.get("html_url")
            
            html += f"""
<div style="border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 8px; padding: 16px; margin-bottom: 16px; background-color: #0a0a0f;">
  <h3 style="margin-top: 0; color: #06b6d4;">{name}</h3>
  <p style="color: #a1a1aa; font-family: monospace; font-size: 13px;">{desc}</p>
  <p style="color: #8b5cf6; font-family: monospace; font-size: 12px;">
    {lang} • ⭐ {stars} • <a href="{url}" style="color: #d946ef; text-decoration: none;">[ SOURCE ]</a>
  </p>
</div>
"""
        return html
