FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install pandas scikit-learn umap-learn matplotlib

CMD ["python", "evaluation.py"]