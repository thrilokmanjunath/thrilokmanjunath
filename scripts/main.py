import sys
from datetime import datetime, timezone
from github_client import GitHubClient
from repository_analyzer import RepositoryAnalyzer
from project_ranker import ProjectRanker
from svg_generator import SVGGenerator
from readme_generator import ReadmeGenerator

def main():
    username = "thrilokmanjunath"
    
    # 1. Fetch data
    client = GitHubClient()
    user_data = client.get_user_data(username)
    if not user_data:
        print("Failed to fetch user data. Exiting.")
        sys.exit(1)
        
    repos = client.get_repos(username)
    events = client.get_events(username)
    
    # 2. Analyze
    analyzer = RepositoryAnalyzer()
    stats, active_repos = analyzer.analyze(user_data, repos)
    
    ranker = ProjectRanker(featured_overrides=["SynStream-AI", "PaperGraph", "Eyes-on-Tigers", "github-achievement-lab"])
    featured_projects = ranker.rank_projects(active_repos)
    
    # 3. Generate SVGs
    svg_gen = SVGGenerator(output_dir="../assets")
    svg_gen.generate_telemetry_svg(stats)
    svg_gen.generate_languages_svg(stats.get("primary_languages", {}))
    
    # 4. Generate README Content
    readme = ReadmeGenerator(readme_path="../README.md")
    
    # System Status
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    status_html = f"""```text
● GITHUB API              ONLINE
● PROFILE ENGINE          ONLINE
● PROJECT SCANNER         ONLINE
● ACTIVITY STREAM         ONLINE
● README GENERATOR        ONLINE

LAST SYNC: {now}
REPOSITORIES MONITORED: {stats.get('total_repos')}
```"""
    readme.replace_section("STATUS", status_html)
    
    # Telemetry
    readme.replace_section("TELEMETRY", '<div align="center">\n<img src="./assets/telemetry.svg" alt="GitHub Telemetry" />\n</div>')
    
    # Tech Matrix (Languages SVG)
    readme.replace_section("TECHMATRIX", '<div align="center">\n<img src="./assets/languages.svg" alt="Primary Languages" />\n</div>')
    
    # Activity
    activity_html = readme.generate_activity_html(events)
    readme.replace_section("ACTIVITY", activity_html)
    
    # Projects
    projects_html = readme.generate_projects_html(featured_projects)
    readme.replace_section("PROJECTS", projects_html)
    
    # Metrics
    # Can combine or use existing SVGs. We will just use placeholders or skip if not needed
    readme.replace_section("METRICS", "*(Engineering metrics integrated into Telemetry)*")
    
    # Save
    readme.save()
    print("Profile successfully updated.")

if __name__ == "__main__":
    main()
