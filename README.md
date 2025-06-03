# ChatbotLlama3 - A Webpage run ChatBot built using the Llama3 LLM and LangChain
This project sets up a basic chatbot using the LLaMA model from the Ollama API and Langchain to manage prompts. The bot can chat with users and keeps track of the conversation context.

## **TechStack**

Llama 3.1

Ollama

LangChain

Python

Flask

HTML


## **A simple conversation with the Bot**

![Screenshot 2024-09-17 000509](https://github.com/user-attachments/assets/29f2af70-3c1f-4873-9274-43dc7873e824)


## **Changelog**

**[0.2.0]**

The ChatBot interface is now on a HTML page.
User inputs and responses are handled on the same page.
The conversation context is displayed on the page.

**[0.1.0]**

Completed the terminal run ChatBot.
Added a conversation context to keep track of the entire conversation.
## **Resources**

https://www.youtube.com/watch?v=d0o89z134CQ

https://ollama.com/download

https://github.com/ollama/ollama

pipeline {
    agent any
     environment {
        GIT_REPO = 'https://github.com/sudarsanand/program8.git' // Replace with your GitHub repo
        ANSIBLE_PLAYBOOK = '/etc/ansible/deployApp.yml' // Ansible playbook path
        INVENTORY = '/etc/ansible/hosts'    // Ansible inventory file path
    }
     stages {
        stage('Clone Repository') {
            steps {
                git url: "${GIT_REPO}", branch: 'master'
            }
        }
stage('Deploy with Ansible') {
            steps {
                script {
                    // Run the Ansible playbook to deploy the artifact
                    sh "ansible-playbook -i ${INVENTORY} ${ANSIBLE_PLAYBOOK}"
                }           }        }
 
        stage('Post-Deployment') {
            steps {
                echo 'Deployment completed successfully!'
                      }         }    }
 post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}

---
- name: Deploy Maven Artifact to Web Server
  hosts: webserver
  become: true
  tasks:
      - name: Copy the JAR file to server
        copy:
          src: target/javateam-1.0-SNAPSHOT.jar
          dest: /var/www/html/javateam-1.0-SNAPSHOT.jar
