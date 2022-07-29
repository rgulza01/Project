pipeline{
  agent any
  environment{
      DATABASE_PASSWORD = credentials('DATABASE_PASSWORD')
      SERVER_NAME = credentials('SERVER_NAME')
      SECRET_KEY = credentials('SECRET_KEY')
  }
  stages{
    stage('setup'){
      steps{
        sh 'export DATABASE_PASSWORD=${DATABASE_PASSWORD}'
        sh 'export SERVER_NAME=${SERVER_NAME}'
        sh 'export SECRET_KEY=${SECRET_KEY}'
        sh "sudo apt install python3-venv -y"
        sh "sudo apt install python3-pip -y"
        sh "python3 -m venv venv"
        sh ". venv/bin/activate"
        sh "pip3 install -r requirements.txt"
      }
    }
    stage('docker swarm'){
      steps{
        sh "docker-compose build"
        sh "docker push radiagulzan/feature_2_image"
        sh "docker stack deploy --compose-file docker-compose.yaml stack_name"
      }
    }
  }
}