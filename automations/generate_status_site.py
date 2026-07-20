#!/usr/bin/env python3
"""Regenerates docs/index.html from MANIFEST.yaml. Run by .github/workflows/status-site.yml on every push to main."""
import yaml, html, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
manifest = yaml.safe_load((ROOT / "MANIFEST.yaml").read_text())

STATUS_COLOR = {
    "migrated": "#34d399", "partial": "#fbbf24", "drafting": "#60a5fa",
    "new": "#c084fc", "stub": "#94a3b8", "active": "#34d399", "canonical": "#34d399",
}

def esc(s):
    return html.escape(str(s)) if s is not None else ""

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

def render_group(name):
    items = groups.get(name, [])
    rows = ""
    for o in items:
        color = STATUS_COLOR.get(o.get("status", "stub"), "#94a3b8")
        note = f' <span style="color:#a5b4fc;">({esc(o["note"])})</span>' if o.get("note") else ""
        rows += f'<div style="font-size:13px;margin:4px 0;"><span style="color:{color};">&#9679;</span> {esc(o["id"])} {esc(o["title"])}{note}</div>\n'
    return rows

conflicts = "".join(
    f'<div style="font-size:12px;color:#fecaca;margin:3px 0;">{esc(c)}</div>\n'
    for c in manifest.get("open_conflicts", [])
)
blocked = "".join(
    f'<div style="font-size:12px;color:#fecaca;margin:3px 0;">{esc(b)}</div>\n'
    for b in manifest.get("blocked", [])
)

now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

panels = "".join(
    f'<div class="panel"><div style="font-size:12px;font-weight:700;color:#a5b4fc;margin-bottom:8px;">{esc(g.upper())}</div>{render_group(g)}</div>'
    for g in group_order
)

html_out = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>OperOS Method (OBOS) - Status</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {{ color-scheme: dark; }}
  body {{ margin:0; font-family: Inter, Arial, sans-serif; background:#0b1020; color:#eef2ff; line-height:1.5; padding:28px; }}
  .grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }}
  .arch {{ display:grid; grid-template-columns:repeat(5,1fr); gap:10px; margin-bottom:24px; }}
  .box {{ background:#121a33; border:1px solid #24304f; border-radius:12px; padding:10px; text-align:center; }}
  .panel {{ background:#121a33; border:1px solid #24304f; border-radius:14px; padding:14px; }}
  .legend span {{ margin-right:14px; font-size:11px; color:#a5b4fc; }}
  .conflicts {{ margin-top:20px; background:#2a1420; border:1px solid #f87171; border-radius:12px; padding:14px; }}
  @media (max-width:800px) {{ .grid, .arch {{ grid-template-columns:1fr 1fr; }} }}
</style></head>
<body>
<div style="color:#a5b4fc;text-transform:uppercase;letter-spacing:.12em;font-size:11px;font-weight:700;">antonioOperOS/OperOSAI-operos-body-of-knowledge - v{esc(manifest.get('version'))}</div>
<div style="font-size:26px;font-weight:700;margin-top:4px;">OperOS Method (OBOS)</div>
<div style="color:#dbeafe;font-size:14px;margin:4px 0 20px;max-width:640px;">{esc(manifest.get('principle'))}</div>

<div class="arch">
  <div class="box" style="border-color:#34d399;"><div style="font-size:12px;font-weight:700;">GitHub</div><div style="font-size:10px;color:#a5b4fc;">canonical - live</div></div>
  <div class="box"><div style="font-size:12px;font-weight:700;">Confluence</div><div style="font-size:10px;color:#a5b4fc;">portal - interim</div></div>
  <div class="box"><div style="font-size:12px;font-weight:700;">Jira</div><div style="font-size:10px;color:#a5b4fc;">{esc(manifest.get('jira_epic'))}</div></div>
  <div class="box" style="border-color:#f87171;"><div style="font-size:12px;font-weight:700;">Databricks</div><div style="font-size:10px;color:#a5b4fc;">brain - blocked</div></div>
  <div class="box"><div style="font-size:12px;font-weight:700;">Drive</div><div style="font-size:10px;color:#a5b4fc;">assets</div></div>
</div>

<div class="legend">
  <span>&#9679; migrated</span><span>&#9679; partial</span><span>&#9679; drafting</span><span>&#9679; new</span><span>&#9679; stub</span>
</div>
<br>

<div class="grid">
{panels}
</div>

<div class="conflicts">
  <div style="font-size:12px;font-weight:700;color:#fca5a5;margin-bottom:8px;">OPEN CONFLICTS - unresolved</div>
  {conflicts}
</div>
<div class="conflicts" style="border-color:#fbbf24;background:#2a2214;">
  <div style="font-size:12px;font-weight:700;color:#fde68a;margin-bottom:8px;">BLOCKED</div>
  {blocked}
</div>

<div style="margin-top:20px;font-size:11px;color:#64748b;">Auto-generated from MANIFEST.yaml by automations/generate_status_site.py - last built {now}</div>
</body></html>
"""

out_path = ROOT / "docs" / "index.html"
out_path.parent.mkdir(exist_ok=True)
out_path.write_text(html_out)
print(f"Wrote {out_path}")
