FROM python:3.8.16-bullseye

WORKDIR /

COPY static/ static/
COPY templates/ templates/
COPY render_templates.py render_templates.py
COPY entrypoint.sh entrypoint.sh

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


EXPOSE 9000
CMD ["./render_templates.py"]