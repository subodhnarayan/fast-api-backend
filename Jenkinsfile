
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME = 'fastapi-products'
        REGISTRY = 'us-central1-docker.pkg.dev'
        PROJECT_ID = 'mystical-ally-399418'
        REPOSITORY = 'fastapi-images'
    }

    stages {

        // Stage 1: Checkout source code
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        // Stage 2: Validate Python code
        stage('Validate Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m compileall -q main.py model.py
                    echo "Python validation successful!"
                '''
            }
        }

        // Stage 3: Install application dependencies
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                    echo "Dependencies installed successfully!"
                '''
            }
        }

        // Stage 4: Build Docker image
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                    echo "Docker image built successfully!"
                '''
            }
        }

        // Stage 5: Verify Docker image
        stage('Verify Docker Image') {
            steps {
                sh '''
                    docker image inspect ${IMAGE_NAME}:${BUILD_NUMBER}
                    echo "Docker image verified successfully!"
                '''
            }
        }

        // Stage 6: Push image to Google Artifact Registry
        stage('Push to Artifact Registry') {
            steps {
                sh '''
                    IMAGE_URI="${REGISTRY}/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}"

                    echo "Tagging Docker image..."
                    docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_URI}:${BUILD_NUMBER}

                    echo "Pushing Docker image to Artifact Registry..."
                    docker push ${IMAGE_URI}:${BUILD_NUMBER}

                    echo "Image pushed successfully!"
                '''
            }
        }
    }

    post {
        success {
            echo """
                CI Pipeline completed successfully!

                Image:
                ${REGISTRY}/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:${BUILD_NUMBER}
            """
        }

        failure {
            echo 'CI Pipeline failed. Check the stage logs.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
