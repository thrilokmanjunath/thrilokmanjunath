from collections import Counter
from datetime import datetime

class RepositoryAnalyzer:
    def analyze(self, user_data, repos):
        stats = {
            "total_stars": sum(r.get("stargazers_count", 0) for r in repos),
            "total_forks": sum(r.get("forks_count", 0) for r in repos),
            "total_repos": user_data.get("public_repos", len(repos)),
            "followers": user_data.get("followers", 0)
        }
        
        langs = [r.get("language") for r in repos if r.get("language") and not r.get("fork")]
        # Get top 4 languages
        stats["primary_languages"] = dict(Counter(langs).most_common(4))
        
        # Sort repos by updated_at
        active_repos = sorted(
            [r for r in repos if not r.get("fork")],
            key=lambda x: x.get("updated_at", ""),
            reverse=True
        )
        return stats, active_repos
