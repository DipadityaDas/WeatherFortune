FROM centos:8

RUN yum -y install python38

WORKDIR /app

COPY . .

RUN pip3 --no-cache-dir install -r requirement.txt

EXPOSE 5000

CMD ["python3","app.py"]
