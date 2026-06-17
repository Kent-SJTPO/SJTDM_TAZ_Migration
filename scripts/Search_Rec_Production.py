from pathlib import Path
import csv

search_root = Path(r"H:\Planning\SJTDM")
repo_root = Path(r"C:\Users\Kschellinger\SJTPO_Git\SJTDM_TAZ_Migration")
out_dir = repo_root / "outputs" / "script_search"
out_dir.mkdir(parents=True, exist_ok=True)

summary_csv = out_dir / "recreational_keyword_summary.csv"
detail_txt = out_dir / "recreational_keyword_hits.txt"

keywords = [
    "CACPROD", "CACATTR", "CVTPROD", "CVTATTR",
    "EACPROD", "EACATTR", "EVTPROD", "EVTATTR",
    "CBSPROD", "CBSATTR",
    "BAC", "BCH", "BWK", "SWK", "CAC", "CVT", "EAC", "EVT", "CBS",
    "SJMREC", "SJRECTG", "EQUIV",
    "BEACHZONE", "COMBRDWLK", "NCOMBRDWLK", "COMMERCIAL",
    "CASINOPCT", "CROOM", "CFLOOR", "CSEATS", "CEMPL",
    "AC_AREA", "TOWNNUMBER", "REGIONCODE",
    "FirstBchZone", "LastBchZone",
    "FirstCasZone", "LastCasZone",
    "FirstEvtZone", "LastEvtZone",
    "LastACzone",
    "CASINO", "SHORE", "BEACH", "BOARDWALK", "ATLANTIC CITY"
]

extensions = {
    ".s", ".job", ".ctl", ".txt", ".csv", ".prn",
    ".xml", ".ini", ".bat", ".cmd"
}

results = []

with detail_txt.open("w", encoding="utf-8", errors="ignore") as detail:
    detail.write("SJTDM recreational reference search\n")
    detail.write(f"Search root: {search_root}\n\n")

    for file_path in search_root.rglob("*"):
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in extensions:
            continue

        try:
            lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception as exc:
            print(f"Skipped: {file_path} ({exc})")
            continue

        for keyword in keywords:
            hits = []
            keyword_lower = keyword.lower()

            for line_number, line in enumerate(lines, start=1):
                if keyword_lower in line.lower():
                    hits.append((line_number, line.strip()))

            if hits:
                results.append({
                    "keyword": keyword,
                    "file": str(file_path),
                    "hits": len(hits)
                })

                detail.write("\n" + "=" * 70 + "\n")
                detail.write(f"KEYWORD: {keyword}\n")
                detail.write(f"FILE: {file_path}\n")
                detail.write(f"HITS: {len(hits)}\n")
                detail.write("=" * 70 + "\n")

                for line_number, line in hits:
                    detail.write(f"Line {line_number}: {line}\n")

with summary_csv.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["keyword", "file", "hits"])
    writer.writeheader()
    writer.writerows(results)

print("Search complete.")
print(f"Summary CSV: {summary_csv}")
print(f"Details TXT: {detail_txt}")
print(f"Total keyword/file matches: {len(results)}")