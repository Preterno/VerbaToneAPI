# VerbaTone API

This is the backend API for the VerbaTone project, a text-to-speech (TTS) web application powered by a custom-trained Coqui TTS model. The API accepts text input and returns synthesized speech as a downloadable .wav file.

## Features

- Text-to-speech conversion with a custom-trained model
- Accepts text input (up to 1000 characters)
- Returns synthesized audio in `.wav` format
- API key-based authentication for secure access

## Technologies Used

- Flask
- Flask-CORS
- Coqui TTS
- dotenv for environment variables

## Setup and Installation
1. Clone the repository:
   ```
   git clone https://github.com/Preterno/VerbaToneAPI.git
   ```

2. Navigate into the directory:
   ```
   cd VerbaToneAPI
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your API key:
   ```
   API_KEY=your_api_key
   ```

5. Ensure that the `best_model.pth` and `config.json` files are located in the same directory as `app.py`. These files, including the custom-trained model (best_model.pth), are already present in this repository.

6. If you'd like to explore the training process used for the model, you can access the Colab notebook used for training [here]{https://colab.research.google.com/drive/14BtqIO1gkU8TrAsUyI5HG1FQoGWesVb2?usp=sharing}

## Running the Application

Run the Flask app:
   ```
   python app.py
   ```

By default, the app will run on `http://0.0.0.0:5000`.

## API Endpoints

### `POST /synthesize`

This endpoint takes text input and returns the generated audio file.

#### Request Headers:

- `X-API-KEY`: Your API key for authentication

#### Request Body:

- `text`: Text to synthesize (up to 1000 characters)

#### Example Request:

   ```json
   {
     "text": "Hello, world!"
   }
   ```

#### Example Response:

The response will be a `.wav` file containing the synthesized speech.

## Error Codes:

`400`: No text provided or text exceeds 1000 characters
`403`: Invalid API key
`500`: Server error (e.g., model or config file not found)

## Connect with Me

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/aslam8483).