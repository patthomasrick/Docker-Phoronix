FROM ubuntu:kinetic

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
    && apt install wget php8.1-cli php8.1-zip -fy
RUN wget https://phoronix-test-suite.com/releases/repo/pts.debian/files/phoronix-test-suite_10.8.4_all.deb -O phoronix.deb \
    && dpkg -i phoronix.deb \
    || apt install -fy

COPY test.sh /test.sh

CMD ["bash", "/test.sh"]
