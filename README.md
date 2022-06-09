# Seminraska za SP1
Glavne komponente aplikacije
```
Database: HarperDB
Backend: Python FastAPI
Frontend: React
```
Projekt je preprosta spletna aplikacija za shranjevanje zapiskov angl. notes.
Videz aplikacije:
![image](https://user-images.githubusercontent.com/71169333/172925337-0096aed1-c312-4708-ab4d-b5c600966642.png)


## Requirements
[python3]('https://www.python.org/downloads/') 

[Node]('https://nodejs.org/en/download/')


## Navodila za namestetitev oz. zagon projekta

#### Backend
```
/** Start Backend **/
open shell
cd backend
python -m virtualenv
env\Scripts\activate.bat
pip install fastapi uvicorn harperdb
python -m uvicorn main:app --reload
```
![image](https://user-images.githubusercontent.com/71169333/172925387-a4aecd01-b0dc-4c65-b0f9-6a27a352fa0b.png)
Link do api dokumentacije http://127.0.0.1:8000/docs

#### Frontend
```
/** Start frontend **/
open new shell
cd frontend
npm start
```
