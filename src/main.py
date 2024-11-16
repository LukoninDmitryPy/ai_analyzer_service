from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import requests

load_dotenv()

from utils.log_utils import getLogger
from utils.xml_utils import get_sales
from utils.ai_utils import send_request_to_ai
from db.requests import add_products, add_answer


app = FastAPI()
logger = getLogger(__name__)

@app.get("/check_route")
async def check_route():
    try:
        response = requests.get("http://127.0.0.1:8000/xml_files/")
        if response.status_code == 200:
            xml_content = response.content
            products = await get_sales(xml_content)
            logger.debug(products)
            add_products(products)
        else:
            logger.error("Route is not working correctly, status: %d", response.status_code)
            return JSONResponse(content={"message": "Route is not working correctly"}, status_code=400)
    except Exception as e:
        logger.exception(e)
        return JSONResponse(content={"message": "Invalid file format or db error"}, status_code=400)
    
    try:
        result = send_request_to_ai(products)
        logger.debug(f'Result of ai: {result}')
        add_answer(result)
    except Exception as e:
        logger.exception(e)
        return JSONResponse(content={"message": "Error while send to ai or db error"}, status_code=400)

    return JSONResponse(content={"message": "File uploaded successfully"}, status_code=200)
