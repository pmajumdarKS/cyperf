FROM ubuntu:22.04

RUN apt update && apt install -y python3-pip python-is-python3 vim wget ca-certificates curl sshpass unzip
RUN gpg --keyserver hkps://keys.openpgp.org --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.17/gosu-$(dpkg --print-architecture)" \
    && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.17/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

COPY envs/entrypoint.sh /usr/local/bin/entrypoint.sh
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt
RUN pip install requests

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
