import uvicorn
from configs._configs import HOST, PORT

if __name__ == "__main__":
    url = "{}:{}/docs".format(HOST, PORT)
    print(f"Please go to the url '{url}' in your browser for the docs.")
    uvicorn.run("app:app", host=HOST, port=int(PORT), reload=True, debug=True, workers=1)
