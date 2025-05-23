The code base is created to create Fast API end points to faciliate interviewer interviewee interactions.
The fastapi app is hosted on **AWS ECS** http://13.233.156.224/docs 

There are two end points created

* POST: post_graph_invoke
    * The end point invokes a langgraph based graph which is responsible to evaluate interviewee response, store the questions, answers, evaluation in db and generate new question for the interviewee.
* GET: get_evaluation
    * The enpoint calls myslq db on **AWS RDS** and fetches questions, evaluations and marks for a given user_id
  
Streamlit has been used for frontend here is the repo url: https://github.com/gpaikane/interviewer-streamlit-frontend and the hosted app url is http://51.20.190.247/ 

**Details**:
* **POST: post_graph_invoke**
   * Here is the graph created in langgraph for the end point
<img width="404" alt="Screenshot 2025-04-25 at 1 45 45 PM" src="https://github.com/user-attachments/assets/bde0ca2b-9a57-4b70-b94c-8b9a78894bec" />


**Below are the graph componenets:**
* `start`: User id, user name, question, answer of the question, subjects, difficulty level is provided as input
* `policy_checker`: Checks text, checks for blank input , derogatory workds, checks if user directs the model to asks specific questions.
* `evaluator`: Evaluates the answer provided as input, provides marks out of 5 
* `db_state_sync`: Stores user_id, user_name, question, answer, feedback and marks in db, also reads all past questions from db so that they won't get repeated.
* `followup_decider`: Decides to ask a followup question to the already answered question
* `followup_generator`: Generates followup question according to the last question and difficulty level
* `question_generator`: Generates new question according to skill and difficulty level

**POST: get_evaluation**
* queries sql database on  **AWS RDS**: `select question from interview_state where user_id = '{state['user_id']}'`


