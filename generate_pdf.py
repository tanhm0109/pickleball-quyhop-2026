import markdown
from weasyprint import HTML, CSS
import os

CSS_STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap');

body {
    font-family: 'Noto Sans', Arial, sans-serif;
    font-size: 13px;
    line-height: 1.6;
    color: #222;
    margin: 0;
    padding: 0;
}
@page {
    margin: 2cm 2.2cm;
    @bottom-right {
        content: counter(page);
        font-size: 11px;
        color: #888;
    }
}
h1 { font-size: 20px; color: #1a5276; border-bottom: 2px solid #1a5276; padding-bottom: 6px; margin-top: 0; }
h2 { font-size: 16px; color: #1f618d; margin-top: 24px; page-break-before: always; break-before: page; }
h2:first-of-type { page-break-before: auto; break-before: auto; }
h3 { font-size: 14px; color: #2471a3; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 12px; page-break-inside: avoid; break-inside: avoid; }
th { background: #1f618d; color: white; padding: 7px 10px; text-align: left; }
td { padding: 6px 10px; border: 1px solid #d5d8dc; }
tr:nth-child(even) td { background: #f2f3f4; }
code { background: #f0f0f0; padding: 1px 4px; border-radius: 3px; font-size: 11px; }
pre { background: #f0f0f0; padding: 10px; border-radius: 4px; font-size: 11px; overflow-x: auto; }
blockquote { border-left: 3px solid #1f618d; margin: 8px 0; padding: 4px 12px; color: #555; background: #eaf2ff; }
hr { border: none; border-top: 1px solid #d5d8dc; margin: 16px 0; }
ul, ol { padding-left: 20px; }
li { margin: 3px 0; }
strong { color: #1a5276; }
em { color: #555; }
"""

files = [
    ("CLAUDE.md", "pdf/00-tong-quan-du-an.pdf"),
    ("docs/01-ke-hoach-trien-khai.md", "pdf/01-ke-hoach-trien-khai.pdf"),
    ("docs/02-bang-phan-cong-btc.md", "pdf/02-bang-phan-cong-btc.pdf"),
    ("docs/03-thong-bao-giai-dau.md", "pdf/03-thong-bao-giai-dau.pdf"),
]

os.makedirs("pdf", exist_ok=True)

md = markdown.Markdown(extensions=["tables", "fenced_code"])

for src, dst in files:
    with open(src, encoding="utf-8") as f:
        content = f.read()
    html_body = md.convert(content)
    md.reset()
    html = f"<html><head><meta charset='utf-8'></head><body>{html_body}</body></html>"
    HTML(string=html).write_pdf(dst, stylesheets=[CSS(string=CSS_STYLE)])
    print(f"✅ {dst}")

print("Xong!")
