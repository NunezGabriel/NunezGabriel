"""Remove the language pie chart group from the generated 3D contribution SVG."""
import re
import sys

PIE_GROUP = '<g transform="translate(40, 520)">'
G_TAGS = re.compile(r"<g\b[^>]*/>|<g[\s>]|</g>")

path = sys.argv[1]
with open(path, encoding="utf-8") as fh:
    svg = fh.read()

start = svg.find(PIE_GROUP)
if start == -1:
    print("pie chart group not found, nothing to strip")
    sys.exit(0)

depth = 0
for m in G_TAGS.finditer(svg, start):
    tag = m.group()
    if tag.endswith("/>"):
        continue
    depth += -1 if tag == "</g>" else 1
    if depth == 0:
        svg = svg[:start] + svg[m.end():]
        break

with open(path, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("pie chart removed")
