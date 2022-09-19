FROM python:3-alpine
COPY /Scores.txt /Scores.txt
COPY /MainScores.py /MainScores.py
COPY /Utils.py /Utils.py
RUN pip install Flask
RUN pip install Utils
CMD ["python", "/MainScores.py"]

