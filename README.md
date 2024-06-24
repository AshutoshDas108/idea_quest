# Fraud Detection System Setup Guide

This guide will help you set up the Fraud Detection System on your local machine. Follow the steps below to get both the Machine Learning Model and the React frontend up and running.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [GitHub Desktop](https://desktop.github.com/) or Git
- [Node.js](https://nodejs.org/en/download/) and npm

## Machine Learning Model Setup

1. **Install Docker**
   - Download and install Docker from the [official website](https://www.docker.com/get-started).
   - Verify the installation by running the following command in your terminal:
     ```sh
     docker --version
     ```

2. **Clone the Project**
   - Use GitHub Desktop to clone the repository or download the zip file and extract it.
   - If using Git, run the following command:
     ```sh
     git clone <repository-url>
     ```

3. **Open Terminal**
   - Navigate to the project root directory where the repository was cloned.

4. **Navigate to Spring Boot Backend Directory**
   - Change directory to the `fdm_server` where the Spring Boot backend is located:
     ```sh
     cd fdm_server
     ```

5. **Build Docker Image**
   - Run the following Maven command to build the Docker image:
     ```sh
     mvn compile jib:dockerBuild
     ```

6. **Return to Root Directory**
   - Change back to the root directory:
     ```sh
     cd ..
     ```

7. **Run Docker Compose**
   - From the root directory, build and start the Docker containers using:
     ```sh
     docker-compose up --build
     ```

## React Frontend Setup

1. **Navigate to React Frontend Directory**
   - From the root directory, move to the `fdm_client` directory:
     ```sh
     cd fdm_client
     ```

2. **Install Dependencies**
   - Run the following command to install the necessary npm packages:
     ```sh
     npm install
     ```

3. **Start the Development Server**
   - Start the React development server using:
     ```sh
     npm run dev
     ```

Your Fraud Detection System should now be up and running! Access the frontend at `http://localhost:3000` and ensure that the backend services are properly communicating.

## Troubleshooting

- Ensure Docker is running properly.
- Verify that the backend Spring Boot service is accessible.
- Check for any errors in the terminal and address dependencies or configuration issues.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy using the Fraud Detection System! If you encounter any issues, please open an issue on GitHub.

