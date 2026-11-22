"""
fetch_metadata.py — System & Environment Diagnostic Script
Data Science Club (DSC KLE) — Sprint Challenge Week 1

Instructions for Recruits:
1. Fill in your personal student metadata variables below.
2. Complete the collect_environment_metadata() function.
3. Run this script via: `python src/fetch_metadata.py`
"""

import sys
import os
import platform
from datetime import datetime, timezone
import json

# ==============================================================================
# RECRUIT METADATA (Fill these in with your real details)
# ==============================================================================
STUDENT_USN = "01FE25BCS417"        
STUDENT_NAME = "Vinayak_Dombarakoppa"    
BRANCH = "CSE"                      
TRACK = "CREDIT_TRACK_YEAR2"        


def collect_environment_metadata() -> dict:
    """
    Collects runtime diagnostic metadata from the host environment.
    
    Returns:
        dict: Diagnostic details including python version, OS platform,
              active virtualenv status, and ISO timestamp.
    """
    # Check if currently executing inside a virtual environment
    is_in_venv = (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )

    metadata = {
        "student": {
            "usn": STUDENT_USN.strip().upper(),
            "name": STUDENT_NAME.strip(),
            "branch": BRANCH.strip(),
            "track": TRACK.strip()
        },
        "environment": {
            "python_version": sys.version.split()[0],
            "python_executable": sys.executable,
            "os_platform": platform.platform(),
            "architecture": platform.machine(),
            "in_virtualenv": is_in_venv,
            "timestamp_utc": datetime.now(timezone.utc).isoformat()
        }
    }
    return metadata


def main():
    print("=" * 60)
    print("DSC KLE — Week 1 Environment Verification")
    print("=" * 60)

    data = collect_environment_metadata()

    # Validation guard for recruit details
    if "XXXX" in data["student"]["usn"] or data["student"]["name"] == "XYZ":
        print("\n⚠️ WARNING: Please update STUDENT_USN and STUDENT_NAME in src/fetch_metadata.py!")
    else:
        print(f"\n[OK] Registered to: {data['student']['name']} ({data['student']['usn']})")

    print(f"[OK] Python: {data['environment']['python_version']} on {data['environment']['os_platform']}")
    print(f"[OK] Virtual Environment Active: {data['environment']['in_virtualenv']}")
    print("\nFull System Metadata Payload:")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
