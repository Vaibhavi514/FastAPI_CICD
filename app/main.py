from fastapi import FastAPI
app =  FastAPI(
    title = "My FastAPi service",
    version = "1.0.0",
)

@app.get("/")
def read_root():
    return {"message" : "Welcome to Vaibhavi's World"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/info")
def get_info():
    return {"app_name" : app.title,
            "version" : app.version,
            "status" : "Running",
            }