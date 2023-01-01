<img
    src="./docs/images/eltiempo.png"
/>

### ☀️ El tiempo
A simple script to scrape some data from [Eltiempo.es](http://eltiempo.es). It uses selenium, css selectors and xpath. Additionally it generates a csv with the obtained data, specifically this script works for the city of Madrid, in the interval of 1 day, in intervals of 1 hour.

### 📦 Installation
1. First, clone the repository:
```
git clone https://github.com/jsonfm/eltiempo-selenium.git
```
2. Create and active a virtual environment:
```
python3 -m venv
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

### 🚀 Run
```
python3 main.py
```