import folium

# =====================
# 1. 基本参数
# =====================

# 亭林园中心
CENTER_LAT = 31.392806
CENTER_LON = 120.944707

# =====================
# 2. 创建地图（MapTiler 底图）
# =====================
m = folium.Map(
    location=[CENTER_LAT, CENTER_LON],
    zoom_start=16,
    tiles=None  # 重要：不用默认 OSM
)

# MapTiler 底图
folium.TileLayer(
    tiles=f"https://www.maptiler.com/maps/#style=streets-v4&lang=auto&mode=2d&position=15.83/31.392806/120.944707",
    attr="© MapTiler © OpenStreetMap contributors",
    name="MapTiler Streets"
).add_to(m)

# =====================
# 3. 景点数据（点是主角）
# =====================
spots = [
    {
        "name": "顾炎武纪念馆",
        "lat": 31.3931,
        "lon": 120.9444,
        "desc": "纪念明末清初思想家顾炎武，是亭林园的核心文化建筑。"
    },
    {
        "name": "玉峰书院",
        "lat": 31.3925,
        "lon": 120.9452,
        "desc": "园内重要的历史书院空间，体现昆山文脉。"
    },
    {
        "name": "亭林祠",
        "lat": 31.3929,
        "lon": 120.9439,
        "desc": "纪念亭林先生的重要场所，具有仪式性与纪念性。"
    }
]

# =====================
# 4. 添加 Marker + Popup Card
# =====================
for spot in spots:
    popup_html = f"""
    <div style="width:200px">
        <h4>{spot['name']}</h4>
        <p style="font-size:12px">{spot['desc']}</p>
    </div>
    """

    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=popup_html,
        icon=folium.Icon(icon="info-sign", color="green")
    ).add_to(m)

# =====================
# 5. 保存为 HTML
# =====================
m.save("tinglin_map.html")

print("✅ tinglin_map.html 已生成")
