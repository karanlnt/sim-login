pipeline {
  agent any

  environment {
    DEPLOY_DIR = '/var/www/html'
  }

  stages {
    stage('Clone Repo') {
      steps {
        git branch: 'main', url: 'https://github.com/karanlnt/sim-login.git'
      }
    }

    stage('Install & Build') {
      steps {
        sh 'python3 -m pip install -r requirements.txt'
      }
    }

    stage('Run App') {
      steps {
        sh 'python3 app.py'
      }
    }
  }
}
