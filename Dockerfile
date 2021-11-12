FROM python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ADD src /app/src
ADD pyproject.toml /app/
ADD setup.cfg /app/
ADD setup.py /app/
ADD MANIFEST.in /app/

WORKDIR /app

RUN pip install .

EXPOSE 8000

ENTRYPOINT ["python", "-m", "otrium_model.main", "serve", "--host", "0.0.0.0"]
