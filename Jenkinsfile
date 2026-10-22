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

        stage('Installing dependencies') 
        {
            steps 
            {
                sh '.venv/bin/python3 -m pip install requirements.txt'
            }
        }


        stage('pylint')
        {
            steps 
            {
                sh '.venv/bin/python -m pylint src/hello_web'
            }
        }
    }
}