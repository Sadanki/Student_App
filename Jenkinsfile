pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Build') {
            steps {
                echo '📦 Installing dependencies...'
                sh 'python3 -m venv $VENV_DIR'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                script {
                    if (fileExists('tests')) {
                        sh './venv/bin/python3 -m pytest tests/'
                    } else {
                        echo "⚠️ 'tests/' directory not found. Skipping tests."
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Starting Flask app...'
                sh 'nohup ./venv/bin/python3 app.py &'
            }
        }
    }

    post {
        success {
            echo '✅ Build succeeded. Sending email...'
            withCredentials([string(credentialsId: 'GMAIL_APP_PASSWORD', variable: 'GMAIL_APP_PASSWORD')]) {
                sh 'GMAIL_APP_PASSWORD=$GMAIL_APP_PASSWORD python3 send_email.py SUCCESS ${BUILD_URL}'
            }
        }

        failure {
            echo '❌ Build failed. Sending email...'
            withCredentials([string(credentialsId: 'GMAIL_APP_PASSWORD', variable: 'GMAIL_APP_PASSWORD')]) {
                sh 'GMAIL_APP_PASSWORD=$GMAIL_APP_PASSWORD python3 send_email.py FAILURE ${BUILD_URL}'
            }
        }
    }
}
