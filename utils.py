def get_job_keywords(role):
    job_keywords = {
        "Software Engineer": ["Python", "Java", "Git", "APIs", "OOP", "Data Structures", "SQL", "Agile"],
        "Machine Learning Engineer": ["Python", "TensorFlow", "scikit-learn", "Pandas", "Numpy", "Regression", "Neural Networks"],
        "Mechanical Engineer": ["SolidWorks", "AutoCAD", "Thermodynamics", "ANSYS", "MATLAB", "Manufacturing", "CAD", "CAM"],
        "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Responsive Design", "Frontend", "Backend"]
    }
    return job_keywords.get(role, [])

def suggest_improvements(text, expected_keywords, found_keywords):
    missing = [kw for kw in expected_keywords if kw not in found_keywords]
    suggestions = []
    for kw in missing:
        suggestions.append(f"Consider adding your experience with '{kw}' if applicable.")
    return suggestions
