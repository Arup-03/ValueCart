\# 🛒 ValueCart



\### Smart E-Commerce Price Comparison Platform



ValueCart is a smart price comparison web application that helps users find the best price for a product across multiple e-commerce platforms.



Instead of checking different websites manually, users can provide a product URL and ValueCart compares available prices and highlights the best deal.



\---



\## 🚀 Features



\- 🔗 Product URL-based search

\- 🔍 Automatic product extraction

\- 🤝 Product matching

\- 💰 Multi-platform price comparison

\- 🏆 Best deal detection

\- 💸 Savings calculation

\- 📊 Price-sorted comparison results

\- 🛍️ Multiple e-commerce platform support

\- 🔐 Environment variable support for API credentials

\- 📱 Responsive dark-themed interface



\---



\## 🛍️ Supported Platforms



\- Amazon

\- Flipkart

\- Croma

\- Reliance Digital

\- Tata CLiQ



\---



\## 🏗️ Project Architecture



```text

ValueCart/

│

├── app.py

├── config.py

├── requirements.txt

├── README.md

│

├── services/

│   ├── price\_comparator.py

│   ├── product\_extractor.py

│   ├── product\_matcher.py

│   ├── search\_manager.py

│   ├── url\_validator.py

│   └── amazon/

│       └── amazon\_api.py

│

├── platforms/

│   ├── amazon.py

│   ├── flipkart.py

│   ├── croma.py

│   ├── reliance.py

│   ├── tatacliq.py

│   └── platform\_base.py

│

├── data/

├── database/

│

├── templates/

│   └── index.html

│

└── static/

&#x20;   ├── css/

&#x20;   ├── js/

&#x20;   └── image/

