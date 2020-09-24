FROM gcc:10.2

WORKDIR /opt/application/libpng
COPY src/libpng .
RUN ./configure
RUN make check
RUN make install

WORKDIR /opt/application
COPY src/ .
RUN make

WORKDIR /opt/application/work_dir

