# 📡 IoT Data Generator App

A desktop GUI application built with Python that simulates realistic IoT sensor data for 1,000 users, complete with statistical analysis and data visualization tools.

---

## 📖 About the Project

The IoT Data Generator App is a wxPython-based desktop application that generates synthetic IoT data — including user profiles and time-series environmental sensor readings (temperature & humidity). The app lets you explore the data through descriptive statistics and three built-in matplotlib plots, then export as CSV or JSON.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔄 **Data Generation** | Generates 1,000 fake user profiles + up to 1,000 sensor readings per user |
| 🌡️ **Sensor Simulation** | Simulates outside and room temperature & humidity at 6-hour intervals from 2015 to today |
| 👤 **Fake User Profiles** | Uses the `Faker` library for realistic names, addresses, emails, and usernames |
| 📊 **Descriptive Statistics** | Displays a full `describe()` summary of all sensor data in a pop-up dialog |
| 📈 **Plot A** | Histogram of outside temperature distribution |
| 📉 **Plot B** | Line graph comparing outside vs. room temperature (1,000-sample subset) |
| 🗂️ **Plot C** | 2×2 histogram grid of all temperature and humidity columns |
| 💾 **Export to JSON** | Save sensor data as a formatted `.json` file |
| 📁 **Export to CSV** | Save sensor data as a `.csv` file |

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install wxPython pandas numpy matplotlib faker
```

### Running the App

```bash
python "IoT Data Generator App.py"
```

---

## 🖥️ How to Use

1. **Generate data** → `File > Generate IoT`
2. **View statistics** → `Statistics > Descriptive`
3. **Visualize** → `Statistics > Plot A / Plot B / Plot C`
4. **Export** → `File > Save JSON` or `File > Save CSV`
5. **Exit** → `File > Exit`

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| `wxPython` | Desktop GUI framework |
| `pandas` | DataFrame creation and export |
| `numpy` | Numerical support |
| `matplotlib` | Data visualization |
| `faker` | Synthetic user profile generation |

---

## 👩‍💻 Author

**Samantha Scott**
GitHub: [@samanthapscott](https://github.com/samanthapscott)
