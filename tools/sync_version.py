"""Sync top-level VERSION with Assets/branding.json.

Run this when you bump the project version to keep branding.json consistent.
"""

import json
import os
import sys


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    version_path = os.path.join(repo_root, "VERSION")
    branding_path = os.path.join(repo_root, "Assets", "branding.json")

    try:
        with open(version_path, "r", encoding="utf-8") as vf:
            version = vf.read().strip()
    except Exception as e:
        print("Could not read VERSION:", e)
        sys.exit(1)

    try:
        with open(branding_path, "r", encoding="utf-8") as bf:
            data = json.load(bf)
    except Exception as e:
        print("Could not read branding.json:", e)
        sys.exit(1)

    if data.get("version") == version:
        print("branding.json already in sync.")
        return

    data["version"] = version
    try:
        with open(branding_path, "w", encoding="utf-8") as bf:
            json.dump(data, bf, indent=4, ensure_ascii=False)
        print(f"Updated branding.json to version {version}")
    except Exception as e:
        print("Failed to update branding.json:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
