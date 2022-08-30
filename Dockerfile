FROM python:3.6.1-alpine
# update pip to minimize dependency errors
RUN pip install --upgrade pip
# define the present working directory
WORKDIR /myflaskappdir
# copy the contents into the working dir
ADD . /myflaskappdir
# run pip to install the dependencies of the flask app
RUN pip install -r requirement.txt
# define the command to start the container
CMD ["python","main.py"]