docker build -t website_builder .
docker run -v ./:/website website_builder bash -c \
  "cd /build && cp -r /website/* . && cp -r /website/.git . && ./scripts/build.sh && mv public /website/"
