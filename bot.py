from pdf2image import convert_from_path
import requests
import json
import base64
from io import BytesIO
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'YOUR_TESSERACT_PATH'


extracted_text = ""


def extract_text_from_pdf(pdf_path):
    # Convert the PDF pages to images
    images = convert_from_path(pdf_path)

    extracted_text = ""
    for page_image in images:
        # Convert the image to grayscale
        grayscale_image = page_image.convert("L")

        # Use pytesseract to extract text from the grayscale image
        extracted_text += pytesseract.image_to_string(grayscale_image)

    return extracted_text



def chat_with_chatbot(user_input):
    global extracted_text  # Access the global variable

    messages = [
        {"role": "user", "content": user_input}
    ]

    if extracted_text:
        messages.append({"role": "system", "content": extracted_text})

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_API_TOKEN",
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": messages,
        }
    )

    api_response = json.loads(response.text)
    chatbot_reply = api_response["choices"][0]["message"]["content"]

    return chatbot_reply

chatbot_response = ""

while True:
    user_input = input("User: ")

    if user_input.startswith("/extract"):
        _, pdf_path = user_input.split(maxsplit=1)

        try:
            extracted_text = extract_text_from_pdf(pdf_path)
            print("Chatbot: Text extracted from the PDF:")
            print(extracted_text)

            chatbot_response = chat_with_chatbot(extracted_text)
            print("Chatbot:", chatbot_response)
        except Exception as e:
            print(f"Chatbot: Error extracting text from the PDF: {str(e)}")
    else:
        if chatbot_response:
            chatbot_response = chat_with_chatbot(user_input + " " + chatbot_response)
        else:
            chatbot_response = chat_with_chatbot(user_input)

        print("Chatbot:", chatbot_response)
