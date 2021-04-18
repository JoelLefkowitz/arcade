FROM node:14.9 AS build
WORKDIR /arcade

ARG BUILD_TARGET
ENV PATH /arcade/node_modules/.bin:$PATH

COPY package.json .
RUN npm i

COPY . .
RUN ng run arcade:server:$BUILD_TARGET

ENTRYPOINT ["node", "/arcade/dist/arcade/server"]