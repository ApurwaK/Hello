pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository from GitHub
                git 'https://github.com/ApurwaK/Hello.git'
            }
        }
        stage('Validate JSON - First Script') {
            steps {
                echo 'Executing first Python script...'
                sh 'python pp.py'
                echo 'First Python script execution completed.'
            }
        }
        stage('Validate JSON - Another Script') {
            steps {
                echo 'Executing another Python script...'
                dir('.github/script'){
                sh 'python validate_json.py'
                echo 'Another Python script execution completed.'
            }
        }
    }
}
}
