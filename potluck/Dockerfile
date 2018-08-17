#FROM python:3-onbuild

#RUN python3

#RUN pip3 install "Django>=1.11.12"
#RUN pip3 install "django-environ>=0.4.0,<0.5"

#RUN pip3 install -r requirements.txt

#CMD ["./bin/run.sh"]

#EXPOSE 8090
#####################

# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3-onbuild

RUN pip3 install -r requirements.txt

ENV APP_ENV test

# COPY startup script into known file location in container
#COPY .run.sh /run.sh

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8090

# CMD specifcies the command to execute to start the server running.
#CMD ["./bin/run.sh"]

STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8090"]

# done!
