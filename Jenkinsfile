pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Starting repository checkout...'
                git url: 'https://github.com/ApurwaK/Hello.git'
                echo 'Repository checkout complete.'
            }
        }
        stage('Lint JSON files') {
            steps {
                echo 'Installing jsonlint...'
                sh 'npm install -g jsonlint'
                echo 'jsonlint installation complete.'
                
                echo 'Checking jsonlint version...'
                sh 'jsonlint --version'
                
                echo 'Listing JSON files...'
                sh 'ls -l *.json'
                
                echo 'Linting JSON files...'
                sh 'find . -name "*.json" -exec jsonlint -q --indent 4 {} \\;'
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
