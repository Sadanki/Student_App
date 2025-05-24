pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'python3 -m venv $VENV_DIR'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh './venv/bin/python3 -m pytest tests/'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting Flask app...'
                sh 'nohup ./venv/bin/python3 app.py &'
            }
        }
    }

    post {
        success {
            mail to: 'sadanki190@gmail.com',
                 subject: "✅ SUCCESS: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Build passed. Check here: ${env.BUILD_URL}"
        }
        failure {
            mail to: 'sadanki190@gmail.com',
                 subject: "❌ FAILURE: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Build failed. Fix it here: ${env.BUILD_URL}"
        }
    }
}
