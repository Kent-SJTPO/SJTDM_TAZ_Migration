from pathlib import Path
import csv
import re

search_dir = Path(r"H:\Planning\SJTDM\SJTDM (old, 2016)\Application Files")
file_pattern = "NWDST00*.S"

repo_root = Path(r"C:\Users\Kschellinger\SJTPO_Git\SJTDM_TAZ_Migration")
out_dir = repo_root / "outputs" / "script_search"
out_dir.mkdir(parents=True, exist_ok=True)

summary_csv = out_dir / "nwdst_recreational_variable_summary.csv"
detail_txt = out_dir / "nwdst_recreational_variable_hits.txt"

variables = [
    "SJRECTG",
    "SJRECTGSHORE",
    "SJRECTGACCESS",
    "SJRECTGCAS",
    "SJRECTGEVT",
    "SJRECTGCASBUS",
    "SHOREPROD",
    "SHOREATTR",
    "OVRBACPROD",
    "OVRBACATTR",
    "DAYBACPROD",
    "DAYBACATTR",
    "SWKPROD",
    "SWKATTR",
    "CACPROD",
    "CACATTR",
    "EACPROD",
    "EACATTR",
    "CBSPROD",
    "CBSATTR",
    "CVTPROD",
    "CVTATTR",
    "EVTPROD",
    "EVTATTR",
    "BAC",
    "DAC",
    "SWK",
    "SHV",
    "CA",
    "EA",
    "CBS",
    "CVT",
    "EVT",
]

filei_re = re.compile(r'FILEI\s+[^=]+=\s+"([^"]+)"', re.IGNORECASE)
fileo_re = re.compile(r'FILEO\s+[^=]+=\s+"([^"]+)"', re.IGNORECASE)
mo_re = re.compile(r'\bMO\s*=\s*([^,\n]+(?:,[^,\n]+)*)', re.IGNORECASE)
name_re = re.compile(r'\bNAME\s*=\s*([A-Z0-9_,\s]+)', re.IGNORECASE)

rows = []

with detail_txt.open("w", encoding="utf-8", errors="ignore") as detail:
    detail.write("NWDST recreational variable search\n")
    detail.write(f"Search folder: {search_dir}\n")
    detail.write(f"File pattern: {file_pattern}\n\n")

    for script_path in sorted(search_dir.glob(file_pattern)):
        try:
            text = script_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:
            print(f"Skipped {script_path}: {exc}")
            continue

        lines = text.splitlines()

        input_files = filei_re.findall(text)
        output_files = fileo_re.findall(text)
        mo_defs = mo_re.findall(text)
        name_defs = name_re.findall(text)

        script_hits = []

        for variable in variables:
            for line_number, line in enumerate(lines, start=1):
                if variable.lower() in line.lower():
                    script_hits.append((variable, line_number, line.strip()))

        if not script_hits and not input_files and not output_files:
            continue

        detail.write("\n" + "=" * 80 + "\n")
        detail.write(f"SCRIPT: {script_path}\n")
        detail.write("=" * 80 + "\n")

        detail.write("\nINPUT FILES:\n")
        for item in input_files:
            detail.write(f"  {item}\n")

        detail.write("\nOUTPUT FILES:\n")
        for item in output_files:
            detail.write(f"  {item}\n")

        detail.write("\nMO DEFINITIONS:\n")
        for item in mo_defs:
            detail.write(f"  {item.strip()}\n")

        detail.write("\nNAME DEFINITIONS:\n")
        for item in name_defs:
            detail.write(f"  {item.strip()}\n")

        detail.write("\nVARIABLE HITS:\n")
        for variable, line_number, line in script_hits:
            detail.write(f"  {variable} | Line {line_number}: {line}\n")

        rows.append({
            "script": str(script_path),
            "input_files": "; ".join(input_files),
            "output_files": "; ".join(output_files),
            "mo_definitions": "; ".join(x.strip() for x in mo_defs),
            "name_definitions": "; ".join(x.strip() for x in name_defs),
            "matched_variables": "; ".join(sorted(set(x[0] for x in script_hits))),
            "hit_count": len(script_hits),
        })

with summary_csv.open("w", newline="", encoding="utf-8") as f:
    fieldnames = [
        "script",
        "input_files",
        "output_files",
        "mo_definitions",
        "name_definitions",
        "matched_variables",
        "hit_count",
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Search complete.")
print(f"Summary CSV: {summary_csv}")
print(f"Detail TXT: {detail_txt}")
print(f"Scripts reviewed: {len(list(search_dir.glob(file_pattern)))}")
print(f"Scripts with relevant output: {len(rows)}")