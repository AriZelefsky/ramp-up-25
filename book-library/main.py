from fastapi import FastAPI
import schemas
app = FastAPI()

fakeDatabase = {
    1:{
        'title':'The Forgotted',
        'author':'Baldaccaci',
        'year':2018
    },
    2:{
        'title':'Moby Dick',
        'author':'Herman Melville',
        'year':1850
    },
}

@app.get('/')
def getAllBooks():
    return fakeDatabase


@app.get("/{id}")
def getBook(id:int):
    return fakeDatabase[id]

@app.post("/")
def addItem(book:schemas.Book):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {
        'title':book.title,
        'author':book.author,
        'year':book.year
    }
    return fakeDatabase

@app.put("/{id}")
def updateItem(id:int, book:schemas.Book):
    fakeDatabase[id] = {
        'title':book.title,
        'author':book.author,
        'year':book.year
    }    
    return fakeDatabase

@app.delete("/{id}")
def deleteItem(id:int):
    del fakeDatabase[id]
    return fakeDatabase
