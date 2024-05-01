# syntax=docker/dockerfile:1
FROM node:20-alpine

WORKDIR /react-docker

COPY . .

RUN npm install
RUN npm install -g serve
RUN npm run build

ENV HOST=0.0.0.0

CMD ["serve", "-s", "build"]

EXPOSE 3000