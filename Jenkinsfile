// Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/karanlnt/sim-login.git'
            }
        }

        stage('Install & Build') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t flask-login-app .'
            }
        }

        stage('Run App') {
            steps {
                echo "Running Docker container..."
                sh '''
                    docker rm -f flask-login || true
                    docker run -d -p 7000:7000 --name flask-login flask-login-app
                '''
            }
        }
    }
}
