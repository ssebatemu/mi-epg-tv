import json
import xml.etree.ElementTree as ET
from datetime import datetime

# Leer el archivo JSON que guardaste
with open("guia.json", "r", encoding="utf-8") as f:
    guia_json = json.load(f)

root = ET.Element("tv", date=datetime.now().strftime("%Y%m%d"))
channel_id = guia_json["channel"].lower().replace(" ", "_")

channel_el = ET.SubElement(root, "channel", id=channel_id)
ET.SubElement(channel_el, "display-name").text = guia_json["channel"]

for p in guia_json["programmes"]:
    start_time = p["start"].replace("-", "").replace(":", "").replace("T", " ")[:-3] + "00"
    stop_time = p["stop"].replace("-", "").replace(":", "").replace("T", " ")[:-3] + "00"

    prog_el = ET.SubElement(root, "programme", start=start_time, stop=stop_time, channel=channel_id)
    ET.SubElement(prog_el, "title", lang="es").text = p["title"]
    if p["subtitle"]:
        ET.SubElement(prog_el, "sub-title", lang="es").text = p["subtitle"]
    ET.SubElement(prog_el, "desc", lang="es").text = p["desc"]
    ET.SubElement(prog_el, "category", lang="es").text = p["category"]
    ET.SubElement(prog_el, "icon", src=p["icon"])

tree = ET.ElementTree(root)
tree.write("guia_tv.xml", encoding="utf-8", xml_declaration=True)
