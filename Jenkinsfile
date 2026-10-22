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


        stage('pylint')
        {
            steps 
            {
                sh '.venv/bin/python -m pylint src/hello_web'
            }
        }
    }
}