import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os

def create_dashboard(df):
    total = len(df)
    total_sus = len(df[df['Status']=='Suspicious'])
    total_normal = len(df[df['Status']=='Normal'])
    fraud_rate = round((total_sus / total) * 100, 1) if total > 0 else 0
    
    sus_df = df[df['Status']=='Suspicious']
    top_region = sus_df['Region'].value_counts().idxmax() if not sus_df.empty else "N/A"
    top_customer = sus_df['Customer_ID'].value_counts().idxmax() if not sus_df.empty else "N/A"

    BG, CARD, BORDER = '#0d1117', '#161b22', '#30363d'
    TEXT, MUTED = '#e6edf3', '#8b949e'
    ACCENT, DANGER, BLUE, WARNING = '#00d4aa', '#ff4757', '#3d8ef8', '#ffa502'
    
    REGION_COLORS = ['#ff4757','#ffa502','#3d8ef8','#2ed573','#a78bfa']
    TYPE_COLORS = ['#ff6b81','#ffa502','#7bed9f']

    fig = make_subplots(
        rows=4, cols=4,
        row_heights=[0.1, 0.28, 0.31, 0.31],
        specs=[
            [{"type":"indicator"},{"type":"indicator"},{"type":"indicator"},{"type":"indicator"}],
            [{"colspan":2}, None, {"colspan":2}, None],
            [{"colspan":2}, None, {"colspan":2}, None],
            [{"colspan":2}, None, {"colspan":2}, None],
        ],
        vertical_spacing=0.07,
        horizontal_spacing=0.06,
        subplot_titles=(
            '','','','',
            'Anomalies by Region', 'Anomalies by Customer Type',
            'Consumption vs Deviation', 'Anomaly Score Distribution',
            'Top 15 Suspicious Customers', 'Suspicious Records by Month'
        )
    )

    kpis = [(total, "TOTAL RECORDS", BLUE), (total_sus, "SUSPICIOUS", DANGER),
            (total_normal, "NORMAL", ACCENT), (fraud_rate, "FRAUD RATE", WARNING)]
    for i, (val, title, col) in enumerate(kpis):
        fig.add_trace(go.Indicator(
            mode="number", value=val,
            title=dict(text=title, font=dict(size=11, color=MUTED)),
            number=dict(font=dict(size=32, color=col), suffix="%" if "RATE" in title else "")
        ), row=1, col=i+1)

    reg_stats = sus_df['Region'].value_counts()
    fig.add_trace(go.Bar(
        x=reg_stats.index, y=reg_stats.values,
        marker_color=REGION_COLORS, showlegend=False
    ), row=2, col=1)

    type_stats = sus_df['Customer_Type'].value_counts()
    fig.add_trace(go.Bar(
        x=type_stats.index, y=type_stats.values,
        marker_color=TYPE_COLORS, showlegend=False
    ), row=2, col=3)

    for status, color, size in [('Normal', BLUE, 4), ('Suspicious', DANGER, 7)]:
        m = df['Status'] == status
        fig.add_trace(go.Scatter(
            x=df[m]['Consumption_kWh'], y=df[m]['Deviation_%'],
            mode='markers', name=status,
            marker=dict(color=color, size=size, opacity=0.4 if status=='Normal' else 0.8)
        ), row=3, col=1)

    fig.add_trace(go.Histogram(
        x=df['Score'], nbinsx=40, 
        marker_color=BLUE, opacity=0.7, showlegend=False
    ), row=3, col=3)

    top_15 = sus_df['Customer_ID'].value_counts().head(15).sort_values(ascending=True)
    fig.add_trace(go.Bar(
        y=top_15.index, x=top_15.values,
        orientation='h', marker_color=DANGER, showlegend=False
    ), row=4, col=1)

    month_map = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',
                 7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    trend = sus_df.groupby('Month').size().reindex(range(1,13), fill_value=0)
    fig.add_trace(go.Scatter(
        x=[month_map[m] for m in trend.index], y=trend.values,
        mode='lines+markers', line=dict(color=WARNING, width=3),
        fill='tozeroy', showlegend=False
    ), row=4, col=3)

   
    fig.update_layout(
        title=dict(
            text=f"SONELGAZ MASCARA - FRAUD ANALYSIS SYSTEM<br><span style='font-size:12px; color:{MUTED}'>Top Suspect: {top_customer} | Region: {top_region}</span>",
            x=0.5, font=dict(size=20, color=TEXT)
        ),
        template="plotly_dark", paper_bgcolor=BG, plot_bgcolor=CARD,
        height=1300, margin=dict(t=120, b=50, l=50, r=50)
    )
    
    output_path = "reports/fraud_dashboard.html"
    if not os.path.exists('reports'): os.makedirs('reports')
    fig.write_html(output_path)
    return output_path