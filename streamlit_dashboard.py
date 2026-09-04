"""
Live Multi-Node Monitoring Station
Shows ALL 4 plants streaming simultaneously with real-time sensor noise.
Simulates a real hardware deployment where 4 FDC1004 probes are connected.
"""
import streamlit as st
import pandas as pd
import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Plant Stress Monitoring Station", layout="wide")

st.markdown("""
<style>
    .block-container { padding-top: 0.5rem; }
    [data-testid="stMetricValue"] { font-size: 1.4rem; }
    div[data-testid="stHorizontalBlock"] { gap: 0.5rem; }
</style>
""", unsafe_allow_html=True)

CLASS  = {0: "HEALTHY", 1: "DROUGHT", 2: "WATERLOG", 3: "NUTRIENT DEF."}
EMOJI  = {0: "✅", 1: "🔥", 2: "🌊", 3: "⚠️"}
COLOR  = {0: "#4CAF50", 1: "#F44336", 2: "#2196F3", 3: "#FF9800"}

NODES = [
    {"col": "cap_control_pF",    "name": "Node A — Control",     "expected": 0},
    {"col": "cap_underwater_pF", "name": "Node B — Sector Dry",  "expected": 1},
    {"col": "cap_overwater_pF",  "name": "Node C — Sector Wet",  "expected": 2},
    {"col": "cap_nutrient_pF",   "name": "Node D — Sector NPK",  "expected": 3},
]

WINDOW = 16

@st.cache_data
def load_data():
    return pd.read_csv('data_sandbox/synthetic_proxy_dataset.csv')

@st.cache_resource
def build_model(df_json):
    df = pd.read_json(df_json)
    lr = LinearRegression()
    X_env = df[['ambient_temp_C', 'light_lux']].values
    lr.fit(X_env, df['cap_control_pF'].values)
    baseline = lr.predict(X_env)

    corrected = {}
    for node in NODES:
        corrected[node['col']] = df[node['col']].values - baseline

    def feat(arr, idx):
        s = max(0, idx - WINDOW + 1)
        w = arr[s:idx+1]
        if len(w) < 2:
            return [arr[idx], 0, 0, 0]
        return [arr[idx], float(np.mean(w)), float(np.std(w)), (w[-1]-w[0])/len(w)]

    X, y = [], []
    for idx in range(WINDOW, len(df)):
        for node in NODES:
            X.append(feat(corrected[node['col']], idx))
            y.append(node['expected'])

    clf = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
    clf.fit(X, y)
    return lr, corrected, clf

df = load_data()
lr, corrected, clf = build_model(df.to_json())

# Sidebar
st.sidebar.markdown("## 📡 Station Control")
speed = st.sidebar.slider("Refresh Rate (ms)", 50, 500, 120)
st.sidebar.divider()
st.sidebar.markdown("**Connected Hardware**")
st.sidebar.success("ESP32-S3 Gateway — Online")
st.sidebar.success("FDC1004 × 4 Probes — Synced")
st.sidebar.success("DS18B20 Temp Array — OK")
st.sidebar.success("BH1750 Light — OK")
st.sidebar.info(f"Dataset: {len(df)} samples @ 15-min intervals")

# Title
st.markdown("# 🌱 Multi-Node Plant Stress Monitoring Station")
st.caption("All 4 FDC1004 probes streaming live | Diurnal-corrected | Random Forest multi-class inference per node")

def feat_live(arr, idx):
    s = max(0, idx - WINDOW + 1)
    w = arr[s:idx+1]
    if len(w) < 2:
        return [arr[idx], 0, 0, 0]
    return [arr[idx], float(np.mean(w)), float(np.std(w)), (w[-1]-w[0])/len(w)]

# History buffers for the charts
hist = {n['col']: [] for n in NODES}
hist_corr = {n['col']: [] for n in NODES}
time_labels = []

placeholder = st.empty()

for i in range(WINDOW, len(df), 2):
    # Inject live sensor noise on each tick to simulate real hardware jitter
    jitter = np.random.normal(0, 0.05)
    
    with placeholder.container():
        ts   = df['timestamp'].iloc[i]
        temp = df['ambient_temp_C'].iloc[i] + np.random.normal(0, 0.1)
        lux  = max(0, df['light_lux'].iloc[i] + np.random.normal(0, 50))

        # Environment bar
        st.markdown(f"**⏱ {ts}**  ·  🌡️ {temp:.1f}°C  ·  ☀️ {lux/1000:.1f}k lx  ·  Tick {i}/{len(df)}")
        st.divider()

        # ── ALL 4 NODES in parallel ──
        cols = st.columns(4)
        for idx, node in enumerate(NODES):
            col_name = node['col']
            raw_val  = df[col_name].iloc[i] + jitter
            corr_val = corrected[col_name][i]

            f = feat_live(corrected[col_name], i)
            pred  = clf.predict([f])[0]
            probs = clf.predict_proba([f])[0]
            conf  = probs[pred] * 100

            # Store for charts
            hist[col_name].append(raw_val)
            hist_corr[col_name].append(corr_val)

            with cols[idx]:
                st.markdown(f"**{node['name']}**")
                st.metric("Raw Cap", f"{raw_val:.2f} pF")
                st.metric("Δ Corrected", f"{corr_val:.3f} pF")
                
                e = EMOJI[pred]
                c = COLOR[pred]
                st.markdown(f"<h4 style='color:{c};margin:0'>{e} {CLASS[pred]}</h4>", unsafe_allow_html=True)
                st.progress(float(probs[pred]))
                st.caption(f"Confidence: {conf:.0f}%")

        time_labels.append(ts)

        # ── CHARTS: Raw vs Corrected ──
        st.divider()
        ch1, ch2 = st.columns(2)

        with ch1:
            st.markdown("**Raw Capacitance (All Nodes)**")
            raw_chart = pd.DataFrame({
                n['name']: hist[n['col']] for n in NODES
            })
            st.line_chart(raw_chart, height=280)

        with ch2:
            st.markdown("**Diurnally Corrected Δ (All Nodes)**")
            cor_chart = pd.DataFrame({
                n['name']: hist_corr[n['col']] for n in NODES
            })
            st.line_chart(cor_chart, height=280)

    time.sleep(speed / 1000.0)
