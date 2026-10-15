pipeline {
    agent any

    environment {
        IMAGE_NAME = 'jenkins-flask-app'
        CONTAINER_NAME = 'jenkins-flask-container'
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from Git repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Preparing Python virtual environment and dependencies...'
                script {
                    if (isUnix()) {
                        sh 'python3 -m pip install --upgrade pip'
                        sh 'python3 -m pip install -r requirements.txt'
                    } else {
                        bat 'python -m pip install --upgrade pip'
                        bat 'python -m pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Executing automated unit tests with pytest...'
                script {
                    if (isUnix()) {
                        sh 'python3 -m pytest test_app.py -v'
                    } else {
                        bat 'python -m pytest test_app.py -v'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker container image: ${IMAGE_NAME}:latest..."
                script {
                    if (isUnix()) {
                        sh "docker build -t ${IMAGE_NAME}:latest ."
                    } else {
                        bat "docker build -t %IMAGE_NAME%:latest ."
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                echo "Deploying container: ${CONTAINER_NAME} on port ${APP_PORT}..."
                script {
                    if (isUnix()) {
                        sh """
                            docker stop ${CONTAINER_NAME} || true
                            docker rm -f ${CONTAINER_NAME} || true
                            docker run -d --name ${CONTAINER_NAME} -p ${APP_PORT}:5000 ${IMAGE_NAME}:latest
                        """
                    } else {
                        bat """
                            docker stop %CONTAINER_NAME% 2>nul || ver >nul
                            docker rm -f %CONTAINER_NAME% 2>nul || ver >nul
                            docker run -d --name %CONTAINER_NAME% -p %APP_PORT%:5000 %IMAGE_NAME%:latest
                        """
                    }
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Verifying container health and HTTP responsiveness...'
                script {
                    if (isUnix()) {
                        sh """
                            sleep 3
                            docker ps -f name=${CONTAINER_NAME}
                            curl -s -f http://localhost:${APP_PORT}/health || exit 1
                        """
                    } else {
                        bat """
                            timeout /t 3 /nobreak >nul
                            docker ps -f name=%CONTAINER_NAME%
                            curl.exe -s -f http://localhost:%APP_PORT%/health || exit 1
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "=========================================================="
            echo "CI/CD Pipeline Completed Successfully!"
            echo "Application is live at: http://localhost:${APP_PORT}"
            echo "Health endpoint is live at: http://localhost:${APP_PORT}/health"
            echo "=========================================================="
        }
        failure {
            echo "=========================================================="
            echo "Pipeline Failed! Check the error log in the stage above."
            echo "=========================================================="
        }
    }
}
