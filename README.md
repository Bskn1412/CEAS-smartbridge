🏗️ Civil Engineering Insight Studio
AI-Powered Image Analysis for Structural Inspection

Civil Engineering Insight Studio is a web-based application that uses Artificial Intelligence to analyze construction and structural images. It helps engineers, students, and professionals quickly understand site conditions, identify visible defects, and generate inspection reports.

Built with Streamlit and NVIDIA Vision AI, the platform provides instant image-based insights and maintains a history of inspections with PDF export support.

🚀 Features

📸 Upload construction/structure images

🤖 AI-powered image analysis

🏗️ Civil engineering–focused insights

📝 Automatic report generation

📚 Persistent inspection history

📂 Sidebar history viewer

📄 Export reports as PDF

🌐 Web-based interface

🔐 Secure API key management

📋 Prerequisites

Before running this project, make sure you have:

Python 3.9+

NVIDIA API Key (NIM Platform)

Internet connection

Git (optional)

🛠️ Technology Stack
Layer	Technology
Frontend	Streamlit
Backend	Python
AI Model	NVIDIA NIM Vision (LLaMA / Kimi)
Storage	JSON
PDF Generator	ReportLab
Image Processing	Pillow (PIL)
📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/civil-engineering-insight-studio.git
cd civil-engineering-insight-studio

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


If requirements.txt is missing, install manually:

pip install streamlit requests pillow python-dotenv reportlab

4️⃣ Configure API Key

Create a .env file in the root directory:

NVIDIA_API_KEY=your_api_key_here


⚠️ Do NOT upload this file to GitHub.

▶️ Usage
Run the Application
streamlit run app.py


The app will open in your browser:

http://localhost:8501

How to Use

Upload an image of a structure/site

(Optional) Enter custom instruction

Click Analyze

View AI-generated insights

Access past reports in sidebar

Export PDF if required

📁 Project Structure
civil-engineering-insight-studio/
│
├── app.py
├── history.json
├── .env
├── requirements.txt
├── README.md
└── assets/

📄 Report History System

All inspections are stored in history.json

Accessible from sidebar

Persists after closing browser

Supports PDF export

🧪 Performance
Parameter	Value
Avg Response Time	5–15 sec
Image Size Limit	~1 MB
PDF Generation	< 3 sec
Concurrent Users	Local Only
⚠️ Limitations

Depends on API availability

Free tier has rate limits

Internet required

AI output may vary

Not a replacement for physical inspection

🔮 Future Enhancements

Mobile application

User authentication

Cloud database

Drone image integration

Real-time monitoring

BIM integration

Multi-language support

🤝 Contributing

Contributions are welcome!

Steps:

Fork repository

Create branch

Commit changes

Submit pull request

📜 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute it for academic and commercial purposes.

👨‍💻 Author

Developed by: [Your Name]
Department: Civil Engineering
Institution: [Your College Name]

📞 Support

If you face any issues:

Open an issue on GitHub

Contact the maintainer

Refer to NVIDIA NIM Docs

⭐ Acknowledgements

NVIDIA AI Platform

Streamlit Community

Open Source Contributors
