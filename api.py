from pydantic import BaseModel
from fastapi import FastAPI, Query
from graph.generate_graph import InterviewGraph

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
    return result