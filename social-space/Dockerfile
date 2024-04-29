# syntax=docker/dockerfile:1
FROM node:20-alpine

WORKDIR /react-docker

COPY . .

RUN npm install --production

CMD [ "npm", "start"]

EXPOSE 3000