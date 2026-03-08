import tkinter as tk
try:
    from tkintermapview import TkinterMapView
    print("tkintermapview imported OK.")
except ImportError:
    print("Install: pip install --upgrade tkintermapview")
    exit()

root = tk.Tk()
root.title("Fixed Map Test - Rozewie Start")
root.geometry("1000x700")

map_widget = TkinterMapView(root, width=1000, height=600, corner_radius=0)
map_widget.pack(fill=tk.BOTH, expand=True)

# Explicit OSM tiles - fixes blank/loading issues [web:40]
map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png", max_zoom=19)

map_widget.set_position(54.8325, 18.3231)  # Rozewie Cape, Poland
map_widget.set_zoom(12)

def on_click(coords):
    lat, lon = coords
    print(f"Clicked ({lat:.6f}, {lon:.6f})")
    map_widget.set_marker(lat, lon, text=f"{lat:.4f}, {lon:.4f}")

map_widget.add_left_click_map_command(on_click)

root.mainloop()
print("App closed.")
