# 🛒 BasketBrain AI

> An AI-powered grocery comparison assistant built for the **Google GenAI Hackathon 2026**.

BasketBrain helps users compare grocery prices across multiple quick-commerce platforms and recommends the best shopping option using **Google Gemini AI**.

---

## ✨ Features

- 🛍 Compare grocery prices
- 💰 Calculate total basket cost
- 🚚 Compare estimated delivery time
- 🤖 AI-powered shopping recommendation (Gemini)
- 📊 Interactive price comparison chart
- ⚡ Clean Streamlit interface

---

## 🖥️ Demo

Users simply enter a grocery list:

```
Milk
Bread
Rice
Eggs
```

BasketBrain automatically:

- Searches available products
- Calculates basket cost
- Compares Blinkit, Zepto, Instamart and BigBasket
- Finds the cheapest store
- Estimates delivery time
- Generates an AI shopping recommendation using Gemini

---

## 📸 Screenshots

*(Add screenshots later)*

```
screenshots/
```

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- Google Gemini API
- Git
- GitHub

---

## 📂 Project Structure

```
BasketBrain/
│
├── assets/
├── data/
│   └── grocery_prices.csv
├── screenshots/
├── notebooks/
│
├── main.py
├── optimizer.py
├── gemini_helper.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ananya-jais/BasketBrain.git
```

Move inside the folder

```bash
cd BasketBrain
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run main.py
```

---

## 🤖 Gemini AI

BasketBrain uses **Google Gemini 2.5 Flash** to generate:

- Shopping insights
- Best store recommendation
- Savings tips
- Delivery comparison
- Overall basket analysis

---

## 🌟 Future Improvements

- Barcode scanner
- OCR bill reader
- Voice shopping
- Live APIs from grocery platforms
- Location-aware recommendations
- Price history tracking
- Personalized shopping preferences

---

## 👩‍💻 Author

**Ananya Jaiswal**

B.Sc. (Hons.) Computer Science  
University of Delhi

GitHub:
https://github.com/ananya-jais

---

## 📜 License

This project is created for learning and hackathon purposes.