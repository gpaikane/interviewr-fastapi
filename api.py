from pydantic import BaseModel
from fastapi import FastAPI
from graph.generate_graph import InterviewGraph
from dbconnector.connetsql import read_sql_data

app = FastAPI()

interview = InterviewGraph()
interview_graph = interview.get_graph()
interview_graph_complied = interview_graph.compile()

class InputData(BaseModel):

    difficulty: str
    user_id: str
    user_name:str
    subjects:list
    human_answer:str
    previous_question:str
    max_questions:int
    num_questions:int


@app.post("/post_graph_invoke/")
async def post_graph_invoke(input_data: InputData):


    difficulty = input_data.difficulty
    user_id = input_data.user_id
    user_name = input_data.user_name
    subjects = input_data.subjects
    human_answer = input_data.human_answer
    previous_question = input_data.previous_question
    max_questions = input_data.max_questions
    num_questions = input_data.num_questions

    result = interview_graph_complied.invoke({"difficulty": difficulty,
                                          "user_id": user_id,
                                          "user_name": user_name,
                                          "subjects": subjects,
                                          'human_answer': human_answer,
                                          'previous_question': previous_question,
                                          'max_questions': max_questions,
                                          "num_questions": num_questions
                                          })

    if(result['policy_violation']!='NA'):
        return {"policy_violation": result['policy_violation']}

    selected_data = {"policy_violation": result['policy_violation'],
                     "new_question":result["new_question"],
                     "evaluation":result["evaluation"],
                     "human_answer":result["human_answer"],
                     "marks":result["marks"],
                     "num_questions":result["num_questions"]}
    return selected_data


@app.get("/get_evaluation/")
async def get_evaluation(uuid: str):
    db = "interviews"
    query= f"select question, user_response, evaluation, marks from interview_state where user_id = '{uuid}'"
    result  =read_sql_data(query, db)
    return result