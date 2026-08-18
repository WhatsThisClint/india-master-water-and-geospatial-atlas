"""
dump_all_qgis_layers.py
Dumps all layer names (vectors and rasters) and properties in QGIS.
"""

import socket
import struct
import json

PORT = 9877

def main():
    qgis_code = r"""
from qgis.core import QgsProject, QgsWkbTypes

project = QgsProject.instance()
root = project.layerTreeRoot()

lines = []
for l in project.mapLayers().values():
    node = root.findLayer(l.id())
    chk = node.itemVisibilityChecked() if node else "None"
    rend = type(l.renderer()).__name__ if l.renderer() else "None"
    if l.type() == 0: # Vector
        wkb = QgsWkbTypes.displayString(l.wkbType())
        lines.append(f"[Vector] {l.name()} | Features: {l.featureCount()} | WKB: {wkb} | Renderer: {rend} | Checked: {chk}")
    elif l.type() == 1: # Raster
        lines.append(f"[Raster] {l.name()} | Provider: {l.dataProvider().name()} | Renderer: {rend} | Checked: {chk}")

with open("F:/Antigravity/Hydrosheds and Basins/all_qgis_layers_dump.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
"""
    payload = json.dumps({"type": "execute_code", "params": {"code": qgis_code}}).encode("utf-8")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(15)
    s.connect(("127.0.0.1", PORT))
    s.sendall(struct.pack(">I", len(payload)) + payload)

    raw_len = s.recv(4)
    msg_len = struct.unpack(">I", raw_len)[0]
    buf = b""
    while len(buf) < msg_len:
        buf += s.recv(min(4096, msg_len - len(buf)))
    s.close()

if __name__ == "__main__":
    main()
