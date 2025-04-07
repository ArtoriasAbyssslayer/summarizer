# Use official Node.js image
FROM node:alpine

# Set the working directory inside the container
WORKDIR /frontend

# Copy package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend files
COPY . /frontend

# Expose the React development server port
EXPOSE $REACT_DOCKER_PORT
# Run the React app
CMD ["npm", "start"]
