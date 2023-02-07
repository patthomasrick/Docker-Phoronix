FROM ubuntu:kinetic

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
    && apt install php8.1-cli php8.1-zip php8.1-dom php8.1-gd php8.1-bz2 php8.1-sqlite3 php8.1-curl git -fy

# Install Phoronix Test Suite.
RUN git clone https://github.com/phoronix-test-suite/phoronix-test-suite.git
WORKDIR /phoronix-test-suite

COPY test.sh /phoronix-test-suite/test.sh

# Install the test.
RUN ./phoronix-test-suite install primesieve

CMD ["bash", "./test.sh"]
