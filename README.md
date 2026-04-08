<h1 align="center">⚡ Electrical Fraud Detection & Anomaly Analysis System</h1>

<p align="center">
  <strong>Intelligent system for detecting and predicting fraudulent electricity consumption</strong>
</p>

<p align="center">
  Author: <b>Belkacem Abdelkader Marouf</b>
</p>

<hr>

<h2>📌 Overview</h2>
<p>
This project focuses on detecting <b>Non-Technical Losses (NTL)</b> such as electricity theft and meter tampering 
within power distribution networks.
</p>

<p>
Using <b>unsupervised machine learning</b>, the system analyzes consumption patterns and identifies abnormal behaviors 
that significantly deviate from expected usage.
</p>

<p><b>Goal:</b></p>
<ul>
  <li>Detect fraud early</li>
  <li>Prioritize inspections</li>
  <li>Improve grid efficiency</li>
</ul>

<hr>

<h2>🚀 Key Features</h2>
<ul>
  <li>✅ <b>Fraud Classification:</b> Classifies users as Normal or Suspicious</li>
  <li>✅ <b>Anomaly Detection:</b> Uses Isolation Forest algorithm</li>
  <li>✅ <b>Predictive Analysis:</b> Identifies high-risk customers</li>
  <li>✅ <b>Regional Insights:</b> Detects fraud hotspots (Ghriss, Sig, Tighennif)</li>
  <li>✅ <b>Interactive Dashboards:</b> Plotly-based visual reports</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
fraud_detection_project/
├── src/
│   ├── main.py
│   ├── visualization.py
│   └── analyzers/
│       └── fraud_detector.py
│
├── data/
│   ├── sonelgaz_mascara_data.xlsx
│   ├── fraud_classified.csv
│   └── risk_predictions.csv
│
├── reports/
├── requirements.txt
└── .gitignore
</pre>

<hr>

<h2>⚙️ Installation</h2>

<h3>1. Clone Repository</h3>
<pre><code>git clone https://github.com/your-username/fraud_detection_project.git
cd fraud_detection_project</code></pre>

<h3>2. Create Virtual Environment</h3>
<pre><code>python -m venv venv</code></pre>

<p><b>Activate:</b></p>
<ul>
  <li><b>Windows:</b> <code>venv\Scripts\activate</code></li>
  <li><b>Mac/Linux:</b> <code>source venv/bin/activate</code></li>
</ul>

<h3>3. Install Dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<h2>▶️ Usage</h2>
<pre><code>python src/main.py</code></pre>

<hr>

<h2>📊 Results</h2>

<h3>📈 Dashboard</h3>
<p>Open: <code>reports/fraud_dashboard.html</code> in your browser</p>

<h3>📄 Outputs</h3>
<ul>
  <li><b>fraud_classified.csv</b> → Classified users</li>
  <li><b>risk_predictions.csv</b> → High-risk users</li>
</ul>

<hr>

<h2>🤝 Contribution</h2>
<p>Contributions are welcome!</p>

<ol>
  <li>Fork the repository</li>
  <li>Create a branch:
    <pre><code>git checkout -b feature/new-feature</code></pre>
  </li>
  <li>Commit changes</li>
  <li>Submit a Pull Request</li>
</ol>

<hr>

<h2>📜 License</h2>
<p>This project is licensed under the <b>MIT License</b>.</p>

<hr>

<h2>💡 Future Improvements</h2>
<ul>
  <li>Real-time smart meter integration</li>
  <li>Deep learning models</li>
  <li>Web dashboard deployment</li>
  <li>API for utility companies</li>
</ul>

<hr>

<p align="center">🚀 Built for innovation, impact, and smarter energy systems</p>
