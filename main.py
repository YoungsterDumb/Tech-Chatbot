from flask import Flask, render_template, request, jsonify
from app import qa_chain
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Create templates directory and static files
import os
if not os.path.exists('templates'):
    os.makedirs('templates')
if not os.path.exists('static'):
    os.makedirs('static')

# Create HTML template
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    try:
        # Use the new invoke method instead of __call__
        response = qa_chain.invoke({"query": question})
        if not response or "result" not in response:
            logger.error(f"Unexpected response format: {response}")
            return jsonify({'error': 'Unexpected response format from model'}), 500
        
        return jsonify({'answer': response["result"]})
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}", exc_info=True)
        return jsonify({'error': 'Có lỗi xảy ra khi xử lý câu hỏi của bạn. Vui lòng thử lại.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
