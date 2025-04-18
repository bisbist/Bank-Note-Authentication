FROM continuumio/anaconda3:2023.09-0
COPY . /usr/app
EXPOSE 5000
WORKDIR /usr/app/
RUN pip uninstall -y numpy pandas && \
    pip install --no-cache-dir numpy==2.0.2 pandas==2.2.3 && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python","app.py"]