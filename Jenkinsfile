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
        stage('Install JSONLint') {
            steps {
                // JSONLint should already be installed globally, so this step is just for demonstration
                // sh 'npm install -g jsonlint' // This line can be omitted if configured globally
                echo 'JSONLint is assumed to be installed globally'
            }
        }
         stage('Lint JSON files') {
            steps {
                // Windows-specific command to find and lint JSON files
                bat '''
                for /R %%i in (*.json) do (
                    jsonlint --quiet --indent 4 "%%i" || exit /b 1
                )
                '''
            }
    }
                 
}
