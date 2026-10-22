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
                     python3.11 -m venv .venv
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


        stage('pylint')
        {
            steps 
            {
                sh '.venv/bin/python -m pylint src/hello_web'
            }
        }
    }
}