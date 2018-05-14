<p align="center">
  <a href="#">
    <img alt="predictlybot" src="https://www.predictly.co/robotic.png" width="128"><br/>    
  </a>
  <sub>Icon by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">Good Ware</a></sub>
</p>

<p align="center">
    Train your own Natural Language Processor straight from your browser With <a href="https://www.predictly.co/predictlybot/">PredictlyBot</a>!
</p>


---

## What?
PredictlyBot allows you to build, train, and classify your own sentences via a Web UI. 
PredictlyBot can also communicate with your applications through a RESTful API.

In other words, PredictlyBot aims to be a free, open sourced alternative to  <a href="http://wit.ai">api.ai</a>, <a href="http://wit.ai">luis.ai</a>, and <a href="http://wit.ai">wit.ai</a>

predictlybot turns words into meanings (with enough training data), for example:

- `Ram lives in Bangalore` -> `{'person': 'Ram', 'location': 'Bangalore`'}`
- `Turbo Charge your Website with Luminate.ai ` -> `{'Organization': 'Luminate.ai'}`
- `Close the door` -> `{'action': 'close', 'object': 'door'}`

---
 
## Getting started

```
git clone https://github.com/predictlytechlabs/predictlybot/
cd predictlybot

npm install -g bower
bower install

pip install -r requirements.txt

# Optional, doing this will yeild more accurate
# predictions, however will have a slower startup
# time. Its downloading pre-processed data.
python -m spacy.en.download --force all 
python manage.py migrate
python manage.py runserver
```

Then navigate to `http://127.0.0.1:8000` to view your own Natural Language Processor!

---

## Contributing

Currently we're using `React` frontend coupled with a `django` backend. JavaScript files are written in `jsx` and then compiled to `js` using gulp.

### Frontend
To get started with frontend development, make sure you have `npm`, `bower`, `gulp` installed globally.

```
npm install -g bower
npm install -g gulp
npm install
bower install
gulp
```

### Backend
To get started with backend development, make sure you have installed everything in the requirements installed
```
pip install -r requirements
```

---

