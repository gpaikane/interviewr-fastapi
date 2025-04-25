The code base is created to create Fast API end points to faciliate interviewer interviewee interactions.
The fastapi app is hosted on **AWS EC2 instance** http://51.20.129.124/docs 

There are two end points created

* POST: post_graph_invoke
    * The end point invokes a langgraph based graph which is responsible to evaluate interviewee response, store the questions, answers, evaluation in db and generate new question for the interviewee.
* GET: get_evaluation
    * The enpoint calls myslq db on **AWS RDS** and fetches questions, evaluations and marks for a given user_id
  
Streamlit has been used for frontend here is the repo url: https://github.com/gpaikane/interviewer-streamlit-frontend

**Details**:
* **POST: post_graph_invoke**
   * Here is the graph created in langgraph for the end point
<img width="404" alt="Screenshot 2025-04-25 at 1 45 45 PM" src="https://github.com/user-attachments/assets/bde0ca2b-9a57-4b70-b94c-8b9a78894bec" />


**Below are the graph componenets:**
* `start`: User id, user name, question, answer of the question, subjects, difficulty level is provided as input
* `policy_checker`: Checks text, checks for blank input , derogatory workds, checks if user directs the model to asks specific questions.
* `evaluator`: Evaluates the answer provided as input, provides marks out of 5 
* `db_state_sync`: stores user_id, user_name, question, answer, feedback and marks in db, also reads all past questions from db so that they won't get repeated.
* ``

