from fastapi import FastAPI, HTTPException

app = FastAPI()

"""
Converts a patente value in it's corresponding id and returns it

Arguments:
patente_value  – string
"""
def convert_patente_value_to_id(patente_value):
    try:
        #separates letters and numbers parts of patente value
        letters = patente_value[:4]
        numbers = patente_value[4:]
        
        #calculates the letter part of patente for the id
        letters_value = 0
        for i, letter in enumerate(letters, 0):
            letters_value += (ord(letter) - ord('A')) * (26 ** (3 - i))

        value = letters_value * 1000 + int(numbers) + 1

        return str(value/1000)
    except:
        return None
    

"""
Converts a patente_id to patente value and returns it

Arguments:
patente_id  – string
"""
def convert_id_to_patente_value(patente_id):

    patente_id -= 1
    
    #extract letters and numbers part
    numbers = patente_id % 1000
    letters_value = patente_id // 1000

    letters = ""
    #calculates corresponding value for letters part
    for i in range(4):
        letter_value = letters_value % 26
        letters = chr(letter_value + ord('A')) + letters
        letters_value //= 26

    patente = letters + str(numbers).zfill(3)

    return patente

#route to get patente by it's id
@app.get("/patente/{patente_id}")
async def search_record_by_patente_id(patente_id: str):
    patente_id_as_int = 0
    try:
        patente_id_as_int = int(patente_id.replace(".", ""))
    except Exception as e:
        raise HTTPException(
        status_code=404, detail=f"Patente not found"
    )
    
    patent_value = convert_id_to_patente_value(patente_id_as_int)

    return {"patente": patent_value}

#route to get patente id by patente value
@app.get("/id/{patente_value}")
async def search_record_by_patente_value(patente_value: str):

    patente_id = convert_patente_value_to_id(patente_value)
    
    if patente_id is None:
        raise HTTPException(
            status_code=404, detail=f"Patente id not found"
        )
    
    return {"id": patente_id}

@app.get("/")
def main_route():
    return { "message": "Hello" }