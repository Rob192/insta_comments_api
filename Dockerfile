FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python app/src/download_model.py


