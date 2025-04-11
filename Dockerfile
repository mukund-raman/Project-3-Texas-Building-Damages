# Image: mkr2497/texas-building-damages

FROM python:3.11

RUN python -m pip install --upgrade pip && \
    python -m pip install tensorflow==2.19 Flask==3.1.0 Pillow

COPY lenet5_model.keras /lenet5_model.keras
COPY api.py /api.py


CMD ["python", "api.py"]