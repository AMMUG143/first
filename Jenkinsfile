<<<<<<< HEAD
pipeline{
    agent any
    stages{
        stage("git clone"){
            steps{

                git url:"https://github.com/AMMUG143/first.git", branch: 'main'

            }
        }
        stage('install dependencies'){
            steps{
                bat '''
                C:\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m venv venv
                venv\\Scripts\\activate
                pip install --upgrade pip
                pip install pytest
                '''

            }
        }
        stages("testing"){
            steps{
                bat '''
                    venv\\Scripts\\activate
                    pytest test.py
                '''
            }
        }
        stages("deploy"){
            steps{
                bat '''
                venv\\Scripts\\activate
                C:\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe helo.py
                '''
                
                
            }
        }
    }
}
=======
pipeline{
    agent any
    stages{
        stage("git clone"){
            steps{

                git url:https://github.com/AMMUG143/first.git", branch: 'main'

            }
        }
        stage('install dependencies'){
            steps{
                bat '''
                C:\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m venv venv
                venv\\Scripts\\activate
                pip install --upgrade pip
                pip install pytest
                '''

            }
        }
        stages("testing"){
            steps{
                bat '''
                    venv\\Scripts\\activate
                    pytest test.py
                '''
            }
        }
        stages("deploy"){
            steps{
                bat '''
                venv\\Scripts\\activate
                C:\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe helo.py
                '''
                
                
            }
        }
    }
}
>>>>>>> 38fcaa55cd32185c87d866c8e0d4c99556d4ff1c
