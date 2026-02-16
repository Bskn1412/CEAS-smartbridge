<h1 align="center">🏗️ Civil Engineering Insight Studio</h1>

<h3 align="center">AI-Powered Image Analysis for Structural Inspection</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg"/>
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red.svg"/>
  <img src="https://img.shields.io/badge/NVIDIA-Vision_AI-green.svg"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg"/>
</p>

<hr/>

<h2>📌 Overview</h2>

<p>
Civil Engineering Insight Studio is a web-based application that uses Artificial Intelligence
to analyze construction and structural images. It provides instant technical insights,
automated reports, and maintains inspection history.
</p>

<hr/>

<h2>🚀 Features</h2>

<ul>
  <li>📸 Upload construction images</li>
  <li>🤖 AI-powered visual analysis</li>
  <li>🏗️ Engineering-focused insights</li>
  <li>📝 Auto-generated reports</li>
  <li>📚 Persistent history</li>
  <li>📄 PDF export</li>
  <li>🌐 Web-based interface</li>
  <li>🔐 Secure API integration</li>
</ul>

<hr/>

<h2>📋 Prerequisites</h2>

<ul>
  <li>Python 3.9 or above</li>
  <li>NVIDIA API Key</li>
  <li>Internet connection</li>
  <li>Git (optional)</li>
</ul>

<hr/>

<h2>🛠️ Technology Stack</h2>

<table border="1" cellpadding="8">
<tr>
<th>Layer</th>
<th>Technology</th>
</tr>

<tr>
<td>Frontend</td>
<td>Streamlit</td>
</tr>

<tr>
<td>Backend</td>
<td>Python</td>
</tr>

<tr>
<td>AI Model</td>
<td>NVIDIA NIM Vision</td>
</tr>

<tr>
<td>Storage</td>
<td>JSON</td>
</tr>

<tr>
<td>PDF Export</td>
<td>ReportLab</td>
</tr>

<tr>
<td>Image Processing</td>
<td>Pillow (PIL)</td>
</tr>
</table>

<hr/>

<h2>📦 Installation</h2>

<h3>1️⃣ Clone Repository</h3>

<pre><code>
git clone https://github.com/your-username/civil-engineering-insight-studio.git
cd civil-engineering-insight-studio
</code></pre>

<hr/>

<h3>2️⃣ Create Virtual Environment (Recommended)</h3>

<pre><code>
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows
</code></pre>

<hr/>

<h3>3️⃣ Install Dependencies</h3>

<pre><code>
pip install -r requirements.txt
</code></pre>

<p><b>OR</b></p>

<pre><code>
pip install streamlit requests pillow python-dotenv reportlab
</code></pre>

<hr/>

<h3>4️⃣ Configure API Key</h3>

<p>Create a <code>.env</code> file:</p>

<pre><code>
NVIDIA_API_KEY=your_api_key_here
</code></pre>

<p>⚠️ Do not upload this file to GitHub.</p>

<hr/>

<h2>▶️ Usage</h2>

<h3>Run Application</h3>

<pre><code>
streamlit run app.py
</code></pre>

<p>Open in browser:</p>

<pre><code>
http://localhost:8501
</code></pre>

<hr/>

<h3>How to Use</h3>

<ol>
  <li>Upload image</li>
  <li>Enter optional prompt</li>
  <li>Click Analyze</li>
  <li>View result</li>
  <li>Check sidebar history</li>
  <li>Export PDF</li>
</ol>

<hr/>

<h2>📁 Project Structure</h2>

<pre><code>
civil-engineering-insight-studio/
│
├── app.py
├── history.json
├── .env
├── requirements.txt
├── README.md
└── assets/
</code></pre>

<hr/>

<h2>📄 History Management</h2>

<ul>
  <li>Stored in <code>history.json</code></li>
  <li>Accessible via sidebar</li>
  <li>Persistent storage</li>
  <li>Supports PDF export</li>
</ul>

<hr/>

<h2>🧪 Performance</h2>

<table border="1" cellpadding="8">

<tr>
<th>Parameter</th>
<th>Value</th>
</tr>

<tr>
<td>Response Time</td>
<td>5–15 sec</td>
</tr>

<tr>
<td>Image Size</td>
<td>&lt; 1 MB</td>
</tr>

<tr>
<td>PDF Generation</td>
<td>&lt; 3 sec</td>
</tr>

<tr>
<td>Concurrent Users</td>
<td>Local</td>
</tr>

</table>

<hr/>

<h2>⚠️ Limitations</h2>

<ul>
  <li>Requires internet</li>
  <li>Free API limits</li>
  <li>Depends on AI accuracy</li>
  <li>No physical inspection</li>
</ul>

<hr/>

<h2>🔮 Future Scope</h2>

<ul>
  <li>Mobile App</li>
  <li>User Login</li>
  <li>Cloud Database</li>
  <li>Drone Integration</li>
  <li>BIM Support</li>
  <li>Real-Time Monitoring</li>
</ul>

<hr/>

<h2>🤝 Contributing</h2>

<ol>
  <li>Fork repository</li>
  <li>Create branch</li>
  <li>Commit changes</li>
  <li>Submit pull request</li>
</ol>

<hr/>

<h2>📜 License</h2>

<p>
This project is licensed under the <b>MIT License</b>.
</p>

<hr/>

<h2>👨‍💻 Author</h2>

<p>
<b>Name:</b> Your Name <br/>
<b>Department:</b> Civil Engineering <br/>
<b>Institution:</b> Your College Name
</p>

<hr/>

<h2>📞 Support</h2>

<ul>
  <li>Open GitHub issue</li>
  <li>Contact maintainer</li>
  <li>Refer NVIDIA Docs</li>
</ul>

<hr/>

<h2>⭐ Acknowledgements</h2>

<ul>
  <li>NVIDIA AI Platform</li>
  <li>Streamlit Community</li>
  <li>Open Source Contributors</li>
</ul>

<hr/>

<p align="center">
⭐ If you like this project, please star the repository!
</p>
