import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import os
from dotenv import load_dotenv

load_dotenv()
client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)


def text_to_speech_file(text: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="pFZP5JQG7iQjIQuC4Bku", # Lily pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.75,
            similarity_boost=1.0,
            style=1.0,
            use_speaker_boost=True,
        ),
    )
    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path

