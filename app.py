from fastapi import FastAPI
post={"title":"ehsas lab","discription":"ehsas lab is for like minded people"}

app= FastAPI()
@app.get("/")   
def home():
    return{"message":"shukar ha mere first fast api bann gae"}

@app.get("/post")
def get_post():
    return post