from fastapi import APIRouter

router = APIRouter(prefix="/db", tags=["db"])

@router.get("/getall")
async def get_all():
    return {"message": "Hello World"}