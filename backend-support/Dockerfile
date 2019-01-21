FROM node:9.11.1-alpine

# make the 'app' folder the current working directory
RUN mkdir /app
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

EXPOSE 8081
CMD [ "npm", "run serve" ]