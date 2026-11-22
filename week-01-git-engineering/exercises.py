"""Week 0: Python Fundamentals Bootcamp — Beginner Practice Tasks."""

import csv
import json
from typing import Dict, List, Tuple, Any


def evaluate_attendance_status(attended: int, total: int) -> str:
    """Return 'ELIGIBLE' (>=75%), 'WARNING' (65% to <75%), or 'SHORTAGE' (<65%).
    If total <= 0, return 'NO_SESSIONS'.
    """
    if(total <= 0):
        return "NO_SESSIONS"
    
    att = (attended/total)*100

    if( att >= 75):
        return "ELIGIBLE";
    elif(att >= 65 and att < 75):
        return "WARNING"
    else:
        return "SHORTAGE"
    # raise NotImplementedError("Task 1a: Implement evaluate_attendance_status")


def safe_parse_float(raw_value: Any, default: float = 0.0) -> float:
    """Convert raw_value to float safely using try/except. Return default on failure."""
    
    try:
        return float(raw_value)
    except(ValueError,TypeError):
        return default
    # raise NotImplementedError("Task 1b: Implement safe_parse_float")


def analyze_pod_scores(records: List[Tuple[str, str, float]]) -> Dict[str, Any]:
    """Analyze (usn, pod_name, score) tuples using sets, dicts, and comprehensions.

    Returns a dictionary with keys:
      - 'unique_student_count': int (number of unique USNs via set)
      - 'high_scorers': List[str] (USNs with score >= 80 using a list comprehension)
      - 'pod_averages': Dict[str, float] (average score per pod rounded to 2 decimals)
    """
    u_usn = set()
    for usn ,pod_name, score in records:
        u_usn.add(usn)
    
    high_scorers = [
        usn for usn, pod_name, score in records if score >= 80
    ]

    pod_scores = {}

    for usn, pod_name, score in records:
        if pod_name not in pod_scores:
            pod_scores[pod_name] = []

        pod_scores[pod_name].append(score)
    
    pod_avg = {}

    for pod_name, score in pod_scores.items():
        pod_avg[pod_name] = round(sum(score) / len(score), 2)

    return {
    "unique_student_count": len(u_usn),
    "high_scorers": high_scorers,
    "pod_averages": pod_avg,
    }

    # raise NotImplementedError("Task 2: Implement analyze_pod_scores")


def summarize_csv_to_json(csv_path: str, json_path: str) -> Dict[str, Any]:
    """Read cohort CSV using built-in csv module and export summary JSON.

    Summary dictionary must contain:
      - 'total_students': int
      - 'branches': List[str] (sorted unique branch codes)
      - 'average_score': float (rounded to 2 decimals)
    """
    students = []
    with open(csv_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    total_students = len(students)

    branches = sorted({row["branch"] for row in students})

    if total_students > 0:
        total_score = sum(float(row["score"]) for row in students)
        average_score = round(total_score / total_students, 2)
    else:
        average_score = 0.0

    summary = {
        "total_students": total_students,
        "branches": branches,
        "average_score": average_score,
    }

    with open(json_path, "w") as out_file:
        json.dump(summary, out_file, indent=4)

    return summary
    # raise NotImplementedError("Task 3: Implement summarize_csv_to_json")


class StudentRecord:
    """Tracks weekly evaluation scores for a single DSC recruit."""

    def __init__(self, usn: str, name: str):
        """Initialize record with uppercase USN, name, and empty scores list."""
        self.usn = usn.upper()
        self.name = name
        self.scores: List[float] = []

    def add_score(self, score: float) -> None:
        """Append a score (must be between 0 and 100; raise ValueError otherwise)."""
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")
        self.scores.append(score)

    def average(self) -> float:
        """Return average score rounded to 2 decimals, or 0.0 if no scores exist."""
        if not self.scores:
            return 0.0
        return round(sum(self.scores) / len(self.scores), 2)

    def is_passing(self, threshold: float = 50.0) -> bool:
        """Return True if average() >= threshold, else False."""
        return self.average() >= threshold