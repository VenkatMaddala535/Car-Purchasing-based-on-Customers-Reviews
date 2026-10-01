pipeline
{
    agent
    {
        label 'pipeline-linux-aget'
    }
    stages
    {
        stage('Creating Virtual Environment')
        {
            steps
            {
                sh '''
                python3 --version
                pip --version
                git --version
                docker --version
                '''
            }
        }
        stage('Create Virtual Environment') 
        {
            steps 
            {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python --version
                '''
            }
        }
    }
}