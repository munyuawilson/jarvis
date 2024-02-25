
from io import BufferedReader
import speech_recognition
from pydub import AudioSegment 
import logging



def convert_audio(path: str = None,
                  convert: str = 'wav',
                  stream: BufferedReader = None) -> dict:
    '''
        Convert MP3, OGG, FLV, WMA, ACC and MP4 audio / video files to WAV
        audio file, by default, or any file type supported by FFmpeg
        
        :param str path: Path to a MP3, OGG, FLV, WMA, ACC or MP4 audio /
         video file

        :param str convert: Type to convert the input file to

        :param BufferedReader stream: Stream file

        :rtype: Dict
        
        :raises FileNotFoundError: Audio was not found
    '''
    error_message = None

    try:
        _audio = AudioSegment.from_file_using_temporary_files(stream) \
            if stream else AudioSegment.from_file(path)
    except FileNotFoundError as error:
        error_message = 'Audio file was not found (convert audio)'

        logging.exception(error_message)

        return dict(error=error_message)
    except Exception as error:
        error_message = 'Unexpected error when open audio file (convert audio)'

        logging.exception(error_message)

        return dict(error=error_message)

    audio_converted = _audio.export(format=convert)

    audio_converted.seek(0)

    return dict(
        audio=_audio,
        audio_converted=audio_converted,
        error=error_message
    )


def audio(path: str = None,
          stream: BufferedReader = None) -> dict:
    '''
        Extract text from MP3, OGG, FLV, WMA, ACC, MP4 and WAV audio /
        video files, through Sphinx API
        
        :param str path: Path to an audio / video file
        
        :param BufferedReader stream: Stream file
        
        :rtype: Dict
        
        :raises FileNotFoundError: Audio was not found
    '''
    # If an error is issued at the Pocket Sphinx installation, remove the
    # `apt remove swig`, install the `apt install swig3.0` and create
    # a symbolic link `ln -s /usr/bin/swig3.0 /usr/bin/swig` to the new
    # version
    recognizer = speech_recognition.Recognizer()

    error_message = None

    try:
        _ = convert_audio(
            stream=stream) if stream else convert_audio(path=path)

        if _.get('error'):
            error_message = _.get('error')

            logging.exception(error_message)

            return dict(error=error_message)

        _audio = _.get('audio_converted')

        with speech_recognition.AudioFile(_audio) as file:
            _audio = recognizer.record(file)
    except FileNotFoundError as error:
        error_message = 'Audio file was not found (audio)'

        logging.exception(error_message)

        return dict(error=error_message)
    except Exception as error:
        error_message = 'Unexpected error when open audio file (audio)'

        logging.exception(error_message)

        return dict(error=error_message)

    text_sphinx = recognizer.recognize_sphinx(_audio)

    return dict(
        text=text_sphinx,
        error=error_message
    )