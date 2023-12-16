from fastapi import FastAPI, HTTPException, UploadFile, Body
import uvicorn
from calc import Calc

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.post("/calculate")
def calculate(body: str = Body(...)):
    calculation = Calc(body).__calculate_opz__()
    if type(calculation) == float:
        return calculation
    else:
        return HTTPException(400, detail=calculation)
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3003)
