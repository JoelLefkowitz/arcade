FROM node:14.9 AS build

WORKDIR /arcade
ENV PATH /arcade/node_modules/.bin:$PATH

COPY ./package.json /arcade/package.json
RUN npm i

COPY . /arcade/
RUN npx webpack

FROM nginx:1.18

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/common /etc/nginx/common

COPY --from=build arcade/dist/ /etc/nginx/html/
