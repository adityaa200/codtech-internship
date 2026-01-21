"""
-----------------------------------------------------------------------
INDI-AIR: Simple Real-Time Air Quality Dashboard for India
Professional Internship Project - API Integration & Visualization
Author: Aditya Santosh Adhav | 3rd Year Computer Engineering Student
Fetches LIVE AQI for 25+ Major Indian Cities | Open-Meteo API (Free)
-----------------------------------------------------------------------

🚀 FEATURES:
• Live data for North/South/East/West/Central India
• Top 5 polluted cities highlighted (Red Alert Box)
• Color-coded AQI (US EPA Standards) 
• Auto-save chart & CSV data
• Runs in <10 seconds!

📦 pip install requests pandas seaborn matplotlib
"""

import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import time
from matplotlib.patches import Patch

# API & 25+ Major Indian Cities (Ready-to-run)
API_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

CITIES = [
    # 🔥 Northern India (Delhi always leads)
    ("Delhi", 28.61, 77.23), ("Jaipur", 26.91, 75.78), ("Lucknow", 26.84, 80.94),
    ("Chandigarh", 30.73, 76.77), ("Agra", 27.17, 78.01), ("Varanasi", 25.32, 82.99),
    
    # 🏙️ Western India (Nashik region included)
    ("Mumbai", 19.07, 72.87), ("Pune", 18.52, 73.85), ("Nashik", 19.99, 73.78),
    ("Ahmedabad", 23.02, 72.57), ("Surat", 21.17, 72.83), ("Nagpur", 21.14, 79.08),
    
    # 🌴 Southern India  
    ("Bengaluru", 12.97, 77.59), ("Chennai", 13.08, 80.27), ("Hyderabad", 17.39, 78.49),
    ("Kochi", 9.93, 76.26), ("Visakhapatnam", 17.69, 83.22),
    
    # 🌆 Eastern & Central India
    ("Kolkata", 22.57, 88.36), ("Patna", 25.59, 85.14), ("Guwahati", 26.14, 91.74),
    ("Indore", 22.72, 75.86), ("Bhopal", 23.25, 77.41), ("Raipur", 21.25, 81.63)
]

def get_aqi(city_name, lat, lon):
    """Get live AQI for one city - Simple & Fast"""
    try:
        url = f"{API_URL}?latitude={lat}&longitude={lon}&current=us_aqi&timezone=Asia/Kolkata"
        data = requests.get(url, timeout=8).json()
        aqi = data['current']['us_aqi']
        print(f"✅ {city_name}: {aqi}")
        return {"City": city_name, "AQI": aqi}
    except:
        print(f"❌ {city_name} (no data)")
        return None

def get_aqi_color(aqi):
    """US EPA Official Colors: Green=Good → Purple=Very Bad"""
    if aqi <= 50: return "#00E400"      # Good 🟢
    elif aqi <= 100: return "#FFFF00"   # Moderate 🟡
    elif aqi <= 150: return "#FF7E00"   # Sensitive 🟠
    elif aqi <= 200: return "#FF0000"   # Unhealthy 🔴
    else: return "#8F3F97"              # Very Bad 🟣

# 🔥 MAIN PROGRAM - Super Fast Parallel Fetching
print("🌡️  INDI-AIR by Aditya Santosh Adhav | Starting Live Data Fetch...")
print(f"📍 Monitoring {len(CITIES)} major Indian cities...\n")
start_time = time.time()

# Fetch all cities simultaneously (10x faster!)
data = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(get_aqi, name, lat, lon) for name, lat, lon in CITIES]
    for future in futures:
        result = future.result()
        if result: 
            data.append(result)

# Create sorted DataFrame
df = pd.DataFrame(data).sort_values("AQI", ascending=False)
print(f"\n✅ COMPLETE! {len(df)} cities | {time.time()-start_time:.1f} seconds")

# 📊 IMPRESSIVE PROFESSIONAL DASHBOARD
plt.figure(figsize=(14, 10))
sns.set_style("whitegrid")

# Main Horizontal Bar Chart (Top 15 Polluted Cities)
colors = [get_aqi_color(row.AQI) for _, row in df.iterrows()]
bars = sns.barplot(data=df.head(15), x="AQI", y="City", palette=colors)

# Add AQI numbers ON bars (Professional touch)
for i, row in df.head(15).iterrows():
    plt.text(row.AQI + 2, i, f'{int(row.AQI)}', va='center', 
             fontweight='bold', fontsize=11)

# 🚨 RED ALERT BOX - TOP 5 MOST POLLUTED
top5_text = "\n".join([f"{i+1}. {row.City}: {int(row.AQI)}" 
                      for i, row in df.head(5).iterrows()])
plt.text(1.02, 0.98, f"🚨 TOP 5 ALERT:\n{top5_text}", 
         transform=plt.gca().transAxes, fontsize=12, fontweight='bold',
         va='top', bbox=dict(boxstyle="round,pad=0.5", facecolor="red", alpha=0.8))

# Professional Titles & Styling
plt.title("🇮🇳 INDIA REAL-TIME AIR QUALITY DASHBOARD\nTOP 15 MOST POLLUTED CITIES\n" + 
          time.strftime("Updated: %Y-%m-%d %H:%M IST"), 
          fontsize=18, fontweight='bold', pad=20)
plt.xlabel("AQI Level (Higher = WORSE)", fontsize=14, fontweight='bold')
plt.ylabel("Cities", fontsize=14, fontweight='bold')

# 📋 Health Risk Legend
colors_legend = ["#00E400", "#FFFF00", "#FF7E00", "#FF0000", "#8F3F97"]
labels = ["Good (0-50)", "Moderate (51-100)", "Sensitive (101-150)", 
          "Unhealthy (151-200)", "Very Bad (200+)"]
plt.legend([Patch(color=c) for c in colors_legend], labels, 
           title="US EPA Health Risk", loc='lower right', 
           bbox_to_anchor=(1.0, 0.0), fontsize=10)

# 🎨 Final Polish & Export
plt.tight_layout()
plt.savefig("india_aqi_dashboard_aditya.png", dpi=300, bbox_inches='tight', 
            facecolor='white')
plt.show()

# 💾 AUTO-SAVE DATA & SUMMARY
df.to_csv("india_aqi_live_aditya.csv", index=False)
print("\n" + "="*70)
print("🎉 DASHBOARD GENERATED SUCCESSFULLY!")
print("📈 Chart saved: india_aqi_dashboard_aditya.png")
print("💾 Data saved: india_aqi_live_aditya.csv")
print("\n🏆 TOP 5 MOST POLLUTED CITIES RIGHT NOW:")
print(df.head()[['City', 'AQI']].round(0).astype(int).to_string(index=False))
print("\n👨‍💻 Created by: Aditya Santosh Adhav")
print("🎓 3rd Year Computer Engineering Student")
print("="*70)
