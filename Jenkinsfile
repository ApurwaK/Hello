pipeline {
    agent any
    
    tools {
        nodejs 'Recent node' // Use the NodeJS installation configured in Jenkins
    }
    
    stages {
        stage('Checkout') {
            steps {
                git  'https://github.com/ApurwaK/Hello.git'
            }
        }
        stage('Print python file') {
            steps {
                script{
                 sh 'python pp.py'
                }// This line can be omitted if configured globally
                echo 'Python script is getting printed'
            }
        }
            
            post {
                failure {
                    echo 'JSON indentation check failed!'
                    error 'JSON indentation check failed!'
                }
            }
        }
    }
}
