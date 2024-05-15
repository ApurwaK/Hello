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
                }
                echo 'Python script is getting printed'
            }
        }
    }
                 
}
