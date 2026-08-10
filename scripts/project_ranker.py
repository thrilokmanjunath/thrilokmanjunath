class ProjectRanker:
    def __init__(self, featured_overrides=None):
        self.featured_overrides = featured_overrides or []

    def rank_projects(self, repos):
        # Filter out forks
        repos = [r for r in repos if not r.get("fork")]
        
        for r in repos:
            score = 0
            score += r.get("stargazers_count", 0) * 2
            score += r.get("forks_count", 0) * 1
            if r.get("description"):
                score += 5
            if r.get("has_pages"):
                score += 5
            
            # Boost specific projects based on name
            if r.get("name") in self.featured_overrides:
                score += 100
                
            r["_score"] = score
            
        ranked = sorted(repos, key=lambda x: x["_score"], reverse=True)
        return ranked[:4] # Top 4 projects
