The code base is created to create Fast API end points to faciliate interviewer interviewee interactions.
The fastapi app is hosted on **AWS EC2 instance** http://51.20.129.124/docs 

There are two end points created

* POST: post_graph_invoke
    * The end point invokes a langgraph based graph which is responsible to evaluate interviewee response, store the questions, answers, evaluation in db and generate new question for the interviewee.
* GET: get_evaluation
    * The enpoint calls DB hosted on **AWS RDS** and fetches questions, evaluations and marks for a  given user_id
 

The Frontend repo for 






<img width="404" alt="Screenshot 2025-04-25 at 1 45 45 PM" src="https://github.com/user-attachments/assets/bde0ca2b-9a57-4b70-b94c-8b9a78894bec" />
