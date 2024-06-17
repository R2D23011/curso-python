import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class = HTMLResponse) 
def get_list():
    return'''
        <h1>1, 2 , 3 , 4 </h1>
    '''

@app.get('/contact', response_class = HTMLResponse) 
def get_list():
    return '''
        <h1>Hola soy una pagina</h1>
        <t>MI PAGINA WEB </p>
        <p>SOY UN PARRAFO</p>
    '''

def run():
    store.get_categories()

if __name__ == '__main__':
    run()