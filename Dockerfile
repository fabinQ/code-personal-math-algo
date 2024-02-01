FROM python:3
COPY signal_handler.py /


ENTRYPOINT ["./signal_handler.py"]
