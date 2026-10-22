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
                    python3 -m venv venv
                    . venv/bin/activate
                    python --version
                '''
            }
        }
    }
}