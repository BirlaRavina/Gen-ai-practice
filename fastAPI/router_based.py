from fastapi import FastAPI, APIRouter
router = APIRouter()

@router.get('/', tags=['this'])
def routerAPI():
    return {"message": "this is router bases api"}

@router.post('/', tags=['this'])
def routerAPI():
    return {"message": "post api"}

@router.put('/')
def routerAPI():
    return {"message": "patch api"}

app = FastAPI()
app.include_router(router, prefix='/api')