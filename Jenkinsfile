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


    }
}