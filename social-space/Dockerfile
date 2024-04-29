# syntax=docker/dockerfile:1
FROM node:20-alpine

WORKDIR /react-docker

COPY . .

RUN npm install
ENV HOST=0.0.0.0

CMD ["npm", "start"]

EXPOSE 3000