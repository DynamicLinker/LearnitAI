from huggingface_hub import InferenceClient


class AIBuddy:
    def __init__(self, key):
        self.client = InferenceClient(api_key=key)
        self.model = "Qwen/Qwen2.5-7B-Instruct"

    def process_request(self, text, task):
        if task == 'Summarize':
            prompt = f"Summarize these notes into clear, bulleted points: {text[:4000]}"
        elif task == 'Simplify':
            prompt = f"Explain the complex concepts in this text in very simple, beginner-friendly terms: {text[:4000]}"
        elif task == 'Quiz':
            prompt = prompt = f"Generate 5 multiple-choice questions with answers based on this material: {text[:4000]}"
        else:
            prompt = f"You are a helpful and expert AI Tutor. Provide a clear, detailed, and accurate answer to this student's query: {text}"

        response = self.client.chat_completion(
            model=self.model,
            messages=[{'role' : 'user', 'content' : prompt}],
            max_tokens=800
        )

        return response.choices[0].message.content