pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/karanlnt/sim-login.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh 'docker build -t flask-login-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo '🚀 Running Docker container...'
                sh '''
                    docker rm -f login-container || true
                    docker run -d -p 7000:7000 --name login-container flask-login-app
                '''
            }
        }
    }
}
