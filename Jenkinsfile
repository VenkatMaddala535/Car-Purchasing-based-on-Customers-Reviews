pipeline
{
    agent
    {
        label 'pipeline-agent'
    }
    stages
    {
        stage('Create Virtual Environment') 
        {
            steps 
            {
                sh '''
                     python -m venv .venv
                '''
            }
        }

        stage('Installing dependencies') 
        {
            steps 
            {
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        // stage('pylint')
        // {
        //     steps 
        //     {
        //         sh '.venv/bin/python -m pylint CarPurchase'
        //     }
        // }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    script {
                        def scannerHome = tool 'SonarScanner'
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=car-purchasing-reviews \
                            -Dsonar.projectName=Car-Purchasing-based-on-Customers-Reviews \
                            -Dsonar.sources=.
                        """
                    }
                }
            }
        }

        stage('Build and save artifact') {
            steps {
                sh '''
                    rm -rf dist
                    mkdir -p dist
                    zip -r dist/car-purchasing-reviews.zip . \
                        -x ".git/*" ".venv/*" "venv/*" \
                        "__pycache__/*" "*/__pycache__/*" \
                        "dist/*" "*.pyc"
                '''
                archiveArtifacts artifacts: 'dist/*.zip', fingerprint: true
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                        -t car-purchasing-based-on-customers-reviews:${BUILD_NUMBER} \
                        -t car-purchasing-based-on-customers-reviews:latest .

                    docker images | grep car-purchasing-based-on-customers-reviews
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'DEBUG 1: Push stage started'

                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-push-cred',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        set -eu

                        echo "DEBUG 2: Credentials loaded"
                        DOCKERHUB_REPO="${DOCKERHUB_USER}/car-purchasing-based-on-customers-reviews"

                        echo "DEBUG 3: Checking Docker access"
                        docker info >/dev/null

                        echo "DEBUG 4: Logging in"
                        # docker login --username <username> --password-stdin
                        echo "$DOCKERHUB_TOKEN" | docker login --username "$DOCKERHUB_USER" --password-stdin

                        echo "DEBUG 5: Tagging images"
                        # docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
                        docker tag car-purchasing-based-on-customers-reviews:${BUILD_NUMBER} "$DOCKERHUB_REPO:${BUILD_NUMBER}"
                        docker tag car-purchasing-based-on-customers-reviews:latest "$DOCKERHUB_REPO:latest"

                        echo "DEBUG 6: Pushing images"
                        docker push "$DOCKERHUB_REPO:${BUILD_NUMBER}"
                        docker push "$DOCKERHUB_REPO:latest"

                        docker logout
                        echo "DEBUG 7: Push completed"
                    '''
                }
            }
        }


    }
}