import pytest
from scripts.repository_analyzer import RepositoryAnalyzer
from scripts.project_ranker import ProjectRanker

def test_repository_analyzer():
    user_data = {"public_repos": 2, "followers": 10}
    repos = [
        {"name": "A", "language": "Python", "stargazers_count": 5, "forks_count": 1},
        {"name": "B", "language": "Java", "stargazers_count": 10, "forks_count": 2, "fork": False},
        {"name": "C", "language": "Python", "fork": True} # Fork should be ignored for languages
    ]
    
    analyzer = RepositoryAnalyzer()
    stats, active = analyzer.analyze(user_data, repos)
    
    assert stats["total_stars"] == 15
    assert stats["total_forks"] == 3
    assert stats["followers"] == 10
    assert "Python" in stats["primary_languages"]
    assert "Java" in stats["primary_languages"]

def test_project_ranker():
    repos = [
        {"name": "Minor", "stargazers_count": 1, "description": "test"},
        {"name": "Major", "stargazers_count": 10, "description": "test", "has_pages": True},
        {"name": "Boosted", "stargazers_count": 0}
    ]
    
    ranker = ProjectRanker(featured_overrides=["Boosted"])
    ranked = ranker.rank_projects(repos)
    
    # Boosted should be first because of the 100 points
    assert ranked[0]["name"] == "Boosted"
    # Major should be second (10*2 + 5 + 5 = 30)
    assert ranked[1]["name"] == "Major"
    # Minor should be third (1*2 + 5 = 7)
    assert ranked[2]["name"] == "Minor"
