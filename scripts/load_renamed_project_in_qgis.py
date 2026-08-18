"""
load_renamed_project_in_qgis.py
Instructs the running QGIS instance to load the project from the renamed GeoPackage.
"""

import socket
import struct
import json
import time

GPKG_PATH = r"F:/Antigravity/Hydrosheds and Basins/india_master_water_and_geospatial_atlas.gpkg"
PORT = 9877

def main():
    qgis_code = r"""
from qgis.core import QgsProject
from qgis.utils import iface

gpkg = "F:/Antigravity/Hydrosheds and Basins/india_master_water_and_geospatial_atlas.gpkg"
uri = f"geopackage:{gpkg}?projectName=India_Master_Hydrology_and_Infrastructure"

print(f"Reading project from: {uri}")
res = QgsProject.instance().read(uri)
print(f"Project Read Result: {res}")

if iface:
    iface.mapCanvas().refresh()
    print("Map canvas refreshed!")

layer_count = len(QgsProject.instance().mapLayers())
print(f"Total Active Layers in Canvas: {layer_count}")
"""

    print("Connecting to QGIS via port 9877...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(15)
        s.connect(("127.0.0.1", PORT))
        
        payload = json.dumps({"type": "execute_code", "params": {"code": qgis_code}}).encode("utf-8")
        s.sendall(struct.pack(">I", len(payload)) + payload)

        raw_len = s.recv(4)
        msg_len = struct.unpack(">I", raw_len)[0]
        buf = b""
        while len(buf) < msg_len:
            buf += s.recv(min(4096, msg_len - len(buf)))
        s.close()
        res = json.loads(buf.decode("utf-8"))
        print(res.get("result", {}).get("stdout", res))
    except Exception as e:
        print(f"Socket connection error: {e}")

if __name__ == "__main__":
    main()
