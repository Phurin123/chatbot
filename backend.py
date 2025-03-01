from transformers import pipeline

def response(user_query):
    # Initialize the pipeline
    pipe = pipeline("text-generation", model="gpt2")
    # Generate the response
    result = pipe(user_query, max_length=200, do_sample=True)

    return result[0]["generated_text"]

# ทดสอบเรียกใช้งาน
query = "What is the capital of France?"
print(response(query))
