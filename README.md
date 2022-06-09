# Seminraska za SP1
## Opis
Projekt je preprosta aplikacija za shranjevanje zapiskov angl. notes.
Videz aplikacije:
![image](https://user-images.githubusercontent.com/71169333/172925337-0096aed1-c312-4708-ab4d-b5c600966642.png)


## Requirements
[python3]('https://www.python.org/downloads/') 

[Node]('https://nodejs.org/en/download/')


## Navodila za namestetitev oz. zagon projekta
```
/** Start Backend **/
open shell
cd backend
python -m virtualenv
env\Scripts\activate.bat
pip install fastapi uvicorn harperdb
python -m uvicorn main:app --reload
```
Slika za pomoč:
Link na katerem se lahko preveri, če backend API-ji delajo: http://127.0.0.1:8000/docs, če dela bi moralo izgledati takole:
![image](https://user-images.githubusercontent.com/71169333/172925387-a4aecd01-b0dc-4c65-b0f9-6a27a352fa0b.png)

/** Stard frontend **/
open new shell
cd frontend
npm start
```
