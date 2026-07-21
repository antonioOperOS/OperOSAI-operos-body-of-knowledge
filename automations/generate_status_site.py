#!/usr/bin/env python3
"""Regenerates docs/index.html from MANIFEST.yaml + build-in-public-log.md. Run by .github/workflows/status-site.yml on every relevant push."""
import yaml, html, pathlib, datetime, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
manifest = yaml.safe_load((ROOT / "MANIFEST.yaml").read_text())

REPO_BLOB = "https://github.com/antonioOperOS/OperOSAI-operos-body-of-knowledge/blob/main/"
REPO_TREE = "https://github.com/antonioOperOS/OperOSAI-operos-body-of-knowledge/tree/main/"
DRIVE_URL = "https://drive.google.com/drive/folders/0AG6QZiEVwppOUk9PVA"
LOG_URL = REPO_BLOB + "automations/build-in-public-log.md"

STATUS_ORDER = ["canonical", "migrated", "active", "partial", "drafting", "new", "stub"]
STATUS_COLOR = {
    "canonical": "#facc15", "migrated": "#34d399", "active": "#2dd4bf",
    "partial": "#fbbf24", "drafting": "#60a5fa", "new": "#c084fc", "stub": "#94a3b8",
}
STATUS_LABEL = {s: s for s in STATUS_ORDER}

def esc(s):
    return html.escape(str(s)) if s is not None else ""

def obj_url(o):
    path = o.get("path")
    if not path:
        return None
    return (REPO_TREE if path.endswith("/") else REPO_BLOB) + path

def group_key(obj_id: str) -> str:
    if obj_id.startswith("SYS") or obj_id == "CONCEPT-RoT":
        return "Governance / Core"
    if obj_id.startswith("FW-001"):
        return "FW-001 Strategy (expanded)"
    if obj_id.startswith("FW-"):
        return "FW-002 - FW-008"
    if obj_id in ("SALES-001", "ASMT-001", "PLAY-001", "GTM-001"):
        return "GTM-adjacent"
    if obj_id in ("CERT-001", "PROOF-001", "REL-001", "ARCH-001"):
        return "Proof / Release / Arch"
    return "Templates & Automations"

groups = {}
for obj in manifest.get("objects", []):
    groups.setdefault(group_key(obj["id"]), []).append(obj)

group_order = ["Governance / Core", "FW-001 Strategy (expanded)", "FW-002 - FW-008",
               "GTM-adjacent", "Proof / Release / Arch", "Templates & Automations"]

def dot(status):
    return f'<span class="dot" style="background:{STATUS_COLOR.get(status, "#94a3b8")};"></span>'

def render_group(name):
    items = groups.get(name, [])
    rows = ""
    for o in items:
        status = o.get("status", "stub")
        note = f' <span style="color:#a5b4fc;">({esc(o["note"])})</span>' if o.get("note") else ""
        label = f'{esc(o["id"])} {esc(o["title"])}'
        url = obj_url(o)
        if url:
            label = f'<a href="{esc(url)}" target="_blank" rel="noopener" style="color:inherit;text-decoration:none;border-bottom:1px dotted #475569;">{label}</a>'
        rows += f'<div style="font-size:13px;margin:5px 0;display:flex;align-items:flex-start;gap:7px;">{dot(status)}<span>{label}{note}</span></div>\n'
    return rows

conflicts = "".join(f'<div style="font-size:12px;color:#fecaca;margin:3px 0;">{esc(c)}</div>\n' for c in manifest.get("open_conflicts", []))
blocked = "".join(f'<div style="font-size:12px;color:#fecaca;margin:3px 0;">{esc(b)}</div>\n' for b in manifest.get("blocked", []))

# --- Parse the build-in-public log into dated entries ---
log_path = ROOT / "automations" / "build-in-public-log.md"
entries = []
if log_path.exists():
    text = log_path.read_text()
    # Split on level-2 headings that look like "## YYYY-MM-DD — Title"
    parts = re.split(r'(?m)^## (\d{4}-\d{2}-\d{2}) — (.+)$', text)
    # parts alternates: [preamble, date, title, body, date, title, body, ...]
    for i in range(1, len(parts), 3):
        date, title, body = parts[i], parts[i + 1], parts[i + 2]
        m = re.search(r'\*\*Milestone:\*\*\s*(.+?)(?:\n\n|\Z)', body, re.S)
        milestone = m.group(1).strip().replace("\n", " ") if m else ""
        entries.append((date, title.strip(), milestone))
entries.sort(key=lambda e: e[0], reverse=True)

def render_bip_entries(entries):
    if not entries:
        return '<div style="font-size:13px;color:#a5b4fc;">No entries yet.</div>'
    rows = ""
    for date, title, milestone in entries[:8]:
        rows += f'''<div style="margin:0 0 14px;padding-bottom:14px;border-bottom:1px solid #24304f;">
  <div style="font-size:11px;color:#a5b4fc;text-transform:uppercase;letter-spacing:.08em;font-weight:700;">{esc(date)}</div>
  <div style="font-size:14px;font-weight:700;margin:2px 0 4px;">{esc(title)}</div>
  <div style="font-size:13px;color:#dbeafe;">{esc(milestone)}</div>
</div>\n'''
    return rows

now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

panels = "".join(
    f'<div class="panel"><div style="font-size:12px;font-weight:700;color:#a5b4fc;margin-bottom:8px;">{esc(g.upper())}</div>{render_group(g)}</div>'
    for g in group_order
)

legend = "".join(
    f'<span class="legend-chip"><span class="dot" style="background:{STATUS_COLOR[s]};"></span>{STATUS_LABEL[s]}</span>'
    for s in STATUS_ORDER
)

REPO_ROOT = "https://github.com/antonioOperOS/OperOSAI-operos-body-of-knowledge"
CONFLUENCE_URL = "https://operos.atlassian.net/wiki/spaces/TLAC"
JIRA_URL = f"https://operos.atlassian.net/browse/{manifest.get('jira_epic')}"

html_out = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>OperOS Method (OBOS) - Status</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {{ color-scheme: dark; }}
  body {{ margin:0; font-family: Inter, Arial, sans-serif; background:#0b1020; color:#eef2ff; line-height:1.5; padding:28px; }}
  a {{ color: inherit; }}
  .dot {{ display:inline-block; width:9px; height:9px; border-radius:50%; flex:0 0 auto; margin-top:4px; }}
  .grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }}
  .arch {{ display:grid; grid-template-columns:repeat(5,1fr); gap:10px; margin-bottom:20px; }}
  .box {{ background:#121a33; border:1px solid #24304f; border-radius:12px; padding:10px; text-align:center; display:block; text-decoration:none; transition:border-color .15s; }}
  .box:hover {{ border-color:#60a5fa; }}
  .panel {{ background:#121a33; border:1px solid #24304f; border-radius:14px; padding:14px; }}
  .legend {{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:20px; }}
  .legend-chip {{ display:inline-flex; align-items:center; gap:6px; font-size:11px; color:#dbeafe; background:#121a33; border:1px solid #24304f; border-radius:999px; padding:4px 10px; }}
  .legend-chip .dot {{ margin-top:0; }}
  .conflicts {{ margin-top:20px; background:#2a1420; border:1px solid #f87171; border-radius:12px; padding:14px; }}
  .bip {{ margin-top:24px; background:#121a33; border:1px solid #facc15; border-radius:14px; padding:16px; }}
  .bip a.hdr {{ text-decoration:none; color:inherit; }}
  .panel a:hover {{ color:#93c5fd; border-bottom-color:#93c5fd !important; }}
  @media (max-width:800px) {{ .grid, .arch {{ grid-template-columns:1fr 1fr; }} }}
</style></head>
<body>
<div style="color:#a5b4fc;text-transform:uppercase;letter-spacing:.12em;font-size:11px;font-weight:700;">
  <a href="{REPO_ROOT}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit;">antonioOperOS/OperOSAI-operos-body-of-knowledge</a> - v{esc(manifest.get('version'))}
</div>
<div style="font-size:26px;font-weight:700;margin-top:4px;">OperOS Method (OBOS)</div>
<div style="color:#dbeafe;font-size:14px;margin:4px 0 20px;max-width:640px;">{esc(manifest.get('principle'))}</div>

<div class="arch">
  <a class="box" href="{REPO_ROOT}" target="_blank" rel="noopener" style="border-color:#34d399;"><div style="font-size:12px;font-weight:700;">GitHub</div><div style="font-size:10px;color:#a5b4fc;">canonical - live</div></a>
  <a class="box" href="{CONFLUENCE_URL}" target="_blank" rel="noopener" style="border-color:#a78bfa;"><div style="font-size:12px;font-weight:700;">Confluence</div><div style="font-size:10px;color:#a5b4fc;">portal - interim</div></a>
  <a class="box" href="{JIRA_URL}" target="_blank" rel="noopener" style="border-color:#f97316;"><div style="font-size:12px;font-weight:700;">Jira</div><div style="font-size:10px;color:#a5b4fc;">{esc(manifest.get('jira_epic'))}</div></a>
  <div class="box" style="border-color:#f87171;cursor:default;"><div style="font-size:12px;font-weight:700;">Databricks</div><div style="font-size:10px;color:#a5b4fc;">brain - blocked</div></div>
  <a class="box" href="{DRIVE_URL}" target="_blank" rel="noopener" style="border-color:#38bdf8;"><div style="font-size:12px;font-weight:700;">Drive</div><div style="font-size:10px;color:#a5b4fc;">assets</div></a>
</div>

<div class="legend">{legend}</div>

<div class="grid">
{panels}
</div>

<div class="bip">
  <a class="hdr" href="{LOG_URL}" target="_blank" rel="noopener">
    <div style="font-size:12px;font-weight:700;color:#fde68a;margin-bottom:12px;">&#128225; BUILD IN PUBLIC LOG &rarr; full drafts (3 voices) on GitHub</div>
  </a>
  {render_bip_entries(entries)}
</div>

<div class="conflicts">
  <div style="font-size:12px;font-weight:700;color:#fca5a5;margin-bottom:8px;">OPEN CONFLICTS - unresolved</div>
  {conflicts}
</div>
<div class="conflicts" style="border-color:#fbbf24;background:#2a2214;">
  <div style="font-size:12px;font-weight:700;color:#fde68a;margin-bottom:8px;">BLOCKED</div>
  {blocked}
</div>

<div style="margin-top:20px;font-size:11px;color:#64748b;">Auto-generated from MANIFEST.yaml and build-in-public-log.md by automations/generate_status_site.py - last built {now}. Click any item to open it.</div>
</body></html>
"""

out_path = ROOT / "docs" / "index.html"
out_path.parent.mkdir(exist_ok=True)
out_path.write_text(html_out)
print(f"Wrote {out_path}, {len(entries)} build-in-public entries parsed")
