FROM ubuntu:14.04

RUN apt-get update -q && apt-get upgrade -yq
RUN apt-get install -yq --fix-missing binutils build-essential gettext gdal-bin libgeoip1 libproj-dev libpq-dev npm python-dev python-pip wget && apt-get clean
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN wget -qO /usr/local/bin/forego https://godist.herokuapp.com/projects/ddollar/forego/releases/0.13.1/linux-amd64/forego && test $(sha256sum /usr/local/bin/forego | awk '{print $1}') = "f02640ad733bd92484f98b9ad3ae5ce54e9854f0115bf18c170251661c4f3b76" && chmod +x /usr/local/bin/forego

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD package.json /app/package.json
ADD bower.json /app/bower.json
RUN cd /app ; npm install

ADD . /app
WORKDIR /app

EXPOSE 8000
USER nobody
ENTRYPOINT ["/usr/local/bin/forego"]
CMD ["start", "-p", "8000", "web"]

