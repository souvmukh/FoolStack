pipeline{
    agent none
    stages{
        stage('Build'){
            agent{
                docker{
                    image 'python:2-alpine'
                }
            }
            steps{
                sh 'python -m py_compile /app.py /makesound.py /mapsound.py /savesound.py'
                stash(name: 'compiled-results', includes: '/*.py*')
            }
        }
    }
}