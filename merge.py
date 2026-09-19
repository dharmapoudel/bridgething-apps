#!/usr/bin/env python3
"""Merge Dharma's per-app Bridgething catalogs into one combined catalog.json.

Usage: python3 merge.py   (writes catalog.json in the current directory)
"""
import json, urllib.request, datetime

SOURCES = [
    "https://dharmapoudel.github.io/atlas-radio-source/catalog.v1.json",
    "https://dharmapoudel.github.io/bridgething-calendar-source/catalog.v1.json",
    "https://dharmapoudel.github.io/bridgething-block-drop-source/catalog.v1.json",
    "https://dharmapoudel.github.io/bridgething-market-pulse-source/catalog.v1.json",
    "https://dharmapoudel.github.io/bridgething-glass-overlay-source/catalog.v1.json",
    "https://dharmapoudel.github.io/bridgething-timezones-source/catalog.v1.json",
]


def fetch(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def main():
    apps = []
    for url in SOURCES:
        catalog = fetch(url)
        apps.extend(catalog.get("apps", []))
    combined = {
        "$schema": "https://apps.bridgething.com/schemas/catalog/v1.json",
        "schema": "catalog.v1",
        "updated_at": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
        "repo": {
            "name": "Dharma's Bridgething apps",
            "description": "Every Bridgething app by Dharma Poudel in one catalog.",
            "homepage": "https://github.com/dharmapoudel/bridgething-apps",
            "icon": None,
        },
        "apps": apps,
        "recommended_sources": [],
    }
    with open("catalog.json", "w") as f:
        json.dump(combined, f, indent=2)
        f.write("\n")
    print("merged %d apps: %s" % (
        len(apps),
        ", ".join("%s %s" % (a["name"], a["versions"][0]["version"]) for a in apps),
    ))


if __name__ == "__main__":
    main()
